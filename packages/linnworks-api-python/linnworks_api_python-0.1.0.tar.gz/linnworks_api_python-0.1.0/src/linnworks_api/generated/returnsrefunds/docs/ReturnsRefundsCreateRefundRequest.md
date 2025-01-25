# ReturnsRefundsCreateRefundRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**CreateRefundRequest**](CreateRefundRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.returns_refunds_create_refund_request import ReturnsRefundsCreateRefundRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnsRefundsCreateRefundRequest from a JSON string
returns_refunds_create_refund_request_instance = ReturnsRefundsCreateRefundRequest.from_json(json)
# print the JSON string representation of the object
print(ReturnsRefundsCreateRefundRequest.to_json())

# convert the object into a dict
returns_refunds_create_refund_request_dict = returns_refunds_create_refund_request_instance.to_dict()
# create an instance of ReturnsRefundsCreateRefundRequest from a dict
returns_refunds_create_refund_request_from_dict = ReturnsRefundsCreateRefundRequest.from_dict(returns_refunds_create_refund_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


