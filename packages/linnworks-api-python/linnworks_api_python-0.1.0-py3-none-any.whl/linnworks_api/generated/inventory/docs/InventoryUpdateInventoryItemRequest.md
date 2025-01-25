# InventoryUpdateInventoryItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory_item** | [**UpdateInventoryItemRequest**](UpdateInventoryItemRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_update_inventory_item_request import InventoryUpdateInventoryItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryUpdateInventoryItemRequest from a JSON string
inventory_update_inventory_item_request_instance = InventoryUpdateInventoryItemRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryUpdateInventoryItemRequest.to_json())

# convert the object into a dict
inventory_update_inventory_item_request_dict = inventory_update_inventory_item_request_instance.to_dict()
# create an instance of InventoryUpdateInventoryItemRequest from a dict
inventory_update_inventory_item_request_from_dict = InventoryUpdateInventoryItemRequest.from_dict(inventory_update_inventory_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


