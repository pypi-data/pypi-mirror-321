# StockItemTitle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_row_id** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**sub_source** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**stock_item_id** | **str** |  | [optional] 
**stock_item_int_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.stock_item_title import StockItemTitle

# TODO update the JSON string below
json = "{}"
# create an instance of StockItemTitle from a JSON string
stock_item_title_instance = StockItemTitle.from_json(json)
# print the JSON string representation of the object
print(StockItemTitle.to_json())

# convert the object into a dict
stock_item_title_dict = stock_item_title_instance.to_dict()
# create an instance of StockItemTitle from a dict
stock_item_title_from_dict = StockItemTitle.from_dict(stock_item_title_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


