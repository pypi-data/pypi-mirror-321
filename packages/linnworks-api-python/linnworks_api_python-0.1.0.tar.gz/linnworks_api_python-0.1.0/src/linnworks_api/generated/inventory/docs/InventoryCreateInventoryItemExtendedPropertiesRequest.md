# InventoryCreateInventoryItemExtendedPropertiesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory_item_extended_properties** | [**List[StockItemExtendedPropertyUpsertItem]**](StockItemExtendedPropertyUpsertItem.md) | list of stockitem Extended Properties | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_create_inventory_item_extended_properties_request import InventoryCreateInventoryItemExtendedPropertiesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryCreateInventoryItemExtendedPropertiesRequest from a JSON string
inventory_create_inventory_item_extended_properties_request_instance = InventoryCreateInventoryItemExtendedPropertiesRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryCreateInventoryItemExtendedPropertiesRequest.to_json())

# convert the object into a dict
inventory_create_inventory_item_extended_properties_request_dict = inventory_create_inventory_item_extended_properties_request_instance.to_dict()
# create an instance of InventoryCreateInventoryItemExtendedPropertiesRequest from a dict
inventory_create_inventory_item_extended_properties_request_from_dict = InventoryCreateInventoryItemExtendedPropertiesRequest.from_dict(inventory_create_inventory_item_extended_properties_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


