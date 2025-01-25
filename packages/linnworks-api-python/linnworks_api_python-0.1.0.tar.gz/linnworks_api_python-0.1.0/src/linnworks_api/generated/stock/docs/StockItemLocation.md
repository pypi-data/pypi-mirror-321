# StockItemLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_location_id** | **str** |  | [optional] 
**location_name** | **str** |  | [optional] 
**bin_rack** | **str** |  | [optional] 
**stock_item_id** | **str** |  | [optional] 
**stock_item_int_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.stock_item_location import StockItemLocation

# TODO update the JSON string below
json = "{}"
# create an instance of StockItemLocation from a JSON string
stock_item_location_instance = StockItemLocation.from_json(json)
# print the JSON string representation of the object
print(StockItemLocation.to_json())

# convert the object into a dict
stock_item_location_dict = stock_item_location_instance.to_dict()
# create an instance of StockItemLocation from a dict
stock_item_location_from_dict = StockItemLocation.from_dict(stock_item_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


