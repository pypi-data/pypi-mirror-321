# LowStockLevel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_title** | **str** |  | [optional] 
**item_number** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**minimum_level** | **int** |  | [optional] 
**in_books** | **int** |  | [optional] 
**location** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.dashboards.models.low_stock_level import LowStockLevel

# TODO update the JSON string below
json = "{}"
# create an instance of LowStockLevel from a JSON string
low_stock_level_instance = LowStockLevel.from_json(json)
# print the JSON string representation of the object
print(LowStockLevel.to_json())

# convert the object into a dict
low_stock_level_dict = low_stock_level_instance.to_dict()
# create an instance of LowStockLevel from a dict
low_stock_level_from_dict = LowStockLevel.from_dict(low_stock_level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


