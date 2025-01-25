# StockCategoryLocationProduct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_number** | **str** |  | [optional] 
**item_title** | **str** |  | [optional] 
**stock_level** | **int** |  | [optional] 
**stock_value** | **float** |  | [optional] 

## Example

```python
from linnworks_api.generated.dashboards.models.stock_category_location_product import StockCategoryLocationProduct

# TODO update the JSON string below
json = "{}"
# create an instance of StockCategoryLocationProduct from a JSON string
stock_category_location_product_instance = StockCategoryLocationProduct.from_json(json)
# print the JSON string representation of the object
print(StockCategoryLocationProduct.to_json())

# convert the object into a dict
stock_category_location_product_dict = stock_category_location_product_instance.to_dict()
# create an instance of StockCategoryLocationProduct from a dict
stock_category_location_product_from_dict = StockCategoryLocationProduct.from_dict(stock_category_location_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


