# APIResultResponseDeleteInventoryItemBulkResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**DeleteInventoryItemBulkResponse**](DeleteInventoryItemBulkResponse.md) |  | [optional] 
**result_status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.api_result_response_delete_inventory_item_bulk_response import APIResultResponseDeleteInventoryItemBulkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of APIResultResponseDeleteInventoryItemBulkResponse from a JSON string
api_result_response_delete_inventory_item_bulk_response_instance = APIResultResponseDeleteInventoryItemBulkResponse.from_json(json)
# print the JSON string representation of the object
print(APIResultResponseDeleteInventoryItemBulkResponse.to_json())

# convert the object into a dict
api_result_response_delete_inventory_item_bulk_response_dict = api_result_response_delete_inventory_item_bulk_response_instance.to_dict()
# create an instance of APIResultResponseDeleteInventoryItemBulkResponse from a dict
api_result_response_delete_inventory_item_bulk_response_from_dict = APIResultResponseDeleteInventoryItemBulkResponse.from_dict(api_result_response_delete_inventory_item_bulk_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


