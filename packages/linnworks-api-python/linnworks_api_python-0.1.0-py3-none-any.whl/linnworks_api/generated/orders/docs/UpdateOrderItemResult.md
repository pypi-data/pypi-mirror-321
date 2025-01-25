# UpdateOrderItemResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**totals_info** | [**OrderTotalsInfo**](OrderTotalsInfo.md) |  | [optional] 
**item** | [**OrderItem**](OrderItem.md) |  | [optional] 
**item_weight** | **float** | Order item weight | [optional] 
**total_weight** | **float** | Order total weight | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.update_order_item_result import UpdateOrderItemResult

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOrderItemResult from a JSON string
update_order_item_result_instance = UpdateOrderItemResult.from_json(json)
# print the JSON string representation of the object
print(UpdateOrderItemResult.to_json())

# convert the object into a dict
update_order_item_result_dict = update_order_item_result_instance.to_dict()
# create an instance of UpdateOrderItemResult from a dict
update_order_item_result_from_dict = UpdateOrderItemResult.from_dict(update_order_item_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


