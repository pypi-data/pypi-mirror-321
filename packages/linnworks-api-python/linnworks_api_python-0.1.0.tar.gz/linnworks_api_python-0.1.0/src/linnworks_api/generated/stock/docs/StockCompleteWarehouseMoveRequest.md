# StockCompleteWarehouseMoveRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**WarehouseMoveCompleteRequest**](WarehouseMoveCompleteRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.stock_complete_warehouse_move_request import StockCompleteWarehouseMoveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StockCompleteWarehouseMoveRequest from a JSON string
stock_complete_warehouse_move_request_instance = StockCompleteWarehouseMoveRequest.from_json(json)
# print the JSON string representation of the object
print(StockCompleteWarehouseMoveRequest.to_json())

# convert the object into a dict
stock_complete_warehouse_move_request_dict = stock_complete_warehouse_move_request_instance.to_dict()
# create an instance of StockCompleteWarehouseMoveRequest from a dict
stock_complete_warehouse_move_request_from_dict = StockCompleteWarehouseMoveRequest.from_dict(stock_complete_warehouse_move_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


