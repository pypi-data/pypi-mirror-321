# GenericPagedResultStockItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_number** | **int** |  | [optional] 
**entries_per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] [readonly] 
**data** | [**List[StockItem]**](StockItem.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.generic_paged_result_stock_item import GenericPagedResultStockItem

# TODO update the JSON string below
json = "{}"
# create an instance of GenericPagedResultStockItem from a JSON string
generic_paged_result_stock_item_instance = GenericPagedResultStockItem.from_json(json)
# print the JSON string representation of the object
print(GenericPagedResultStockItem.to_json())

# convert the object into a dict
generic_paged_result_stock_item_dict = generic_paged_result_stock_item_instance.to_dict()
# create an instance of GenericPagedResultStockItem from a dict
generic_paged_result_stock_item_from_dict = GenericPagedResultStockItem.from_dict(generic_paged_result_stock_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


