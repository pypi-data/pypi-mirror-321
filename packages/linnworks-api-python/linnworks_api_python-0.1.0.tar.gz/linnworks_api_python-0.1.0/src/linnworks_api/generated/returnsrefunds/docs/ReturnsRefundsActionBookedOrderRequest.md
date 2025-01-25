# ReturnsRefundsActionBookedOrderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_order_id** | **str** | unique ID of the order | [optional] 
**booked_items** | [**List[BookedReturnsExchangeItem]**](BookedReturnsExchangeItem.md) | list of returns/exchange items to be actioned | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.returns_refunds_action_booked_order_request import ReturnsRefundsActionBookedOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnsRefundsActionBookedOrderRequest from a JSON string
returns_refunds_action_booked_order_request_instance = ReturnsRefundsActionBookedOrderRequest.from_json(json)
# print the JSON string representation of the object
print(ReturnsRefundsActionBookedOrderRequest.to_json())

# convert the object into a dict
returns_refunds_action_booked_order_request_dict = returns_refunds_action_booked_order_request_instance.to_dict()
# create an instance of ReturnsRefundsActionBookedOrderRequest from a dict
returns_refunds_action_booked_order_request_from_dict = ReturnsRefundsActionBookedOrderRequest.from_dict(returns_refunds_action_booked_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


