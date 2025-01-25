# AddImageToInventoryItemResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_item_id** | **str** | pkStockItemId of an item | [optional] 
**image_id** | **str** | ImageId of newly added image | [optional] 
**image_url** | **str** | Image new URL | [optional] 
**image_thumbnail_url** | **str** | Image Thumbnail URL | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.add_image_to_inventory_item_response import AddImageToInventoryItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddImageToInventoryItemResponse from a JSON string
add_image_to_inventory_item_response_instance = AddImageToInventoryItemResponse.from_json(json)
# print the JSON string representation of the object
print(AddImageToInventoryItemResponse.to_json())

# convert the object into a dict
add_image_to_inventory_item_response_dict = add_image_to_inventory_item_response_instance.to_dict()
# create an instance of AddImageToInventoryItemResponse from a dict
add_image_to_inventory_item_response_from_dict = AddImageToInventoryItemResponse.from_dict(add_image_to_inventory_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


