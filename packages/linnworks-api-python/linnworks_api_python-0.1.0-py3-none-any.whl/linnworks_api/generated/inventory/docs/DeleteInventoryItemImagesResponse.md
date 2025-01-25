# DeleteInventoryItemImagesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory_item_id** | **str** | InventoryItemId/StockItemId | [optional] 
**item_number** | **str** | The Item Number (SKU). Only provided if passed in the request | [optional] 
**image_id** | **str** | Image Id | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.delete_inventory_item_images_response import DeleteInventoryItemImagesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteInventoryItemImagesResponse from a JSON string
delete_inventory_item_images_response_instance = DeleteInventoryItemImagesResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteInventoryItemImagesResponse.to_json())

# convert the object into a dict
delete_inventory_item_images_response_dict = delete_inventory_item_images_response_instance.to_dict()
# create an instance of DeleteInventoryItemImagesResponse from a dict
delete_inventory_item_images_response_from_dict = DeleteInventoryItemImagesResponse.from_dict(delete_inventory_item_images_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


