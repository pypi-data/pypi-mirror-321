# StockItemReturn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** |  | [optional] 
**month** | **int** |  | [optional] 
**reason** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**stock_item_id** | **str** |  | [optional] 
**stock_item_int_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.stock_item_return import StockItemReturn

# TODO update the JSON string below
json = "{}"
# create an instance of StockItemReturn from a JSON string
stock_item_return_instance = StockItemReturn.from_json(json)
# print the JSON string representation of the object
print(StockItemReturn.to_json())

# convert the object into a dict
stock_item_return_dict = stock_item_return_instance.to_dict()
# create an instance of StockItemReturn from a dict
stock_item_return_from_dict = StockItemReturn.from_dict(stock_item_return_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


