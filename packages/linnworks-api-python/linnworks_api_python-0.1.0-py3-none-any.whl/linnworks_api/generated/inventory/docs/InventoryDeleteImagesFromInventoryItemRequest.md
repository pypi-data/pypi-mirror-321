# InventoryDeleteImagesFromInventoryItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory_item_images** | **Dict[str, List[str]]** | Inventory item ids and a list of image urls to be deleted for each item | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_delete_images_from_inventory_item_request import InventoryDeleteImagesFromInventoryItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryDeleteImagesFromInventoryItemRequest from a JSON string
inventory_delete_images_from_inventory_item_request_instance = InventoryDeleteImagesFromInventoryItemRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryDeleteImagesFromInventoryItemRequest.to_json())

# convert the object into a dict
inventory_delete_images_from_inventory_item_request_dict = inventory_delete_images_from_inventory_item_request_instance.to_dict()
# create an instance of InventoryDeleteImagesFromInventoryItemRequest from a dict
inventory_delete_images_from_inventory_item_request_from_dict = InventoryDeleteImagesFromInventoryItemRequest.from_dict(inventory_delete_images_from_inventory_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


