# ProcessedOrdersDownloadOrdersToCSVRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**DownloadOrdersToCSVRequest**](DownloadOrdersToCSVRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.processedorders.models.processed_orders_download_orders_to_csv_request import ProcessedOrdersDownloadOrdersToCSVRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessedOrdersDownloadOrdersToCSVRequest from a JSON string
processed_orders_download_orders_to_csv_request_instance = ProcessedOrdersDownloadOrdersToCSVRequest.from_json(json)
# print the JSON string representation of the object
print(ProcessedOrdersDownloadOrdersToCSVRequest.to_json())

# convert the object into a dict
processed_orders_download_orders_to_csv_request_dict = processed_orders_download_orders_to_csv_request_instance.to_dict()
# create an instance of ProcessedOrdersDownloadOrdersToCSVRequest from a dict
processed_orders_download_orders_to_csv_request_from_dict = ProcessedOrdersDownloadOrdersToCSVRequest.from_dict(processed_orders_download_orders_to_csv_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


