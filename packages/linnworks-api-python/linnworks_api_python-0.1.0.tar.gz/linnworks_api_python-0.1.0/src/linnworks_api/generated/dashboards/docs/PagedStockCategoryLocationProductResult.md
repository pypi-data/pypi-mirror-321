# PagedStockCategoryLocationProductResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_results** | **int** |  | [optional] 
**results** | [**List[StockCategoryLocationProduct]**](StockCategoryLocationProduct.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.dashboards.models.paged_stock_category_location_product_result import PagedStockCategoryLocationProductResult

# TODO update the JSON string below
json = "{}"
# create an instance of PagedStockCategoryLocationProductResult from a JSON string
paged_stock_category_location_product_result_instance = PagedStockCategoryLocationProductResult.from_json(json)
# print the JSON string representation of the object
print(PagedStockCategoryLocationProductResult.to_json())

# convert the object into a dict
paged_stock_category_location_product_result_dict = paged_stock_category_location_product_result_instance.to_dict()
# create an instance of PagedStockCategoryLocationProductResult from a dict
paged_stock_category_location_product_result_from_dict = PagedStockCategoryLocationProductResult.from_dict(paged_stock_category_location_product_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


