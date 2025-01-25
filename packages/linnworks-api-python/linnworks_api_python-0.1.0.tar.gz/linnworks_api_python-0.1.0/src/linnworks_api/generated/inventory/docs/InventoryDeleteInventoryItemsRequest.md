# InventoryDeleteInventoryItemsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**DeleteInventoryItemsRequest**](DeleteInventoryItemsRequest.md) |  | [optional] 
**inventory_item_ids** | **List[str]** | List of stock item IDs that needs to be deleted | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_delete_inventory_items_request import InventoryDeleteInventoryItemsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryDeleteInventoryItemsRequest from a JSON string
inventory_delete_inventory_items_request_instance = InventoryDeleteInventoryItemsRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryDeleteInventoryItemsRequest.to_json())

# convert the object into a dict
inventory_delete_inventory_items_request_dict = inventory_delete_inventory_items_request_instance.to_dict()
# create an instance of InventoryDeleteInventoryItemsRequest from a dict
inventory_delete_inventory_items_request_from_dict = InventoryDeleteInventoryItemsRequest.from_dict(inventory_delete_inventory_items_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


