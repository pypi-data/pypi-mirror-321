# OrderFulfillmentState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fulfillment_state** | **str** |  | [optional] 
**purchase_order_state** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.order_fulfillment_state import OrderFulfillmentState

# TODO update the JSON string below
json = "{}"
# create an instance of OrderFulfillmentState from a JSON string
order_fulfillment_state_instance = OrderFulfillmentState.from_json(json)
# print the JSON string representation of the object
print(OrderFulfillmentState.to_json())

# convert the object into a dict
order_fulfillment_state_dict = order_fulfillment_state_instance.to_dict()
# create an instance of OrderFulfillmentState from a dict
order_fulfillment_state_from_dict = OrderFulfillmentState.from_dict(order_fulfillment_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


