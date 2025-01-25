# StockConsumption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** |  | [optional] 
**stock_quantity** | **int** |  | [optional] 
**stock_value** | **float** |  | [optional] 
**shipped** | **int** |  | [optional] 
**stock_item_id** | **str** |  | [optional] 
**stock_item_int_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.stock_consumption import StockConsumption

# TODO update the JSON string below
json = "{}"
# create an instance of StockConsumption from a JSON string
stock_consumption_instance = StockConsumption.from_json(json)
# print the JSON string representation of the object
print(StockConsumption.to_json())

# convert the object into a dict
stock_consumption_dict = stock_consumption_instance.to_dict()
# create an instance of StockConsumption from a dict
stock_consumption_from_dict = StockConsumption.from_dict(stock_consumption_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


