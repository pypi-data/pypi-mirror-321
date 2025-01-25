# DownloadOrdersToCSVRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_term** | **str** | Search Term | [optional] 
**search_filters** | [**List[SearchFilters]**](SearchFilters.md) | Search Filters | [optional] 
**date_field** | **str** | Date Field Type | [optional] 
**from_date** | **datetime** | From Date | [optional] 
**to_date** | **datetime** | To Date | [optional] 
**search_sorting** | [**SearchSorting**](SearchSorting.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.processedorders.models.download_orders_to_csv_request import DownloadOrdersToCSVRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadOrdersToCSVRequest from a JSON string
download_orders_to_csv_request_instance = DownloadOrdersToCSVRequest.from_json(json)
# print the JSON string representation of the object
print(DownloadOrdersToCSVRequest.to_json())

# convert the object into a dict
download_orders_to_csv_request_dict = download_orders_to_csv_request_instance.to_dict()
# create an instance of DownloadOrdersToCSVRequest from a dict
download_orders_to_csv_request_from_dict = DownloadOrdersToCSVRequest.from_dict(download_orders_to_csv_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


