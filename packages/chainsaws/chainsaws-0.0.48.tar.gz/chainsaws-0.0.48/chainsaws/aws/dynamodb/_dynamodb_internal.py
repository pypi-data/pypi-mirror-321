import logging
import time
from concurrent.futures import ThreadPoolExecutor
from typing import Any, Literal, Dict, List, Optional, Tuple

from boto3 import Session
from boto3.dynamodb.conditions import Attr, Key
from boto3.dynamodb.types import TypeDeserializer, TypeSerializer
from botocore import client
from botocore.waiter import WaiterError
import aioboto3

from chainsaws.aws.dynamodb._dynamodb_utils import decode_dict, divide_chunks
from chainsaws.aws.dynamodb.dynamodb_models import DynamoDBAPIConfig
from chainsaws.aws.dynamodb.dynamodb_exception import DynamoDBError

logger = logging.getLogger(__name__)
type_deserializer = TypeDeserializer()
type_serializer = TypeSerializer()


class DynamoDB:
    """DynamoDB client wrapper for simplified table operations."""

    def __init__(self, boto3_session: Session, table_name: str, config: Optional[DynamoDBAPIConfig] = None) -> None:
        """Initialize DynamoDB client."""
        dynamo_config = client.Config(max_pool_connections=100)
        self.client = boto3_session.client(
            service_name="dynamodb",
            config=dynamo_config,
            endpoint_url=config.endpoint_url if config else None,
            region_name=config.region if config else None,
        )

        self.resource = boto3_session.resource(
            service_name="dynamodb",
            config=dynamo_config,
            endpoint_url=config.endpoint_url if config else None,
            region_name=config.region if config else None,
        )
        self.table_cache = {}
        self.table_name = table_name

    def init_db_table(self) -> None:
        """Initialize DynamoDB table."""
        self.create_db_table()
        self.enable_ttl()

    def create_db_table(self) -> dict[str, Any]:
        """Create a new DynamoDB table."""
        table_name = self.table_name

        try:
            existing_tables = self.client.list_tables()["TableNames"]
            if table_name in existing_tables:
                logger.info(
                    f"Table {table_name} already exists, skipping creation.")
                return {}

            logger.info(f"Creating DynamoDB table: {table_name}...")
            response = self.client.create_table(
                AttributeDefinitions=[
                    {
                        "AttributeName": "_pk",
                        "AttributeType": "S",
                    },
                    {
                        "AttributeName": "_sk",
                        "AttributeType": "S",
                    },
                ],
                TableName=table_name,
                KeySchema=[
                    {
                        "AttributeName": "_pk",
                        "KeyType": "HASH",
                    },
                    {
                        "AttributeName": "_sk",
                        "KeyType": "RANGE",
                    },
                ],
                BillingMode="PAY_PER_REQUEST",
                StreamSpecification={
                    "StreamEnabled": True,
                    "StreamViewType": "NEW_AND_OLD_IMAGES",
                },
            )
            self.client.get_waiter("table_exists").wait(TableName=table_name)
            logger.info(f"Table {table_name} created successfully!")
            return response
        except Exception as ex:
            logger.exception(f"Failed to create table: {ex!s}")
            raise

    def enable_ttl(self) -> dict[str, Any]:
        """Enable TTL for the table."""
        try:
            logger.info(f"Checking TTL status for table: {self.table_name}...")

            # First check if TTL is already enabled
            ttl_status = self.client.describe_time_to_live(
                TableName=self.table_name
            )

            current_status = ttl_status.get(
                'TimeToLiveDescription', {}).get('TimeToLiveStatus')

            # If TTL is already ENABLED, return without trying to enable again
            if current_status == 'ENABLED':
                logger.info(f"TTL is already enabled for table: {
                            self.table_name}")
                return ttl_status

            logger.info(f"Enabling TTL for table: {self.table_name}...")
            response = self.client.update_time_to_live(
                TableName=self.table_name,
                TimeToLiveSpecification={
                    "Enabled": True,
                    "AttributeName": "_ttl",
                },
            )

            logger.info(f"TTL enabled for table: {self.table_name}")
            return response
        except Exception as ex:
            logger.exception(f"Failed to enable TTL for table: {ex!s}")
            raise

    def create_db_partition_index(
        self,
        index_name: str,
        pk_name: str,
        sk_name: str,
    ) -> dict[str, Any]:
        """Create a global secondary index and wait for it to be active.

        Args:
            index_name: Name of the index to create
            pk_name: Partition key attribute name
            sk_name: Sort key attribute name
            wait_timeout: Maximum time to wait for index creation (seconds)
            wait_interval: Time between status checks (seconds)

        Returns:
            Dict[str, Any]: AWS response

        Raises:
            WaiterError: If index creation times out
            Exception: If index creation fails

        """
        try:
            response = self.client.update_table(
                AttributeDefinitions=[
                    {
                        "AttributeName": pk_name,
                        "AttributeType": "S",
                    },
                    {
                        "AttributeName": sk_name,
                        "AttributeType": "S",
                    },
                ],
                TableName=self.table_name,
                GlobalSecondaryIndexUpdates=[
                    {
                        "Create": {
                            "IndexName": index_name,
                            "KeySchema": [
                                {
                                    "AttributeName": pk_name,
                                    "KeyType": "HASH",
                                },
                                {
                                    "AttributeName": sk_name,
                                    "KeyType": "RANGE",
                                },
                            ],
                            "Projection": {
                                "ProjectionType": "ALL",
                            },
                        },
                    },
                ],
            )

            logger.info(f"Creating GSI {index_name} on table {
                        self.table_name}...")

            # Wait for index to become active
            self.client.get_waiter("table_exists")
            start_time = time.time()

            # 420 seconds is the maximum time for index creation
            # This is probably enough time for any index to be created
            wait_timeout, wait_interval = 420, 5

            while time.time() - start_time < wait_timeout:
                try:
                    # Check table description
                    table_desc = self.client.describe_table(
                        TableName=self.table_name)
                    indexes = table_desc.get("Table", {}).get(
                        "GlobalSecondaryIndexes", [])

                    # Find our index
                    target_index = next(
                        (idx for idx in indexes if idx["IndexName"]
                         == index_name),
                        None,
                    )

                    if target_index:
                        status = target_index["IndexStatus"]
                        if status == "ACTIVE":
                            logger.info(f"GSI {index_name} is now active")
                            return response
                        if status == "CREATING":
                            logger.debug(
                                f"GSI {index_name} is still being created...")
                        else:
                            msg = f"Unexpected index status: {status}"
                            raise Exception(
                                msg)

                    time.sleep(wait_interval)

                except self.client.exceptions.ResourceNotFoundException:
                    logger.debug("Table description not available yet...")
                    time.sleep(wait_interval)

            raise WaiterError(
                name="table_exists",
                reason=f"GSI {index_name} creation timed out after {
                    wait_timeout} seconds",
                last_response=response,
            )

        except Exception as ex:
            logger.exception(
                f"Failed to create index: {ex!s}\n"
                f"pk:{pk_name}, sk:{sk_name}",
            )
            raise

    def get_table(self, table_name: str):
        """Get cached table resource.

        This method returns a DynamoDB table resource, using a cache to avoid
        recreating the resource for the same table multiple times.

        Args:
            table_name: Name of the DynamoDB table

        Returns:
            boto3.resource.Table: The DynamoDB table resource

        """
        if table_name in self.table_cache:
            return self.table_cache[table_name]
        table = self.resource.Table(table_name)
        self.table_cache[table_name] = table
        return table

    def delete_db_table(self) -> dict[str, Any] | None:
        """Delete the DynamoDB table.

        Attempts to delete the DynamoDB table specified by self.table_name.

        Returns:
            Optional[Dict[str, Any]]: Response from delete_table API call if successful,
                                    None if deletion fails

        Logs:
            Error message if table deletion fails

        """
        try:
            return self.client.delete_table(
                TableName=self.table_name,
            )
        except BaseException as ex:
            logger.exception(f"Failed to delete table: {ex!s}")
            return None

    def get_item(
        self,
        pk: str,
        sk: str | None = None,
        consistent_read: bool = False,
    ) -> dict[str, Any]:
        """Retrieve a single item from DynamoDB by primary key.

        Gets an item from DynamoDB using partition key and optional sort key.
        Uses the table's primary key schema.

        Args:
            pk: Partition key value
            sk: Sort key value (optional)
            consistent_read: Whether to use strongly consistent reads (default False)

        Returns:
            Dict[str, Any]: The item if found, None if not found

        Notes:
            The returned item is in raw DynamoDB format with attributes like
            '_pk' and '_sk' included

        """
        table = self.get_table(self.table_name)
        key = {
            "_pk": pk,
            "_sk": sk,
        }
        response = table.get_item(
            Key=key,
            ConsistentRead=consistent_read,
        )
        return response.get("Item", None)

    def _get_items(self, pk_sk_pairs, consistent_read=False, retry_attempt=0):
        """Helper method to get items in batches with retry logic.

        Args:
            pk_sk_pairs: List of partition key and sort key pairs
            consistent_read: Whether to use strongly consistent reads
            retry_attempt: Number of retry attempts made so far

        Returns:
            List of successfully retrieved items

        """
        # Convert pk/sk pairs into DynamoDB key format
        keys = [{
            "_pk": {"S": pk_sk_pair["_pk"]},
            "_sk": {"S": pk_sk_pair["_sk"]},
        } for pk_sk_pair in pk_sk_pairs if pk_sk_pair]

        if keys:
            response = self.client.batch_get_item(
                RequestItems={
                    self.table_name: {
                        "Keys": keys,
                        "ConsistentRead": consistent_read,
                    },
                },
            )

            items_succeed = response["Responses"][self.table_name]

            # Handle unprocessed keys with exponential backoff retry
            unprocessed_keys = response.get("UnprocessedKeys", {}).get(
                self.table_name, {}).get("Keys", [])
            if unprocessed_keys:
                # Exponential backoff based on retry attempt
                time.sleep(pow(retry_attempt + 1, 2))
                items_to_extend = self._get_items(
                    unprocessed_keys, consistent_read, retry_attempt + 1)
                items_succeed.extend(items_to_extend)
        else:
            # No keys provided, return empty list
            items_succeed = []

        # Deserialize the DynamoDB response format into Python types
        for item in items_succeed:
            for key, value in item.items():
                value = type_deserializer.deserialize(value)
                item[key] = value

        return items_succeed

    def get_items(self, pk_sk_pairs: list[tuple[str, str]], consistent_read: bool = False):
        """Get multiple items from DynamoDB in parallel batches.

        Args:
            pk_sk_pairs: List of partition key and sort key pairs to retrieve
            consistent_read: Whether to use strongly consistent reads

        Returns:
            List of items in the same order as the input pk_sk_pairs

        """
        # Split into chunks of 100 (DynamoDB batch limit)
        chunks = list(divide_chunks(pk_sk_pairs, 100))
        items_succeed = []
        futures = []

        # Use thread pool to fetch chunks in parallel
        with ThreadPoolExecutor(max_workers=max(1, len(chunks))) as worker:
            for chunk in chunks:
                futures.append(worker.submit(
                    self._get_items, chunk, consistent_read))
        for future in futures:
            items_succeed.extend(future.result())

        # Sort results to match input order
        items_by_key = {(item.get("_pk", ""), item.get(
            "_sk", "")): item for item in items_succeed}
        sorted_items = []
        for pk_sk in pk_sk_pairs:
            if pk_sk:
                item = items_by_key.get((pk_sk["_pk"], pk_sk["_sk"]), None)
                sorted_items.append(item)
            else:
                sorted_items.append(None)
        return sorted_items

    def put_item(
        self,
        item: dict[str, Any],
        can_overwrite: bool = True,
    ) -> dict[str, Any]:
        table = self.get_table(self.table_name)
        # Consider index types before inserting data into DB
        if can_overwrite:
            return table.put_item(
                Item=item,
            )
        # Add condition to prevent duplicate writes when key already exists
        try:
            return table.put_item(
                Item=item,
                ConditionExpression="attribute_not_exists(#pk) AND attribute_not_exists(#sk)",
                ExpressionAttributeNames={
                    "#pk": "_pk",
                    "#sk": "_sk",
                },
            )
        except self.resource.meta.client.exceptions.ConditionalCheckFailedException as e:
            pk = item["_pk"]
            sk = item["_sk"]
            raise DynamoDBError(
                message=f'Item already exist _pk:"{pk}" _sk:"{sk}"  Check "pk_field" and "sk_field" & "post_sk_fields" combination.') from e

    @classmethod
    def get_update_expression_attrs_pair(cls, item: dict[str, Any]) -> tuple[str, dict[str, Any], dict[str, Any]]:
        """Generates DynamoDB update expression and attribute maps from an item dictionary.

        Args:
            item: Dictionary containing the fields and values to update.

        Returns:
            A tuple containing:
                - Update expression string starting with "set"
                - Dictionary mapping attribute name placeholders to actual names
                - Dictionary mapping attribute value placeholders to actual values

        Example:
            For item {"name": "John", "age": 30}, returns:
            ("set #key0=:val0, #key1=:val1",
             {"#key0": "name", "#key1": "age"},
             {":val0": "John", ":val1": 30})
        """
        expression = "set"
        attr_names = {}
        attr_values = {}
        for idx, (key, value) in enumerate(item.items()):
            attr_key = f"#key{idx}"
            attr_value = f":val{idx}"
            expression += f" {attr_key}={attr_value}"

            attr_names[f"{attr_key}"] = key
            attr_values[f"{attr_value}"] = value
            if idx != len(item) - 1:
                expression += ","
        return expression, attr_names, attr_values

    def update_item(self, pk: str, sk: str, item: dict[str, Any]) -> dict[str, Any]:
        """Update an item.
        If the item to update does not exist in the DB, an error will occur.
        :param pk:
        :param sk:
        :param item:
        :return:
        """
        expression, attr_names, attr_values = self.get_update_expression_attrs_pair(
            item)

        attr_names["#pk"] = "_pk"
        attr_names["#sk"] = "_sk"

        try:
            response = self.get_table(self.table_name).update_item(
                Key={"_pk": pk, "_sk": sk},
                UpdateExpression=expression,
                ExpressionAttributeValues=attr_values,
                ExpressionAttributeNames=attr_names,
                ReturnValues="ALL_NEW",
                ConditionExpression="attribute_exists(#pk) AND attribute_exists(#sk)",
            )
        except Exception as e:
            msg = "Item to update not exist"
            raise DynamoDBError(msg) from e

        return response

    def batch_put(
        self,
        items: list[dict[str, Any]],
        can_overwrite: bool = False,
    ) -> bool:
        table = self.get_table(self.table_name)
        overwrite_by_keys = None if can_overwrite else ["_pk", "_sk"]

        with table.batch_writer(overwrite_by_pkeys=overwrite_by_keys) as batch:
            for item in items:
                batch.put_item(
                    Item=item,
                )

        return True

    def delete_item(
        self,
        pk: str,
        sk: str,
    ) -> dict[str, Any]:
        """Delete single item."""
        table = self.get_table(table_name=self.table_name)

        return table.delete_item(
            Key={"_pk": pk, "_sk": sk},
            ReturnValues="ALL_OLD",
        )

    def batch_delete(self, pk_sk_pairs: list[tuple[str, str]]) -> bool:
        """Delete multiple items from DynamoDB in a batch operation.

        This method efficiently deletes multiple items in parallel using DynamoDB's batch writer.
        The batch writer automatically handles throttling, retries, and batching of requests.

        Args:
            pk_sk_pairs: List of dictionaries containing partition key and sort key pairs.
                Each dictionary should have the format:
                {
                    '_pk': 'partition_key_value',
                    '_sk': 'sort_key_value'
                }

        Returns:
            bool: True if all deletions were successful

        Note:
            DynamoDB has a limit of 25 items per batch write operation.
            The batch_writer handles splitting larger batches automatically.

        """
        table = self.get_table(table_name=self.table_name)

        with table.batch_writer() as batch:
            for pk_sk_pair in pk_sk_pairs:
                _pk, _sk = pk_sk_pair

                batch.delete_item(Key={
                    "_pk": _pk,
                    "_sk": _sk,
                })

        return True

    def query_items(
        self,
        partition_key_name: str,
        partition_key_value: str,
        sort_condition: str | None = None,
        sort_key_name: str | None = None,
        sort_key_value: Any | None = None,
        sort_key_second_value: Any | None = None,
        filters: list[dict[str, Any]] | None = None,
        start_key: dict[str, Any] | None = None,
        reverse: bool = False,
        limit: int = 100,
        consistent_read: bool = False,
        index_name: str | None = None,
        recursive_filters: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Query items with complex filtering."""
        table = self.get_table(table_name=self.table_name)

        # Build key condition expression
        key_expression = Key(name=partition_key_name).eq(
            value=partition_key_value)

        if sort_condition and sort_key_name and sort_key_value is not None:
            if sort_condition == "eq":
                key_expression &= Key(name=sort_key_name).eq(
                    value=sort_key_value)
            elif sort_condition == "lte":
                key_expression &= Key(name=sort_key_name).lte(
                    value=sort_key_value)
            elif sort_condition == "lt":
                key_expression &= Key(name=sort_key_name).lt(
                    value=sort_key_value)
            elif sort_condition == "gte":
                key_expression &= Key(name=sort_key_name).gte(
                    value=sort_key_value)
            elif sort_condition == "gt":
                key_expression &= Key(name=sort_key_name).gt(
                    value=sort_key_value)
            elif sort_condition == "btw":
                key_expression &= Key(name=sort_key_name).between(
                    low_value=sort_key_value,
                    high_value=sort_key_second_value,
                )
            elif sort_condition == "stw":
                key_expression &= Key(
                    name=sort_key_name).begins_with(value=sort_key_value)

        # Build filter expression
        filter_expression = None
        if filters:
            for ft in filters:
                attr_expr = self._get_filter_expression(filter_dict=ft)
                if filter_expression:
                    filter_expression &= attr_expr
                else:
                    filter_expression = attr_expr
        elif recursive_filters:
            filter_expression = self._get_recursive_filter_expression(
                recursive_filters=recursive_filters)

        query_args = {
            "KeyConditionExpression": key_expression,
            "Limit": limit,
            "ConsistentRead": consistent_read,
            "ScanIndexForward": not reverse,
        }

        if index_name:
            query_args["IndexName"] = index_name
            query_args["ConsistentRead"] = False

        if filter_expression:
            query_args["FilterExpression"] = filter_expression

        if start_key:
            query_args["ExclusiveStartKey"] = start_key

        query_args = decode_dict(dict_obj=query_args)

        return table.query(**query_args)

    def _get_filter_expression(self, filter_dict: dict[str, Any]) -> Any:
        """Convert filter dict to DynamoDB filter expression."""
        field = filter_dict["field"]
        value = filter_dict.get("value")
        condition = filter_dict["condition"]
        second_value = filter_dict.get("second_value")

        attr = Attr(field)

        if condition == "eq":
            return attr.eq(value)
        if condition == "neq":
            return attr.ne(value)
        if condition == "lte":
            return attr.lte(value)
        if condition == "lt":
            return attr.lt(value)
        if condition == "gte":
            return attr.gte(value)
        if condition == "gt":
            return attr.gt(value)
        if condition == "btw":
            return attr.between(value, second_value)
        if condition == "not_btw":
            return ~attr.between(value, second_value)
        if condition == "stw":
            return attr.begins_with(value)
        if condition == "not_stw":
            return ~attr.begins_with(value)
        if condition == "is_in":
            return attr.is_in(value)
        if condition == "is_not_in":
            return ~attr.is_in(value)
        if condition == "contains":
            return attr.contains(value)
        if condition == "not_contains":
            return ~attr.contains(value)
        if condition == "exist":
            return attr.exists()
        if condition == "not_exist":
            return attr.not_exists()
        msg = f"Invalid filter condition: {condition}"
        raise ValueError(msg)

    def _get_recursive_filter_expression(self, recursive_filters: dict[str, Any]) -> Any:
        """Convert recursive filter dict to DynamoDB filter expression."""
        if "field" in recursive_filters:
            return self._get_filter_expression(recursive_filters)

        if "left" in recursive_filters and "right" in recursive_filters and "operation" in recursive_filters:
            left = self._get_recursive_filter_expression(
                recursive_filters["left"])
            right = self._get_recursive_filter_expression(
                recursive_filters["right"])

            if recursive_filters["operation"] == "and":
                return left & right
            if recursive_filters["operation"] == "or":
                return left | right
            msg = (
                f"Invalid operation: {
                    recursive_filters['operation']}"
            )
            raise ValueError(msg)

        msg = "Invalid recursive filter format"
        raise ValueError(msg)

    def scan_table(
        self,
        filters: list[dict[Literal["field",
                                   "condition", "value"], Any]] | None = None,
        recursive_filters: dict[str, Any] | None = None,
        start_key: dict[str, Any] | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        """Scan table with optional filtering.

        Args:
            table_name: Name of the DynamoDB table to scan
            filters: List of filter conditions to apply. Each filter is a dict with:
                - field: Name of the attribute to filter on
                - condition: Filter condition (eq, lt, gt etc)
                - value: Value to compare against
            recursive_filters: Nested filter conditions with AND/OR operations
            start_key: Key to start scan from for pagination
            limit: Maximum number of items to return

        Returns:
            Dict containing scan results with Items and LastEvaluatedKey

        """
        # Get table reference
        table = self.get_table(table_name=self.table_name)

        # Build scan parameters
        scan_kwargs = {}
        if limit:
            scan_kwargs["Limit"] = limit
        if start_key:
            scan_kwargs["ExclusiveStartKey"] = start_key

        # Build filter expression from conditions
        filter_expression = None
        if filters:
            # Combine multiple filter conditions with AND
            for ft in filters:
                attr_to_add = self.get_attr(ft)
                if filter_expression:
                    filter_expression &= attr_to_add
                else:
                    filter_expression = attr_to_add
        elif recursive_filters:
            # Handle nested filter conditions with AND/OR operations
            filter_expression = self.get_recursive_filters_expression(
                recursive_filters)

        # Add filter expression to scan if present
        if filter_expression:
            scan_kwargs["FilterExpression"] = filter_expression

        # Execute scan operation
        return table.scan(**scan_kwargs)


class AsyncDynamoDB:
    """Asynchronous DynamoDB client wrapper."""

    def __init__(
        self,
        table_name: str,
        config: Optional[DynamoDBAPIConfig] = None,
    ) -> None:
        self.config = config or DynamoDBAPIConfig()
        self.table_name = table_name
        self._session = aioboto3.Session()

    async def init_db_table(self) -> None:
        """Initialize DynamoDB table asynchronously."""
        async with self._session.resource("dynamodb") as dynamodb:
            self.table = await dynamodb.Table(self.table_name)

    async def get_item(
        self,
        pk: str,
        sk: str,
        consistent_read: bool = False,
    ) -> Optional[Dict[str, Any]]:
        """Get single item by primary key asynchronously."""
        async with self._session.resource("dynamodb") as dynamodb:
            table = await dynamodb.Table(self.table_name)
            response = await table.get_item(
                Key={"_pk": pk, "_sk": sk},
                ConsistentRead=consistent_read,
            )
            return response.get("Item")

    async def get_items(
        self,
        pk_sk_pairs: List[Tuple[str, str]],
        consistent_read: bool = False,
    ) -> List[Optional[Dict[str, Any]]]:
        """Get multiple items by primary keys asynchronously."""
        async with self._session.resource("dynamodb") as dynamodb:
            table = await dynamodb.Table(self.table_name)

            # DynamoDB batch_get_item limit is 100 items
            batch_size = 100
            all_items = []

            for i in range(0, len(pk_sk_pairs), batch_size):
                batch = pk_sk_pairs[i:i + batch_size]
                request_items = {
                    self.table_name: {
                        "Keys": [{"_pk": pk, "_sk": sk} for pk, sk in batch],
                        "ConsistentRead": consistent_read,
                    }
                }

                response = await table.meta.client.batch_get_item(
                    RequestItems=request_items
                )

                items = response.get("Responses", {}).get(self.table_name, [])
                all_items.extend(items)

            return all_items

    async def put_item(
        self,
        item: Dict[str, Any],
        can_overwrite: bool = True,
    ) -> Dict[str, Any]:
        """Put single item asynchronously."""
        async with self._session.resource("dynamodb") as dynamodb:
            table = await dynamodb.Table(self.table_name)

            if not can_overwrite:
                condition = "attribute_not_exists(_pk) AND attribute_not_exists(_sk)"
            else:
                condition = None

            try:
                response = await table.put_item(
                    Item=item,
                    ConditionExpression=condition,
                    ReturnValues="ALL_OLD",
                )
                return response
            except Exception as e:
                if "ConditionalCheckFailedException" in str(e):
                    raise DynamoDBError("Item already exists") from e
                raise

    async def batch_put(
        self,
        items: List[Dict[str, Any]],
        can_overwrite: bool = True,
    ) -> bool:
        """Put multiple items asynchronously."""
        async with self._session.resource("dynamodb") as dynamodb:
            table = await dynamodb.Table(self.table_name)

            # DynamoDB batch_write_item limit is 25 items
            batch_size = 25

            for i in range(0, len(items), batch_size):
                batch = items[i:i + batch_size]
                request_items = {
                    self.table_name: [
                        {"PutRequest": {"Item": item}} for item in batch
                    ]
                }

                try:
                    response = await table.meta.client.batch_write_item(
                        RequestItems=request_items
                    )

                    unprocessed = response.get("UnprocessedItems", {}).get(
                        self.table_name, []
                    )
                    if unprocessed:
                        return False

                except Exception:
                    return False

            return True

    async def update_item(
        self,
        pk: str,
        sk: str,
        item: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Update single item asynchronously."""
        async with self._session.resource("dynamodb") as dynamodb:
            table = await dynamodb.Table(self.table_name)

            update_expression = "SET " + \
                ", ".join(f"#{k} = :{k}" for k in item.keys())
            expression_attribute_names = {f"#{k}": k for k in item.keys()}
            expression_attribute_values = {f":{k}": v for k, v in item.items()}

            try:
                response = await table.update_item(
                    Key={"_pk": pk, "_sk": sk},
                    UpdateExpression=update_expression,
                    ExpressionAttributeNames=expression_attribute_names,
                    ExpressionAttributeValues=expression_attribute_values,
                    ReturnValues="ALL_NEW",
                )
                return response
            except Exception as e:
                if "ConditionalCheckFailedException" in str(e):
                    raise DynamoDBError("Item does not exist") from e
                raise

    async def delete_item(
        self,
        pk: str,
        sk: str,
    ) -> Dict[str, Any]:
        """Delete single item asynchronously."""
        async with self._session.resource("dynamodb") as dynamodb:
            table = await dynamodb.Table(self.table_name)
            response = await table.delete_item(
                Key={"_pk": pk, "_sk": sk},
                ReturnValues="ALL_OLD",
            )
            return response

    async def batch_delete(
        self,
        pk_sk_pairs: List[Tuple[str, str]],
    ) -> None:
        """Delete multiple items asynchronously."""
        async with self._session.resource("dynamodb") as dynamodb:
            table = await dynamodb.Table(self.table_name)

            # DynamoDB batch_write_item limit is 25 items
            batch_size = 25

            for i in range(0, len(pk_sk_pairs), batch_size):
                batch = pk_sk_pairs[i:i + batch_size]
                request_items = {
                    self.table_name: [
                        {
                            "DeleteRequest": {
                                "Key": {"_pk": pk, "_sk": sk}
                            }
                        }
                        for pk, sk in batch
                    ]
                }

                await table.meta.client.batch_write_item(RequestItems=request_items)

    async def query_items(
        self,
        partition_key_name: str,
        partition_key_value: str,
        sort_condition: Optional[str] = None,
        sort_key_name: Optional[str] = None,
        sort_key_value: Optional[str] = None,
        sort_key_second_value: Optional[str] = None,
        filters: Optional[List[Dict[str, Any]]] = None,
        start_key: Optional[Dict[str, Any]] = None,
        reverse: bool = False,
        limit: int = 1000,
        consistent_read: bool = False,
        index_name: Optional[str] = None,
        recursive_filters: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Query items asynchronously."""
        async with self._session.resource("dynamodb") as dynamodb:
            table = await dynamodb.Table(self.table_name)

            key_condition = f"#{partition_key_name} = :{partition_key_name}"
            expression_attribute_names = {
                f"#{partition_key_name}": partition_key_name}
            expression_attribute_values = {
                f":{partition_key_name}": partition_key_value}

            if sort_condition and sort_key_name and sort_key_value:
                key_condition += f" AND #{sort_key_name} {
                    sort_condition} :{sort_key_name}"
                expression_attribute_names[f"#{sort_key_name}"] = sort_key_name
                expression_attribute_values[f":{
                    sort_key_name}"] = sort_key_value

                if sort_key_second_value:
                    expression_attribute_values[f":{
                        sort_key_name}_2"] = sort_key_second_value

            query_kwargs = {
                "KeyConditionExpression": key_condition,
                "ExpressionAttributeNames": expression_attribute_names,
                "ExpressionAttributeValues": expression_attribute_values,
                "ScanIndexForward": not reverse,
                "Limit": limit,
                "ConsistentRead": consistent_read,
            }

            if index_name:
                query_kwargs["IndexName"] = index_name

            if start_key:
                query_kwargs["ExclusiveStartKey"] = start_key

            if filters:
                filter_expression = " AND ".join(
                    f"#{f['field']} {f['condition']} :{f['field']}"
                    for f in filters
                )
                for f in filters:
                    expression_attribute_names[f"#{f['field']}"] = f["field"]
                    expression_attribute_values[f":{f['field']}"] = f["value"]
                query_kwargs["FilterExpression"] = filter_expression

            response = await table.query(**query_kwargs)
            return response

    async def scan_table(
        self,
        filters: Optional[List[Dict[str, Any]]] = None,
        recursive_filters: Optional[Dict[str, Any]] = None,
        start_key: Optional[Dict[str, Any]] = None,
        limit: int = 1000,
    ) -> Tuple[List[Dict[str, Any]], Optional[str]]:
        """Scan table asynchronously."""
        async with self._session.resource("dynamodb") as dynamodb:
            table = await dynamodb.Table(self.table_name)

            scan_kwargs = {
                "Limit": limit,
            }

            if start_key:
                scan_kwargs["ExclusiveStartKey"] = start_key

            if filters:
                filter_expression = " AND ".join(
                    f"#{f['field']} {f['condition']} :{f['field']}"
                    for f in filters
                )
                expression_attribute_names = {
                    f"#{f['field']}": f["field"] for f in filters
                }
                expression_attribute_values = {
                    f":{f['field']}": f["value"] for f in filters
                }
                scan_kwargs.update({
                    "FilterExpression": filter_expression,
                    "ExpressionAttributeNames": expression_attribute_names,
                    "ExpressionAttributeValues": expression_attribute_values,
                })

            response = await table.scan(**scan_kwargs)
            items = response.get("Items", [])
            last_key = response.get("LastEvaluatedKey")

            return items, last_key if last_key else None
