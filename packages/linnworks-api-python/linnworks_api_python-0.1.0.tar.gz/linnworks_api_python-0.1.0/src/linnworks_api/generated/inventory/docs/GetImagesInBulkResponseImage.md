# GetImagesInBulkResponseImage

Image response item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sku** | **str** | SKU | [optional] 
**is_main** | **bool** | Is main image | [optional] 
**pk_row_id** | **str** | Image row id | [optional] 
**checksum_value** | **str** | Checksum | [optional] 
**raw_checksum** | **str** | Raw file checksum (original and unaltered) | [optional] 
**sort_order** | **int** | Sort order | [optional] 
**stock_item_id** | **str** | Stockitem id | [optional] 
**full_source** | **str** | Full image path | [optional] 
**full_source_thumbnail** | **str** | Thumbnail image path | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.get_images_in_bulk_response_image import GetImagesInBulkResponseImage

# TODO update the JSON string below
json = "{}"
# create an instance of GetImagesInBulkResponseImage from a JSON string
get_images_in_bulk_response_image_instance = GetImagesInBulkResponseImage.from_json(json)
# print the JSON string representation of the object
print(GetImagesInBulkResponseImage.to_json())

# convert the object into a dict
get_images_in_bulk_response_image_dict = get_images_in_bulk_response_image_instance.to_dict()
# create an instance of GetImagesInBulkResponseImage from a dict
get_images_in_bulk_response_image_from_dict = GetImagesInBulkResponseImage.from_dict(get_images_in_bulk_response_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


