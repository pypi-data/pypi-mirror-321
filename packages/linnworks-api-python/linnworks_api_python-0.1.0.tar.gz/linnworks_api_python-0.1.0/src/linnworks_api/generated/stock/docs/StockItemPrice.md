# StockItemPrice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rules** | [**List[StockItemPricingRule]**](StockItemPricingRule.md) |  | [optional] 
**pk_row_id** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**sub_source** | **str** |  | [optional] 
**price** | **float** |  | [optional] 
**tag** | **str** |  | [optional] 
**update_status** | **str** |  | [optional] 
**stock_item_id** | **str** |  | [optional] 
**stock_item_int_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.stock_item_price import StockItemPrice

# TODO update the JSON string below
json = "{}"
# create an instance of StockItemPrice from a JSON string
stock_item_price_instance = StockItemPrice.from_json(json)
# print the JSON string representation of the object
print(StockItemPrice.to_json())

# convert the object into a dict
stock_item_price_dict = stock_item_price_instance.to_dict()
# create an instance of StockItemPrice from a dict
stock_item_price_from_dict = StockItemPrice.from_dict(stock_item_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


