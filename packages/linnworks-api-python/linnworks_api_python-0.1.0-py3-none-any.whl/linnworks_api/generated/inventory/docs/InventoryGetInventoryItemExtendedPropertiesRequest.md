# InventoryGetInventoryItemExtendedPropertiesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory_item_id** | **str** | stockitem id | [optional] 
**property_params** | [**GetExtendedPropertyFilter**](GetExtendedPropertyFilter.md) |  | [optional] 
**item_number** | **str** | This can be used as an alternative to stockitemid | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_get_inventory_item_extended_properties_request import InventoryGetInventoryItemExtendedPropertiesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryGetInventoryItemExtendedPropertiesRequest from a JSON string
inventory_get_inventory_item_extended_properties_request_instance = InventoryGetInventoryItemExtendedPropertiesRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryGetInventoryItemExtendedPropertiesRequest.to_json())

# convert the object into a dict
inventory_get_inventory_item_extended_properties_request_dict = inventory_get_inventory_item_extended_properties_request_instance.to_dict()
# create an instance of InventoryGetInventoryItemExtendedPropertiesRequest from a dict
inventory_get_inventory_item_extended_properties_request_from_dict = InventoryGetInventoryItemExtendedPropertiesRequest.from_dict(inventory_get_inventory_item_extended_properties_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


