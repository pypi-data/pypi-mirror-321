# InventoryDeleteInventoryItemExtendedPropertiesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory_item_id** | **str** | Id of StockItem | [optional] 
**inventory_item_extended_property_ids** | **List[str]** | list of stockitem Extended Properties | [optional] 
**item_number** | **str** | The stock item SKU, only used if inventoryItemId is not supplied | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_delete_inventory_item_extended_properties_request import InventoryDeleteInventoryItemExtendedPropertiesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryDeleteInventoryItemExtendedPropertiesRequest from a JSON string
inventory_delete_inventory_item_extended_properties_request_instance = InventoryDeleteInventoryItemExtendedPropertiesRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryDeleteInventoryItemExtendedPropertiesRequest.to_json())

# convert the object into a dict
inventory_delete_inventory_item_extended_properties_request_dict = inventory_delete_inventory_item_extended_properties_request_instance.to_dict()
# create an instance of InventoryDeleteInventoryItemExtendedPropertiesRequest from a dict
inventory_delete_inventory_item_extended_properties_request_from_dict = InventoryDeleteInventoryItemExtendedPropertiesRequest.from_dict(inventory_delete_inventory_item_extended_properties_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


