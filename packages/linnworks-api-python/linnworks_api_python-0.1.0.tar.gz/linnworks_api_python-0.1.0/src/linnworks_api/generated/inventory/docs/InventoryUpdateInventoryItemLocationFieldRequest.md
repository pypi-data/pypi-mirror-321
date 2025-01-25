# InventoryUpdateInventoryItemLocationFieldRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory_item_id** | **str** | Stock Item Id | [optional] 
**field_name** | **str** | Name of field updated | [optional] 
**field_value** | **str** | Input value | [optional] 
**location_id** | **str** | Location Id | [optional] 
**change_source** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_update_inventory_item_location_field_request import InventoryUpdateInventoryItemLocationFieldRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryUpdateInventoryItemLocationFieldRequest from a JSON string
inventory_update_inventory_item_location_field_request_instance = InventoryUpdateInventoryItemLocationFieldRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryUpdateInventoryItemLocationFieldRequest.to_json())

# convert the object into a dict
inventory_update_inventory_item_location_field_request_dict = inventory_update_inventory_item_location_field_request_instance.to_dict()
# create an instance of InventoryUpdateInventoryItemLocationFieldRequest from a dict
inventory_update_inventory_item_location_field_request_from_dict = InventoryUpdateInventoryItemLocationFieldRequest.from_dict(inventory_update_inventory_item_location_field_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


