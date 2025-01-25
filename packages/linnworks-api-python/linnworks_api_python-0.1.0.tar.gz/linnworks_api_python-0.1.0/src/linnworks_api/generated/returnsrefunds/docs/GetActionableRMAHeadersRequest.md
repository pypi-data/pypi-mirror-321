# GetActionableRMAHeadersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** | The page number to return for a given set of filters | [optional] 
**filters** | [**ActionablePostSaleSearchFilters**](ActionablePostSaleSearchFilters.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.get_actionable_rma_headers_request import GetActionableRMAHeadersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetActionableRMAHeadersRequest from a JSON string
get_actionable_rma_headers_request_instance = GetActionableRMAHeadersRequest.from_json(json)
# print the JSON string representation of the object
print(GetActionableRMAHeadersRequest.to_json())

# convert the object into a dict
get_actionable_rma_headers_request_dict = get_actionable_rma_headers_request_instance.to_dict()
# create an instance of GetActionableRMAHeadersRequest from a dict
get_actionable_rma_headers_request_from_dict = GetActionableRMAHeadersRequest.from_dict(get_actionable_rma_headers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


