# InventoryDeleteItemLocationsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory_item_id** | **str** | Id of StockItem | [optional] 
**item_locations** | **List[str]** | List of stock item location ids | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_delete_item_locations_request import InventoryDeleteItemLocationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryDeleteItemLocationsRequest from a JSON string
inventory_delete_item_locations_request_instance = InventoryDeleteItemLocationsRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryDeleteItemLocationsRequest.to_json())

# convert the object into a dict
inventory_delete_item_locations_request_dict = inventory_delete_item_locations_request_instance.to_dict()
# create an instance of InventoryDeleteItemLocationsRequest from a dict
inventory_delete_item_locations_request_from_dict = InventoryDeleteItemLocationsRequest.from_dict(inventory_delete_item_locations_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


