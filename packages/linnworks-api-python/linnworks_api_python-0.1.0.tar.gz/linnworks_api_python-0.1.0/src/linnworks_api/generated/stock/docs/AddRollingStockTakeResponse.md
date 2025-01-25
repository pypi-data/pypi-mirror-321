# AddRollingStockTakeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errored_items** | [**List[StockTakeItemWithError]**](StockTakeItemWithError.md) | List of items that have failed validation, if any items are returned then the stock take won&#39;t be submitted. | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.add_rolling_stock_take_response import AddRollingStockTakeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddRollingStockTakeResponse from a JSON string
add_rolling_stock_take_response_instance = AddRollingStockTakeResponse.from_json(json)
# print the JSON string representation of the object
print(AddRollingStockTakeResponse.to_json())

# convert the object into a dict
add_rolling_stock_take_response_dict = add_rolling_stock_take_response_instance.to_dict()
# create an instance of AddRollingStockTakeResponse from a dict
add_rolling_stock_take_response_from_dict = AddRollingStockTakeResponse.from_dict(add_rolling_stock_take_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


