# StatsStockItemLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_location_id** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**stock_level** | **float** |  | [optional] 
**stock_value** | **float** |  | [optional] 

## Example

```python
from linnworks_api.generated.dashboards.models.stats_stock_item_location import StatsStockItemLocation

# TODO update the JSON string below
json = "{}"
# create an instance of StatsStockItemLocation from a JSON string
stats_stock_item_location_instance = StatsStockItemLocation.from_json(json)
# print the JSON string representation of the object
print(StatsStockItemLocation.to_json())

# convert the object into a dict
stats_stock_item_location_dict = stats_stock_item_location_instance.to_dict()
# create an instance of StatsStockItemLocation from a dict
stats_stock_item_location_from_dict = StatsStockItemLocation.from_dict(stats_stock_item_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


