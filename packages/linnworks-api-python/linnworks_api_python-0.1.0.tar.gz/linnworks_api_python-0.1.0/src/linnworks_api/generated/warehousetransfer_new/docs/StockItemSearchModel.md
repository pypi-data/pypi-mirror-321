# StockItemSearchModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**barcode_number** | **str** |  | [optional] 
**item_number** | **str** |  | [optional] 
**item_title** | **str** |  | [optional] 
**seller_sku** | **str** |  | [optional] 
**asin** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.stock_item_search_model import StockItemSearchModel

# TODO update the JSON string below
json = "{}"
# create an instance of StockItemSearchModel from a JSON string
stock_item_search_model_instance = StockItemSearchModel.from_json(json)
# print the JSON string representation of the object
print(StockItemSearchModel.to_json())

# convert the object into a dict
stock_item_search_model_dict = stock_item_search_model_instance.to_dict()
# create an instance of StockItemSearchModel from a dict
stock_item_search_model_from_dict = StockItemSearchModel.from_dict(stock_item_search_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


