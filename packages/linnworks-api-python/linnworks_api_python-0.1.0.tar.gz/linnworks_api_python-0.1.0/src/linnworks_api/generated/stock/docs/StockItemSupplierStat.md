# StockItemSupplierStat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_default** | **bool** |  | [optional] 
**supplier** | **str** |  | [optional] 
**supplier_id** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**supplier_barcode** | **str** |  | [optional] 
**lead_time** | **int** |  | [optional] 
**purchase_price** | **float** |  | [optional] 
**min_price** | **float** |  | [optional] 
**max_price** | **float** |  | [optional] 
**average_price** | **float** |  | [optional] 
**average_lead_time** | **float** |  | [optional] 
**supplier_min_order_qty** | **int** |  | [optional] 
**supplier_pack_size** | **int** |  | [optional] 
**supplier_currency** | **str** |  | [optional] 
**stock_item_id** | **str** |  | [optional] 
**stock_item_int_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.stock_item_supplier_stat import StockItemSupplierStat

# TODO update the JSON string below
json = "{}"
# create an instance of StockItemSupplierStat from a JSON string
stock_item_supplier_stat_instance = StockItemSupplierStat.from_json(json)
# print the JSON string representation of the object
print(StockItemSupplierStat.to_json())

# convert the object into a dict
stock_item_supplier_stat_dict = stock_item_supplier_stat_instance.to_dict()
# create an instance of StockItemSupplierStat from a dict
stock_item_supplier_stat_from_dict = StockItemSupplierStat.from_dict(stock_item_supplier_stat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


