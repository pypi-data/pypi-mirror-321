# OrderItemShippingBatchWithRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_item_row_id** | **str** |  | [optional] 
**batch_number** | **str** |  | [optional] 
**fk_bin_id** | **str** |  | [optional] 
**fk_order_item_batch_id** | **int** |  | [optional] 
**quantity** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.order_item_shipping_batch_with_row import OrderItemShippingBatchWithRow

# TODO update the JSON string below
json = "{}"
# create an instance of OrderItemShippingBatchWithRow from a JSON string
order_item_shipping_batch_with_row_instance = OrderItemShippingBatchWithRow.from_json(json)
# print the JSON string representation of the object
print(OrderItemShippingBatchWithRow.to_json())

# convert the object into a dict
order_item_shipping_batch_with_row_dict = order_item_shipping_batch_with_row_instance.to_dict()
# create an instance of OrderItemShippingBatchWithRow from a dict
order_item_shipping_batch_with_row_from_dict = OrderItemShippingBatchWithRow.from_dict(order_item_shipping_batch_with_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


