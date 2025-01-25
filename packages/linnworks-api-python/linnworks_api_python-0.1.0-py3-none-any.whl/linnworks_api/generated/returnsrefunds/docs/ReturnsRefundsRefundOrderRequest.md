# ReturnsRefundsRefundOrderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_order_id** | **str** | unique ID of the order | [optional] 
**refund_reference** | **str** | Refund Reference Id | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.returns_refunds_refund_order_request import ReturnsRefundsRefundOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnsRefundsRefundOrderRequest from a JSON string
returns_refunds_refund_order_request_instance = ReturnsRefundsRefundOrderRequest.from_json(json)
# print the JSON string representation of the object
print(ReturnsRefundsRefundOrderRequest.to_json())

# convert the object into a dict
returns_refunds_refund_order_request_dict = returns_refunds_refund_order_request_instance.to_dict()
# create an instance of ReturnsRefundsRefundOrderRequest from a dict
returns_refunds_refund_order_request_from_dict = ReturnsRefundsRefundOrderRequest.from_dict(returns_refunds_refund_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


