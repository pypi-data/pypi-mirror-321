# BatchedAPIResponseDeleteInventoryItemBulkResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[APIResultResponseDeleteInventoryItemBulkResponse]**](APIResultResponseDeleteInventoryItemBulkResponse.md) |  | [optional] 
**total_results** | **int** |  | [optional] [readonly] 
**result_status** | **str** |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.inventory.models.batched_api_response_delete_inventory_item_bulk_response import BatchedAPIResponseDeleteInventoryItemBulkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BatchedAPIResponseDeleteInventoryItemBulkResponse from a JSON string
batched_api_response_delete_inventory_item_bulk_response_instance = BatchedAPIResponseDeleteInventoryItemBulkResponse.from_json(json)
# print the JSON string representation of the object
print(BatchedAPIResponseDeleteInventoryItemBulkResponse.to_json())

# convert the object into a dict
batched_api_response_delete_inventory_item_bulk_response_dict = batched_api_response_delete_inventory_item_bulk_response_instance.to_dict()
# create an instance of BatchedAPIResponseDeleteInventoryItemBulkResponse from a dict
batched_api_response_delete_inventory_item_bulk_response_from_dict = BatchedAPIResponseDeleteInventoryItemBulkResponse.from_dict(batched_api_response_delete_inventory_item_bulk_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


