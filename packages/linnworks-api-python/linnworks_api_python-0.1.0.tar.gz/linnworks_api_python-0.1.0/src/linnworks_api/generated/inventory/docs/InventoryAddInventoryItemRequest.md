# InventoryAddInventoryItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory_item** | [**StockItem**](StockItem.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_add_inventory_item_request import InventoryAddInventoryItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryAddInventoryItemRequest from a JSON string
inventory_add_inventory_item_request_instance = InventoryAddInventoryItemRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryAddInventoryItemRequest.to_json())

# convert the object into a dict
inventory_add_inventory_item_request_dict = inventory_add_inventory_item_request_instance.to_dict()
# create an instance of InventoryAddInventoryItemRequest from a dict
inventory_add_inventory_item_request_from_dict = InventoryAddInventoryItemRequest.from_dict(inventory_add_inventory_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


