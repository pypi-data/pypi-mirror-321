# DownloadOrdersToCSVResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**download_progress** | **float** |  | [optional] 
**upload_progress** | **float** |  | [optional] 
**id** | **str** |  | [optional] 
**creation_date** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.processedorders.models.download_orders_to_csv_response import DownloadOrdersToCSVResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadOrdersToCSVResponse from a JSON string
download_orders_to_csv_response_instance = DownloadOrdersToCSVResponse.from_json(json)
# print the JSON string representation of the object
print(DownloadOrdersToCSVResponse.to_json())

# convert the object into a dict
download_orders_to_csv_response_dict = download_orders_to_csv_response_instance.to_dict()
# create an instance of DownloadOrdersToCSVResponse from a dict
download_orders_to_csv_response_from_dict = DownloadOrdersToCSVResponse.from_dict(download_orders_to_csv_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


