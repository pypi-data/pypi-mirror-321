# DeleteInventoryItemBulkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory_item_ids** | **List[str]** | List of items by ids to delete. If not provided, you must provide ItemNumbers | [optional] 
**item_numbers** | **List[str]** | List of items by item number to delete. If InventoryItemIds is provided, ItemNumbers will be ignored | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.delete_inventory_item_bulk_request import DeleteInventoryItemBulkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteInventoryItemBulkRequest from a JSON string
delete_inventory_item_bulk_request_instance = DeleteInventoryItemBulkRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteInventoryItemBulkRequest.to_json())

# convert the object into a dict
delete_inventory_item_bulk_request_dict = delete_inventory_item_bulk_request_instance.to_dict()
# create an instance of DeleteInventoryItemBulkRequest from a dict
delete_inventory_item_bulk_request_from_dict = DeleteInventoryItemBulkRequest.from_dict(delete_inventory_item_bulk_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


