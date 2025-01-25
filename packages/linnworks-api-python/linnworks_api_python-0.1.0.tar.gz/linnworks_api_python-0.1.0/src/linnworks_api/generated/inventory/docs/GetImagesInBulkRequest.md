# GetImagesInBulkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_item_ids** | **List[str]** |  | [optional] 
**skus** | **List[str]** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.get_images_in_bulk_request import GetImagesInBulkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetImagesInBulkRequest from a JSON string
get_images_in_bulk_request_instance = GetImagesInBulkRequest.from_json(json)
# print the JSON string representation of the object
print(GetImagesInBulkRequest.to_json())

# convert the object into a dict
get_images_in_bulk_request_dict = get_images_in_bulk_request_instance.to_dict()
# create an instance of GetImagesInBulkRequest from a dict
get_images_in_bulk_request_from_dict = GetImagesInBulkRequest.from_dict(get_images_in_bulk_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


