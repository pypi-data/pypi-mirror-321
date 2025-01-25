# OrderSplit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[OrderSplitOutItem]**](OrderSplitOutItem.md) |  | [optional] 
**postal_service_id** | **str** |  | [optional] 
**park_order** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.order_split import OrderSplit

# TODO update the JSON string below
json = "{}"
# create an instance of OrderSplit from a JSON string
order_split_instance = OrderSplit.from_json(json)
# print the JSON string representation of the object
print(OrderSplit.to_json())

# convert the object into a dict
order_split_dict = order_split_instance.to_dict()
# create an instance of OrderSplit from a dict
order_split_from_dict = OrderSplit.from_dict(order_split_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


