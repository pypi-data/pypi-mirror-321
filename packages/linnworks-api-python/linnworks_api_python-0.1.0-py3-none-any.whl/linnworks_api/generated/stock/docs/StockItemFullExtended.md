# StockItemFullExtended


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_channel_descriptions** | [**List[StockItemDescription]**](StockItemDescription.md) |  | [optional] 
**item_extended_properties** | [**List[StockItemExtendedProperty]**](StockItemExtendedProperty.md) |  | [optional] 
**item_channel_titles** | [**List[StockItemTitle]**](StockItemTitle.md) |  | [optional] 
**item_channel_prices** | [**List[StockItemPrice]**](StockItemPrice.md) |  | [optional] 
**suppliers** | [**List[StockItemSupplierStat]**](StockItemSupplierStat.md) |  | [optional] 
**stock_levels** | [**List[StockItemLevel]**](StockItemLevel.md) |  | [optional] 
**images** | [**List[StockItemImage]**](StockItemImage.md) |  | [optional] 
**item_number** | **str** |  | [optional] 
**item_title** | **str** |  | [optional] 
**barcode_number** | **str** |  | [optional] 
**meta_data** | **str** |  | [optional] 
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
**is_composite_parent** | **bool** |  | [optional] 
**inventory_tracking_type** | **int** |  | [optional] 
**batch_number_scan_required** | **bool** |  | [optional] 
**serial_number_scan_required** | **bool** |  | [optional] 
**stock_item_id** | **str** |  | [optional] 
**stock_item_int_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.stock_item_full_extended import StockItemFullExtended

# TODO update the JSON string below
json = "{}"
# create an instance of StockItemFullExtended from a JSON string
stock_item_full_extended_instance = StockItemFullExtended.from_json(json)
# print the JSON string representation of the object
print(StockItemFullExtended.to_json())

# convert the object into a dict
stock_item_full_extended_dict = stock_item_full_extended_instance.to_dict()
# create an instance of StockItemFullExtended from a dict
stock_item_full_extended_from_dict = StockItemFullExtended.from_dict(stock_item_full_extended_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


