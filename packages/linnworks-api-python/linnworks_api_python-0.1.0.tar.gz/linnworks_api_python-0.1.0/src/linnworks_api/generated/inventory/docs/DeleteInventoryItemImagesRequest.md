# DeleteInventoryItemImagesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory_item_id** | **str** | The id of the item. If not provided, you must provide ItemNumber | [optional] 
**item_number** | **str** | The item number (SKU) for the item. If InventoryItemId is provided, this will be ignored. | [optional] 
**image_ids** | **List[str]** | A list of images by image ids to delete for the item | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.delete_inventory_item_images_request import DeleteInventoryItemImagesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteInventoryItemImagesRequest from a JSON string
delete_inventory_item_images_request_instance = DeleteInventoryItemImagesRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteInventoryItemImagesRequest.to_json())

# convert the object into a dict
delete_inventory_item_images_request_dict = delete_inventory_item_images_request_instance.to_dict()
# create an instance of DeleteInventoryItemImagesRequest from a dict
delete_inventory_item_images_request_from_dict = DeleteInventoryItemImagesRequest.from_dict(delete_inventory_item_images_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


