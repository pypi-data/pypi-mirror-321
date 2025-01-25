# OrderItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** |  | [optional] 
**item_number** | **str** |  | [optional] 
**sku** | **str** |  | [optional] 
**item_source** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**category_name** | **str** |  | [optional] 
**composite_availablity** | **int** |  | [optional] 
**stock_levels_specified** | **bool** |  | [optional] 
**on_order** | **int** |  | [optional] 
**on_purchase_order** | [**OrderItemOnOrder**](OrderItemOnOrder.md) |  | [optional] 
**in_order_book** | **int** |  | [optional] 
**level** | **int** |  | [optional] 
**minimum_level** | **int** |  | [optional] 
**available_stock** | **int** |  | [optional] 
**price_per_unit** | **float** |  | [optional] 
**unit_cost** | **float** |  | [optional] 
**despatch_stock_unit_cost** | **float** |  | [optional] 
**discount** | **float** |  | [optional] 
**tax** | **float** |  | [optional] [readonly] 
**tax_rate** | **float** |  | [optional] 
**cost** | **float** |  | [optional] 
**cost_inc_tax** | **float** |  | [optional] 
**composite_sub_items** | [**List[OrderItem]**](OrderItem.md) |  | [optional] 
**is_service** | **bool** |  | [optional] 
**sales_tax** | **float** |  | [optional] 
**tax_cost_inclusive** | **bool** |  | [optional] 
**part_shipped** | **bool** |  | [optional] 
**weight** | **float** |  | [optional] 
**barcode_number** | **str** |  | [optional] 
**market** | **int** |  | [optional] 
**channel_sku** | **str** |  | [optional] 
**channel_title** | **str** |  | [optional] 
**discount_value** | **float** |  | [optional] [readonly] 
**has_image** | **bool** |  | [optional] [readonly] 
**image_id** | **str** |  | [optional] 
**additional_info** | [**List[OrderItemOption]**](OrderItemOption.md) |  | [optional] 
**stock_level_indicator** | **int** |  | [optional] 
**shipping_cost** | **float** |  | [optional] 
**part_shipped_qty** | **int** |  | [optional] 
**item_name** | **str** |  | [optional] 
**batch_number_scan_required** | **bool** |  | [optional] 
**serial_number_scan_required** | **bool** |  | [optional] 
**bin_rack** | **str** |  | [optional] 
**bin_racks** | [**List[OrderItemBinRack]**](OrderItemBinRack.md) |  | [optional] 
**inventory_tracking_type** | **int** |  | [optional] 
**is_batched_stock_item** | **bool** |  | [optional] [readonly] 
**is_warehouse_managed** | **bool** |  | [optional] 
**is_unlinked** | **bool** |  | [optional] [readonly] 
**stock_item_int_id** | **int** |  | [optional] 
**boxes** | [**List[StockItemBoxConfiguration]**](StockItemBoxConfiguration.md) |  | [optional] 
**added_date** | **datetime** |  | [optional] 
**row_id** | **str** |  | [optional] 
**order_id** | **str** |  | [optional] 
**stock_item_id** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.postsale.models.order_item import OrderItem

# TODO update the JSON string below
json = "{}"
# create an instance of OrderItem from a JSON string
order_item_instance = OrderItem.from_json(json)
# print the JSON string representation of the object
print(OrderItem.to_json())

# convert the object into a dict
order_item_dict = order_item_instance.to_dict()
# create an instance of OrderItem from a dict
order_item_from_dict = OrderItem.from_dict(order_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


