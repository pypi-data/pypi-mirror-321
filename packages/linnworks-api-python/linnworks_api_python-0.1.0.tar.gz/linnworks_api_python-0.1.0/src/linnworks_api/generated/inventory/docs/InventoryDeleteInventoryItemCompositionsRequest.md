# InventoryDeleteInventoryItemCompositionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_item_id** | **str** | Id of StockItem | [optional] 
**inventory_item_composition_ids** | **List[str]** | stockItem composition ids | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_delete_inventory_item_compositions_request import InventoryDeleteInventoryItemCompositionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryDeleteInventoryItemCompositionsRequest from a JSON string
inventory_delete_inventory_item_compositions_request_instance = InventoryDeleteInventoryItemCompositionsRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryDeleteInventoryItemCompositionsRequest.to_json())

# convert the object into a dict
inventory_delete_inventory_item_compositions_request_dict = inventory_delete_inventory_item_compositions_request_instance.to_dict()
# create an instance of InventoryDeleteInventoryItemCompositionsRequest from a dict
inventory_delete_inventory_item_compositions_request_from_dict = InventoryDeleteInventoryItemCompositionsRequest.from_dict(inventory_delete_inventory_item_compositions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


