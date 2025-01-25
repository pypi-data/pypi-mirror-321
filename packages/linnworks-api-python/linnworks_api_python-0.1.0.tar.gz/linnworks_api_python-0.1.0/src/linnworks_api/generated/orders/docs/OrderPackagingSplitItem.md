# OrderPackagingSplitItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assigned_batches** | [**List[OrderItemShippingBatchWithRow]**](OrderItemShippingBatchWithRow.md) |  | [optional] 
**row_id** | **str** |  | [optional] 
**box_id** | **int** |  | [optional] [readonly] 
**quantity** | **int** |  | [optional] 
**tracking_number** | **str** |  | [optional] 
**weight** | **float** |  | [optional] 
**sku** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**is_batched** | **bool** |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.orders.models.order_packaging_split_item import OrderPackagingSplitItem

# TODO update the JSON string below
json = "{}"
# create an instance of OrderPackagingSplitItem from a JSON string
order_packaging_split_item_instance = OrderPackagingSplitItem.from_json(json)
# print the JSON string representation of the object
print(OrderPackagingSplitItem.to_json())

# convert the object into a dict
order_packaging_split_item_dict = order_packaging_split_item_instance.to_dict()
# create an instance of OrderPackagingSplitItem from a dict
order_packaging_split_item_from_dict = OrderPackagingSplitItem.from_dict(order_packaging_split_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


