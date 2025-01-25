# OrderItemReturnInfoBatched


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_item_batch_id** | **int** |  | [optional] 
**batch_inventory_id** | **int** |  | [optional] 
**batch_number** | **str** |  | [optional] 
**despatch_unit_value** | **float** |  | [optional] 
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
from linnworks_api.generated.processedorders.models.order_item_return_info_batched import OrderItemReturnInfoBatched

# TODO update the JSON string below
json = "{}"
# create an instance of OrderItemReturnInfoBatched from a JSON string
order_item_return_info_batched_instance = OrderItemReturnInfoBatched.from_json(json)
# print the JSON string representation of the object
print(OrderItemReturnInfoBatched.to_json())

# convert the object into a dict
order_item_return_info_batched_dict = order_item_return_info_batched_instance.to_dict()
# create an instance of OrderItemReturnInfoBatched from a dict
order_item_return_info_batched_from_dict = OrderItemReturnInfoBatched.from_dict(order_item_return_info_batched_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


