# ReturnsRefundsGetRefundOptionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**GetRefundOptionsRequest**](GetRefundOptionsRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.returns_refunds_get_refund_options_request import ReturnsRefundsGetRefundOptionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnsRefundsGetRefundOptionsRequest from a JSON string
returns_refunds_get_refund_options_request_instance = ReturnsRefundsGetRefundOptionsRequest.from_json(json)
# print the JSON string representation of the object
print(ReturnsRefundsGetRefundOptionsRequest.to_json())

# convert the object into a dict
returns_refunds_get_refund_options_request_dict = returns_refunds_get_refund_options_request_instance.to_dict()
# create an instance of ReturnsRefundsGetRefundOptionsRequest from a dict
returns_refunds_get_refund_options_request_from_dict = ReturnsRefundsGetRefundOptionsRequest.from_dict(returns_refunds_get_refund_options_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


