# OrderSplitOutItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**row_id** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**weight** | **float** |  | [optional] 
**unit_cost** | **float** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.order_split_out_item import OrderSplitOutItem

# TODO update the JSON string below
json = "{}"
# create an instance of OrderSplitOutItem from a JSON string
order_split_out_item_instance = OrderSplitOutItem.from_json(json)
# print the JSON string representation of the object
print(OrderSplitOutItem.to_json())

# convert the object into a dict
order_split_out_item_dict = order_split_out_item_instance.to_dict()
# create an instance of OrderSplitOutItem from a dict
order_split_out_item_from_dict = OrderSplitOutItem.from_dict(order_split_out_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


