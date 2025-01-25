# GetProcessedOrAckedErrorRMAHeadersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** | The page number returned | [optional] 
**total_headers** | **int** | A count of the total number of RMA headers matching the filter set by the request | [optional] 
**headers_per_page** | **int** | A count of the number of RMA headers returned per page | [optional] 
**rma_headers** | [**List[OrderRMAHeader]**](OrderRMAHeader.md) | A collection of RMA headers matching the filter set by the request | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.get_processed_or_acked_error_rma_headers_response import GetProcessedOrAckedErrorRMAHeadersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetProcessedOrAckedErrorRMAHeadersResponse from a JSON string
get_processed_or_acked_error_rma_headers_response_instance = GetProcessedOrAckedErrorRMAHeadersResponse.from_json(json)
# print the JSON string representation of the object
print(GetProcessedOrAckedErrorRMAHeadersResponse.to_json())

# convert the object into a dict
get_processed_or_acked_error_rma_headers_response_dict = get_processed_or_acked_error_rma_headers_response_instance.to_dict()
# create an instance of GetProcessedOrAckedErrorRMAHeadersResponse from a dict
get_processed_or_acked_error_rma_headers_response_from_dict = GetProcessedOrAckedErrorRMAHeadersResponse.from_dict(get_processed_or_acked_error_rma_headers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


