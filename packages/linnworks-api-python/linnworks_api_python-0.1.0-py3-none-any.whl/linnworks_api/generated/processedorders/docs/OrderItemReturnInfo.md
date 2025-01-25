# OrderItemReturnInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**child_items** | [**List[OrderItemReturnInfo]**](OrderItemReturnInfo.md) |  | [optional] 
**batches** | [**List[OrderItemReturnInfoBatched]**](OrderItemReturnInfoBatched.md) |  | [optional] 
**order_id** | **str** |  | [optional] [readonly] 
**fk_order_item_row_id** | **str** |  | [optional] 
**parent_row_id** | **str** |  | [optional] 
**returnable_qty** | **int** |  | [optional] [readonly] 
**order_qty** | **int** |  | [optional] 
**returned_qty** | **int** |  | [optional] 
**sku** | **str** |  | [optional] 
**item_title** | **str** |  | [optional] 
**unit_value** | **float** |  | [optional] 
**tax_rate** | **float** |  | [optional] 
**tax_cost_inclusive** | **bool** |  | [optional] 
**currency** | **str** |  | [optional] 
**is_composite_parent** | **bool** |  | [optional] 
**is_partial_composite_return** | **bool** |  | [optional] 
**parent_ratio** | **int** |  | [optional] 
**pk_stock_item_id** | **str** |  | [optional] 
**resent_qty** | **int** |  | [optional] 
**fk_refund_row_id** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.processedorders.models.order_item_return_info import OrderItemReturnInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OrderItemReturnInfo from a JSON string
order_item_return_info_instance = OrderItemReturnInfo.from_json(json)
# print the JSON string representation of the object
print(OrderItemReturnInfo.to_json())

# convert the object into a dict
order_item_return_info_dict = order_item_return_info_instance.to_dict()
# create an instance of OrderItemReturnInfo from a dict
order_item_return_info_from_dict = OrderItemReturnInfo.from_dict(order_item_return_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


