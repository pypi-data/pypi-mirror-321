# BookInStockItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_item_id** | **str** |  | [optional] 
**location_id** | **str** |  | [optional] 
**quantity_received** | **int** |  | [optional] 
**cost_per_unit** | **float** |  | [optional] 
**bin_rack** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.book_in_stock_item import BookInStockItem

# TODO update the JSON string below
json = "{}"
# create an instance of BookInStockItem from a JSON string
book_in_stock_item_instance = BookInStockItem.from_json(json)
# print the JSON string representation of the object
print(BookInStockItem.to_json())

# convert the object into a dict
book_in_stock_item_dict = book_in_stock_item_instance.to_dict()
# create an instance of BookInStockItem from a dict
book_in_stock_item_from_dict = BookInStockItem.from_dict(book_in_stock_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


