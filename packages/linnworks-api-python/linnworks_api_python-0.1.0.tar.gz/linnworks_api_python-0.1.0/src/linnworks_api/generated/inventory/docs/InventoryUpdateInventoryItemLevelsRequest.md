# InventoryUpdateInventoryItemLevelsRequest


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
from linnworks_api.generated.inventory.models.inventory_update_inventory_item_levels_request import InventoryUpdateInventoryItemLevelsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryUpdateInventoryItemLevelsRequest from a JSON string
inventory_update_inventory_item_levels_request_instance = InventoryUpdateInventoryItemLevelsRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryUpdateInventoryItemLevelsRequest.to_json())

# convert the object into a dict
inventory_update_inventory_item_levels_request_dict = inventory_update_inventory_item_levels_request_instance.to_dict()
# create an instance of InventoryUpdateInventoryItemLevelsRequest from a dict
inventory_update_inventory_item_levels_request_from_dict = InventoryUpdateInventoryItemLevelsRequest.from_dict(inventory_update_inventory_item_levels_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


