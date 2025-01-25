# StockItemModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_item_id** | **str** | Stock Item Guid | [optional] 
**stock_item_int_id** | **int** | Stock Item integer Id | [optional] 
**asin** | **str** |  | [optional] 
**seller_sku** | **str** |  | [optional] 
**thumbnail_source** | **str** |  | [optional] 
**item_number** | **str** | SKU | [optional] 
**item_title** | **str** | Item title | [optional] 
**condition** | **str** |  | [optional] 
**fba_total_stock** | **int** |  | [optional] 
**quantity** | **int** | Quantity in stock | [optional] 
**in_order_book** | **int** | Quantity in order book | [optional] 
**available** | **int** | Available level. Quantity - InOrder,&lt;br&gt;Its used in Stock Finder UI | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.stock_item_model import StockItemModel

# TODO update the JSON string below
json = "{}"
# create an instance of StockItemModel from a JSON string
stock_item_model_instance = StockItemModel.from_json(json)
# print the JSON string representation of the object
print(StockItemModel.to_json())

# convert the object into a dict
stock_item_model_dict = stock_item_model_instance.to_dict()
# create an instance of StockItemModel from a dict
stock_item_model_from_dict = StockItemModel.from_dict(stock_item_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


