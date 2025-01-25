# ReturnsRefundsGetReturnOptionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**GetReturnOptionsRequest**](GetReturnOptionsRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.returns_refunds_get_return_options_request import ReturnsRefundsGetReturnOptionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnsRefundsGetReturnOptionsRequest from a JSON string
returns_refunds_get_return_options_request_instance = ReturnsRefundsGetReturnOptionsRequest.from_json(json)
# print the JSON string representation of the object
print(ReturnsRefundsGetReturnOptionsRequest.to_json())

# convert the object into a dict
returns_refunds_get_return_options_request_dict = returns_refunds_get_return_options_request_instance.to_dict()
# create an instance of ReturnsRefundsGetReturnOptionsRequest from a dict
returns_refunds_get_return_options_request_from_dict = ReturnsRefundsGetReturnOptionsRequest.from_dict(returns_refunds_get_return_options_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


