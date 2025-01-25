# GetImagesInBulkResponse

Bulk image response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**images** | [**List[GetImagesInBulkResponseImage]**](GetImagesInBulkResponseImage.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.get_images_in_bulk_response import GetImagesInBulkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetImagesInBulkResponse from a JSON string
get_images_in_bulk_response_instance = GetImagesInBulkResponse.from_json(json)
# print the JSON string representation of the object
print(GetImagesInBulkResponse.to_json())

# convert the object into a dict
get_images_in_bulk_response_dict = get_images_in_bulk_response_instance.to_dict()
# create an instance of GetImagesInBulkResponse from a dict
get_images_in_bulk_response_from_dict = GetImagesInBulkResponse.from_dict(get_images_in_bulk_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


