# CommonPurchaseOrderItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_purchase_item_id** | **str** |  | [optional] 
**fk_stock_item_id** | **str** |  | [optional] 
**stock_item_int_id** | **int** |  | [optional] 
**quantity** | **int** |  | [optional] 
**cost** | **float** |  | [optional] 
**delivered** | **int** |  | [optional] 
**tax_rate** | **float** |  | [optional] 
**tax** | **float** |  | [optional] 
**pack_quantity** | **int** |  | [optional] 
**pack_size** | **int** |  | [optional] 
**sku** | **str** |  | [optional] 
**item_title** | **str** |  | [optional] 
**inventory_tracking_type** | **int** |  | [optional] 
**is_deleted** | **bool** |  | [optional] 
**sort_order** | **int** |  | [optional] 
**dim_height** | **float** |  | [optional] 
**dim_width** | **float** |  | [optional] 
**barcode_number** | **str** |  | [optional] 
**dim_depth** | **float** |  | [optional] 
**bound_to_open_orders_items** | **int** |  | [optional] 
**bin_rack** | **str** |  | [optional] 
**quantity_bound_to_open_orders_items** | **int** |  | [optional] 
**supplier_code** | **str** |  | [optional] 
**supplier_barcode** | **str** |  | [optional] 
**sku_group_ids** | **List[int]** |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.common_purchase_order_item import CommonPurchaseOrderItem

# TODO update the JSON string below
json = "{}"
# create an instance of CommonPurchaseOrderItem from a JSON string
common_purchase_order_item_instance = CommonPurchaseOrderItem.from_json(json)
# print the JSON string representation of the object
print(CommonPurchaseOrderItem.to_json())

# convert the object into a dict
common_purchase_order_item_dict = common_purchase_order_item_instance.to_dict()
# create an instance of CommonPurchaseOrderItem from a dict
common_purchase_order_item_from_dict = CommonPurchaseOrderItem.from_dict(common_purchase_order_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


