# DeleteInventoryItemsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory_item_ids** | **List[str]** |  | [optional] 
**selected_regions** | [**List[TupleInt32Int32]**](TupleInt32Int32.md) |  | [optional] 
**token** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.delete_inventory_items_request import DeleteInventoryItemsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteInventoryItemsRequest from a JSON string
delete_inventory_items_request_instance = DeleteInventoryItemsRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteInventoryItemsRequest.to_json())

# convert the object into a dict
delete_inventory_items_request_dict = delete_inventory_items_request_instance.to_dict()
# create an instance of DeleteInventoryItemsRequest from a dict
delete_inventory_items_request_from_dict = DeleteInventoryItemsRequest.from_dict(delete_inventory_items_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


