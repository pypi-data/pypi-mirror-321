# StockItemInfo

Basic stock item information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sku** | **str** | Item SKU | [optional] 
**stock_item_id** | **str** | Item unique id | [optional] 
**item_title** | **str** | Item Title | [optional] 
**barcode** | **str** | Barcode number on the item header | [optional] 
**primary_image_url** | **str** | Image URL | [optional] 
**identifiers** | [**List[StockItemIdentifier]**](StockItemIdentifier.md) | Product identifiers | [optional] 

## Example

```python
from linnworks_api.generated.picking.models.stock_item_info import StockItemInfo

# TODO update the JSON string below
json = "{}"
# create an instance of StockItemInfo from a JSON string
stock_item_info_instance = StockItemInfo.from_json(json)
# print the JSON string representation of the object
print(StockItemInfo.to_json())

# convert the object into a dict
stock_item_info_dict = stock_item_info_instance.to_dict()
# create an instance of StockItemInfo from a dict
stock_item_info_from_dict = StockItemInfo.from_dict(stock_item_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


