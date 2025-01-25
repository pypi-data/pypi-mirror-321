# InventorySetInventoryItemImageAsMainRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory_item_id** | **str** | Id of StockItem | [optional] 
**main_image_id** | **str** | main image id | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_set_inventory_item_image_as_main_request import InventorySetInventoryItemImageAsMainRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventorySetInventoryItemImageAsMainRequest from a JSON string
inventory_set_inventory_item_image_as_main_request_instance = InventorySetInventoryItemImageAsMainRequest.from_json(json)
# print the JSON string representation of the object
print(InventorySetInventoryItemImageAsMainRequest.to_json())

# convert the object into a dict
inventory_set_inventory_item_image_as_main_request_dict = inventory_set_inventory_item_image_as_main_request_instance.to_dict()
# create an instance of InventorySetInventoryItemImageAsMainRequest from a dict
inventory_set_inventory_item_image_as_main_request_from_dict = InventorySetInventoryItemImageAsMainRequest.from_dict(inventory_set_inventory_item_image_as_main_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


