# AddRollingStockTakeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_id** | **str** | Location Id | [optional] 
**session_duriation_seconds** | **int** | Time in seconds the stock take session has taken | [optional] 
**items** | [**List[StockTakeItem]**](StockTakeItem.md) | List of stock take items. Maximum 1000 items in a stock take session | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.add_rolling_stock_take_request import AddRollingStockTakeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddRollingStockTakeRequest from a JSON string
add_rolling_stock_take_request_instance = AddRollingStockTakeRequest.from_json(json)
# print the JSON string representation of the object
print(AddRollingStockTakeRequest.to_json())

# convert the object into a dict
add_rolling_stock_take_request_dict = add_rolling_stock_take_request_instance.to_dict()
# create an instance of AddRollingStockTakeRequest from a dict
add_rolling_stock_take_request_from_dict = AddRollingStockTakeRequest.from_dict(add_rolling_stock_take_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


