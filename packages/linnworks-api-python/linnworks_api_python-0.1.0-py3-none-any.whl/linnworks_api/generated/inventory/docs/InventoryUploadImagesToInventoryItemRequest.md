# InventoryUploadImagesToInventoryItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory_item_id** | **str** | Id of StockItem | [optional] 
**image_ids** | **List[str]** | List of image Ids | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_upload_images_to_inventory_item_request import InventoryUploadImagesToInventoryItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryUploadImagesToInventoryItemRequest from a JSON string
inventory_upload_images_to_inventory_item_request_instance = InventoryUploadImagesToInventoryItemRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryUploadImagesToInventoryItemRequest.to_json())

# convert the object into a dict
inventory_upload_images_to_inventory_item_request_dict = inventory_upload_images_to_inventory_item_request_instance.to_dict()
# create an instance of InventoryUploadImagesToInventoryItemRequest from a dict
inventory_upload_images_to_inventory_item_request_from_dict = InventoryUploadImagesToInventoryItemRequest.from_dict(inventory_upload_images_to_inventory_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


