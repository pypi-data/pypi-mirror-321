# StockItemPricingRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_row_id** | **int** |  | [optional] 
**fk_stock_pricing_id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**lower_bound** | **int** |  | [optional] 
**value** | **float** |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.stock_item_pricing_rule import StockItemPricingRule

# TODO update the JSON string below
json = "{}"
# create an instance of StockItemPricingRule from a JSON string
stock_item_pricing_rule_instance = StockItemPricingRule.from_json(json)
# print the JSON string representation of the object
print(StockItemPricingRule.to_json())

# convert the object into a dict
stock_item_pricing_rule_dict = stock_item_pricing_rule_instance.to_dict()
# create an instance of StockItemPricingRule from a dict
stock_item_pricing_rule_from_dict = StockItemPricingRule.from_dict(stock_item_pricing_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


