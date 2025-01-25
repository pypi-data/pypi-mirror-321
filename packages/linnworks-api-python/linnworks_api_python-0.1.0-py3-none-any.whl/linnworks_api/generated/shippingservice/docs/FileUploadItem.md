# FileUploadItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encoded_file** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**doc_type** | **str** |  | [optional] 
**expiration_date** | **str** |  | [optional] 
**doc_usage_type** | **str** |  | [optional] 
**order_id** | **str** |  | [optional] 
**account_id** | **str** |  | [optional] 
**vendor** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.shippingservice.models.file_upload_item import FileUploadItem

# TODO update the JSON string below
json = "{}"
# create an instance of FileUploadItem from a JSON string
file_upload_item_instance = FileUploadItem.from_json(json)
# print the JSON string representation of the object
print(FileUploadItem.to_json())

# convert the object into a dict
file_upload_item_dict = file_upload_item_instance.to_dict()
# create an instance of FileUploadItem from a dict
file_upload_item_from_dict = FileUploadItem.from_dict(file_upload_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


