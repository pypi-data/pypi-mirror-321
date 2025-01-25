# ReturnsRefundsDeleteBookedOrderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_order_id** | **str** | unique ID of the order | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.returns_refunds_delete_booked_order_request import ReturnsRefundsDeleteBookedOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnsRefundsDeleteBookedOrderRequest from a JSON string
returns_refunds_delete_booked_order_request_instance = ReturnsRefundsDeleteBookedOrderRequest.from_json(json)
# print the JSON string representation of the object
print(ReturnsRefundsDeleteBookedOrderRequest.to_json())

# convert the object into a dict
returns_refunds_delete_booked_order_request_dict = returns_refunds_delete_booked_order_request_instance.to_dict()
# create an instance of ReturnsRefundsDeleteBookedOrderRequest from a dict
returns_refunds_delete_booked_order_request_from_dict = ReturnsRefundsDeleteBookedOrderRequest.from_dict(returns_refunds_delete_booked_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


