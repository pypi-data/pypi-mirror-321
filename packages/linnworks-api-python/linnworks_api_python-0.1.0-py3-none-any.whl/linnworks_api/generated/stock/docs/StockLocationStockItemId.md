# StockLocationStockItemId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_item_id** | **str** |  | [optional] 
**stock_location_id** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.stock_location_stock_item_id import StockLocationStockItemId

# TODO update the JSON string below
json = "{}"
# create an instance of StockLocationStockItemId from a JSON string
stock_location_stock_item_id_instance = StockLocationStockItemId.from_json(json)
# print the JSON string representation of the object
print(StockLocationStockItemId.to_json())

# convert the object into a dict
stock_location_stock_item_id_dict = stock_location_stock_item_id_instance.to_dict()
# create an instance of StockLocationStockItemId from a dict
stock_location_stock_item_id_from_dict = StockLocationStockItemId.from_dict(stock_location_stock_item_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


