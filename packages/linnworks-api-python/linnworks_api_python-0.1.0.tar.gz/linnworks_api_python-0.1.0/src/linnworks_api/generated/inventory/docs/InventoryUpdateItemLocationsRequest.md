# InventoryUpdateItemLocationsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_locations** | [**List[StockItemLocation]**](StockItemLocation.md) | List of stock item locations | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_update_item_locations_request import InventoryUpdateItemLocationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryUpdateItemLocationsRequest from a JSON string
inventory_update_item_locations_request_instance = InventoryUpdateItemLocationsRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryUpdateItemLocationsRequest.to_json())

# convert the object into a dict
inventory_update_item_locations_request_dict = inventory_update_item_locations_request_instance.to_dict()
# create an instance of InventoryUpdateItemLocationsRequest from a dict
inventory_update_item_locations_request_from_dict = InventoryUpdateItemLocationsRequest.from_dict(inventory_update_item_locations_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


