# StockItemFull


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**suppliers** | [**List[StockItemSupplierStat]**](StockItemSupplierStat.md) |  | [optional] 
**stock_levels** | [**List[StockItemLevel]**](StockItemLevel.md) |  | [optional] 
**item_channel_descriptions** | [**List[StockItemDescription]**](StockItemDescription.md) |  | [optional] [readonly] 
**item_extended_properties** | [**List[StockItemExtendedProperty]**](StockItemExtendedProperty.md) |  | [optional] [readonly] 
**item_channel_titles** | [**List[StockItemTitle]**](StockItemTitle.md) |  | [optional] [readonly] 
**item_channel_prices** | [**List[StockItemPrice]**](StockItemPrice.md) |  | [optional] [readonly] 
**images** | [**List[StockItemImage]**](StockItemImage.md) |  | [optional] 
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
from linnworks_api.generated.stock.models.stock_item_full import StockItemFull

# TODO update the JSON string below
json = "{}"
# create an instance of StockItemFull from a JSON string
stock_item_full_instance = StockItemFull.from_json(json)
# print the JSON string representation of the object
print(StockItemFull.to_json())

# convert the object into a dict
stock_item_full_dict = stock_item_full_instance.to_dict()
# create an instance of StockItemFull from a dict
stock_item_full_from_dict = StockItemFull.from_dict(stock_item_full_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


