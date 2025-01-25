# InventoryAddInventoryItemBulkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**AddInventoryItemRequest**](AddInventoryItemRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_add_inventory_item_bulk_request import InventoryAddInventoryItemBulkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryAddInventoryItemBulkRequest from a JSON string
inventory_add_inventory_item_bulk_request_instance = InventoryAddInventoryItemBulkRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryAddInventoryItemBulkRequest.to_json())

# convert the object into a dict
inventory_add_inventory_item_bulk_request_dict = inventory_add_inventory_item_bulk_request_instance.to_dict()
# create an instance of InventoryAddInventoryItemBulkRequest from a dict
inventory_add_inventory_item_bulk_request_from_dict = InventoryAddInventoryItemBulkRequest.from_dict(inventory_add_inventory_item_bulk_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


