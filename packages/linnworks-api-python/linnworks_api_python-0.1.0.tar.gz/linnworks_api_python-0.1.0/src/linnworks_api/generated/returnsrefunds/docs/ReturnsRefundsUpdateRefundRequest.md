# ReturnsRefundsUpdateRefundRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**UpdateRefundRequest**](UpdateRefundRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.returns_refunds_update_refund_request import ReturnsRefundsUpdateRefundRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnsRefundsUpdateRefundRequest from a JSON string
returns_refunds_update_refund_request_instance = ReturnsRefundsUpdateRefundRequest.from_json(json)
# print the JSON string representation of the object
print(ReturnsRefundsUpdateRefundRequest.to_json())

# convert the object into a dict
returns_refunds_update_refund_request_dict = returns_refunds_update_refund_request_instance.to_dict()
# create an instance of ReturnsRefundsUpdateRefundRequest from a dict
returns_refunds_update_refund_request_from_dict = ReturnsRefundsUpdateRefundRequest.from_dict(returns_refunds_update_refund_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


