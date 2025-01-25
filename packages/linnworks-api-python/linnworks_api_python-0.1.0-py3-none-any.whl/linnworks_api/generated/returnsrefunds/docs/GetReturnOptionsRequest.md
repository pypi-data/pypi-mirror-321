# GetReturnOptionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** |  | [optional] 
**rma_header_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.get_return_options_request import GetReturnOptionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetReturnOptionsRequest from a JSON string
get_return_options_request_instance = GetReturnOptionsRequest.from_json(json)
# print the JSON string representation of the object
print(GetReturnOptionsRequest.to_json())

# convert the object into a dict
get_return_options_request_dict = get_return_options_request_instance.to_dict()
# create an instance of GetReturnOptionsRequest from a dict
get_return_options_request_from_dict = GetReturnOptionsRequest.from_dict(get_return_options_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


