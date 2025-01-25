# SearchStockByKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Item ID | [optional] 
**location_id** | **str** | Location ID | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.search_stock_by_key import SearchStockByKey

# TODO update the JSON string below
json = "{}"
# create an instance of SearchStockByKey from a JSON string
search_stock_by_key_instance = SearchStockByKey.from_json(json)
# print the JSON string representation of the object
print(SearchStockByKey.to_json())

# convert the object into a dict
search_stock_by_key_dict = search_stock_by_key_instance.to_dict()
# create an instance of SearchStockByKey from a dict
search_stock_by_key_from_dict = SearchStockByKey.from_dict(search_stock_by_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


