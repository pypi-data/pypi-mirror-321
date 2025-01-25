# InventoryUpdateInventoryItemCompositionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory_item_compositions** | [**List[StockItemComposition]**](StockItemComposition.md) | stockItem compositions | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_update_inventory_item_compositions_request import InventoryUpdateInventoryItemCompositionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryUpdateInventoryItemCompositionsRequest from a JSON string
inventory_update_inventory_item_compositions_request_instance = InventoryUpdateInventoryItemCompositionsRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryUpdateInventoryItemCompositionsRequest.to_json())

# convert the object into a dict
inventory_update_inventory_item_compositions_request_dict = inventory_update_inventory_item_compositions_request_instance.to_dict()
# create an instance of InventoryUpdateInventoryItemCompositionsRequest from a dict
inventory_update_inventory_item_compositions_request_from_dict = InventoryUpdateInventoryItemCompositionsRequest.from_dict(inventory_update_inventory_item_compositions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


