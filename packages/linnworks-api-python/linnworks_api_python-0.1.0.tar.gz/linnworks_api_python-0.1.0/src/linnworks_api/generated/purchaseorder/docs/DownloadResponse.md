# DownloadResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**path** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.download_response import DownloadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadResponse from a JSON string
download_response_instance = DownloadResponse.from_json(json)
# print the JSON string representation of the object
print(DownloadResponse.to_json())

# convert the object into a dict
download_response_dict = download_response_instance.to_dict()
# create an instance of DownloadResponse from a dict
download_response_from_dict = DownloadResponse.from_dict(download_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


