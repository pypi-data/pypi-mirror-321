# InventoryAddItemLocationsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_locations** | [**List[StockItemLocation]**](StockItemLocation.md) | List of stock item locations | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_add_item_locations_request import InventoryAddItemLocationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryAddItemLocationsRequest from a JSON string
inventory_add_item_locations_request_instance = InventoryAddItemLocationsRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryAddItemLocationsRequest.to_json())

# convert the object into a dict
inventory_add_item_locations_request_dict = inventory_add_item_locations_request_instance.to_dict()
# create an instance of InventoryAddItemLocationsRequest from a dict
inventory_add_item_locations_request_from_dict = InventoryAddItemLocationsRequest.from_dict(inventory_add_item_locations_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


