# StockCategoryLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_location_id** | **str** |  | [optional] 
**category_name** | **str** |  | [optional] 
**category_id** | **str** |  | [optional] 
**stock_level** | **int** |  | [optional] 
**stock_value** | **float** |  | [optional] 

## Example

```python
from linnworks_api.generated.dashboards.models.stock_category_location import StockCategoryLocation

# TODO update the JSON string below
json = "{}"
# create an instance of StockCategoryLocation from a JSON string
stock_category_location_instance = StockCategoryLocation.from_json(json)
# print the JSON string representation of the object
print(StockCategoryLocation.to_json())

# convert the object into a dict
stock_category_location_dict = stock_category_location_instance.to_dict()
# create an instance of StockCategoryLocation from a dict
stock_category_location_from_dict = StockCategoryLocation.from_dict(stock_category_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


