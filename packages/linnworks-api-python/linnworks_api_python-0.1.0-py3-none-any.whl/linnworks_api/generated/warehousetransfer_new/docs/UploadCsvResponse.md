# UploadCsvResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** |  | [optional] 
**expiration_date** | **datetime** | File gets deleted from s3 automatically | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.upload_csv_response import UploadCsvResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UploadCsvResponse from a JSON string
upload_csv_response_instance = UploadCsvResponse.from_json(json)
# print the JSON string representation of the object
print(UploadCsvResponse.to_json())

# convert the object into a dict
upload_csv_response_dict = upload_csv_response_instance.to_dict()
# create an instance of UploadCsvResponse from a dict
upload_csv_response_from_dict = UploadCsvResponse.from_dict(upload_csv_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


