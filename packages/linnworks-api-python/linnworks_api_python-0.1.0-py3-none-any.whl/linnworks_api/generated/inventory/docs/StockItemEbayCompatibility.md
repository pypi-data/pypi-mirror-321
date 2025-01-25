# StockItemEbayCompatibility


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fk_stock_item_id** | **str** |  | [optional] 
**fk_compatibility_list_id** | **str** |  | [optional] 
**sku** | **str** |  | [optional] 
**compatibility_notes** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**include_years** | **str** |  | [optional] 
**exclude_years** | **str** |  | [optional] 
**culture** | **str** |  | [optional] 
**ebay_compitibility_type** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.stock_item_ebay_compatibility import StockItemEbayCompatibility

# TODO update the JSON string below
json = "{}"
# create an instance of StockItemEbayCompatibility from a JSON string
stock_item_ebay_compatibility_instance = StockItemEbayCompatibility.from_json(json)
# print the JSON string representation of the object
print(StockItemEbayCompatibility.to_json())

# convert the object into a dict
stock_item_ebay_compatibility_dict = stock_item_ebay_compatibility_instance.to_dict()
# create an instance of StockItemEbayCompatibility from a dict
stock_item_ebay_compatibility_from_dict = StockItemEbayCompatibility.from_dict(stock_item_ebay_compatibility_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


