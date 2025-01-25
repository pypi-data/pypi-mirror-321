# GetProcessedOrAckedErrorRefundHeadersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** | The page number to return for a given set of filters | [optional] 
**filters** | [**ProcessedPostSaleSearchFilters**](ProcessedPostSaleSearchFilters.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.get_processed_or_acked_error_refund_headers_request import GetProcessedOrAckedErrorRefundHeadersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetProcessedOrAckedErrorRefundHeadersRequest from a JSON string
get_processed_or_acked_error_refund_headers_request_instance = GetProcessedOrAckedErrorRefundHeadersRequest.from_json(json)
# print the JSON string representation of the object
print(GetProcessedOrAckedErrorRefundHeadersRequest.to_json())

# convert the object into a dict
get_processed_or_acked_error_refund_headers_request_dict = get_processed_or_acked_error_refund_headers_request_instance.to_dict()
# create an instance of GetProcessedOrAckedErrorRefundHeadersRequest from a dict
get_processed_or_acked_error_refund_headers_request_from_dict = GetProcessedOrAckedErrorRefundHeadersRequest.from_dict(get_processed_or_acked_error_refund_headers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


