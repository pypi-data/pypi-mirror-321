# GetActionableRefundHeadersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** | The page number returned | [optional] 
**total_headers** | **int** | A count of the total number of refund headers matching the filter set by the request | [optional] 
**headers_per_page** | **int** | A count of the number of refund headers returned per page | [optional] 
**refund_headers** | [**List[OrderRefundHeader]**](OrderRefundHeader.md) | A collection of refund headers matching the filter set by the request | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.get_actionable_refund_headers_response import GetActionableRefundHeadersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetActionableRefundHeadersResponse from a JSON string
get_actionable_refund_headers_response_instance = GetActionableRefundHeadersResponse.from_json(json)
# print the JSON string representation of the object
print(GetActionableRefundHeadersResponse.to_json())

# convert the object into a dict
get_actionable_refund_headers_response_dict = get_actionable_refund_headers_response_instance.to_dict()
# create an instance of GetActionableRefundHeadersResponse from a dict
get_actionable_refund_headers_response_from_dict = GetActionableRefundHeadersResponse.from_dict(get_actionable_refund_headers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


