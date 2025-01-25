# StockItemHeader


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_number** | **str** |  | [optional] 
**item_title** | **str** |  | [optional] 
**barcode_number** | **str** |  | [optional] 
**meta_data** | **str** |  | [optional] 
**is_variation_parent** | **bool** |  | [optional] 
**is_batched_stock_type** | **bool** |  | [optional] [readonly] 
**purchase_price** | **float** |  | [optional] 
**retail_price** | **float** |  | [optional] 
**tax_rate** | **float** |  | [optional] 
**postal_service_id** | **str** |  | [optional] 
**postal_service_name** | **str** |  | [optional] 
**category_id** | **str** |  | [optional] 
**category_name** | **str** |  | [optional] 
**package_group_id** | **str** |  | [optional] 
**package_group_name** | **str** |  | [optional] 
**height** | **float** |  | [optional] 
**width** | **float** |  | [optional] 
**depth** | **float** |  | [optional] 
**weight** | **float** |  | [optional] 
**creation_date** | **datetime** |  | [optional] 
**inventory_tracking_type** | **int** |  | [optional] 
**batch_number_scan_required** | **bool** |  | [optional] 
**serial_number_scan_required** | **bool** |  | [optional] 
**stock_item_id** | **str** |  | [optional] 
**stock_item_int_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.stock_item_header import StockItemHeader

# TODO update the JSON string below
json = "{}"
# create an instance of StockItemHeader from a JSON string
stock_item_header_instance = StockItemHeader.from_json(json)
# print the JSON string representation of the object
print(StockItemHeader.to_json())

# convert the object into a dict
stock_item_header_dict = stock_item_header_instance.to_dict()
# create an instance of StockItemHeader from a dict
stock_item_header_from_dict = StockItemHeader.from_dict(stock_item_header_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


