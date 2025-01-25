# InventoryUpdateInventoryItemFieldRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory_item_id** | **str** |  | [optional] 
**field_name** | **str** |  | [optional] 
**field_value** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_update_inventory_item_field_request import InventoryUpdateInventoryItemFieldRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryUpdateInventoryItemFieldRequest from a JSON string
inventory_update_inventory_item_field_request_instance = InventoryUpdateInventoryItemFieldRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryUpdateInventoryItemFieldRequest.to_json())

# convert the object into a dict
inventory_update_inventory_item_field_request_dict = inventory_update_inventory_item_field_request_instance.to_dict()
# create an instance of InventoryUpdateInventoryItemFieldRequest from a dict
inventory_update_inventory_item_field_request_from_dict = InventoryUpdateInventoryItemFieldRequest.from_dict(inventory_update_inventory_item_field_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


