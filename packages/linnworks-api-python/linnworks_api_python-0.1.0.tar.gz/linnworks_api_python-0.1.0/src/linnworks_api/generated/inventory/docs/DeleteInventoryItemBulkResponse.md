# DeleteInventoryItemBulkResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_number** | **str** | The ItemNumber (SKU) for the stock item. Only provided if passed in the request | [optional] 
**inventory_item_id** | **str** | The Id for the stock item. Always provided unless not found | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.delete_inventory_item_bulk_response import DeleteInventoryItemBulkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteInventoryItemBulkResponse from a JSON string
delete_inventory_item_bulk_response_instance = DeleteInventoryItemBulkResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteInventoryItemBulkResponse.to_json())

# convert the object into a dict
delete_inventory_item_bulk_response_dict = delete_inventory_item_bulk_response_instance.to_dict()
# create an instance of DeleteInventoryItemBulkResponse from a dict
delete_inventory_item_bulk_response_from_dict = DeleteInventoryItemBulkResponse.from_dict(delete_inventory_item_bulk_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


