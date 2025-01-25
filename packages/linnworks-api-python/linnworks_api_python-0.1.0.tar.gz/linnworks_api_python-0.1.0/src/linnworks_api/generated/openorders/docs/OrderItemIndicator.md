# OrderItemIndicator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_item_id** | **str** |  | [optional] 
**stock_item_id** | **str** |  | [optional] 
**indicator** | **int** |  | [optional] 
**fulfillment_state** | **str** |  | [optional] 
**purchase_order_state** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.openorders.models.order_item_indicator import OrderItemIndicator

# TODO update the JSON string below
json = "{}"
# create an instance of OrderItemIndicator from a JSON string
order_item_indicator_instance = OrderItemIndicator.from_json(json)
# print the JSON string representation of the object
print(OrderItemIndicator.to_json())

# convert the object into a dict
order_item_indicator_dict = order_item_indicator_instance.to_dict()
# create an instance of OrderItemIndicator from a dict
order_item_indicator_from_dict = OrderItemIndicator.from_dict(order_item_indicator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


