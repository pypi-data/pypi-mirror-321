# GenericPagedResultStockItemChangeHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_number** | **int** |  | [optional] 
**entries_per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] [readonly] 
**data** | [**List[StockItemChangeHistory]**](StockItemChangeHistory.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.generic_paged_result_stock_item_change_history import GenericPagedResultStockItemChangeHistory

# TODO update the JSON string below
json = "{}"
# create an instance of GenericPagedResultStockItemChangeHistory from a JSON string
generic_paged_result_stock_item_change_history_instance = GenericPagedResultStockItemChangeHistory.from_json(json)
# print the JSON string representation of the object
print(GenericPagedResultStockItemChangeHistory.to_json())

# convert the object into a dict
generic_paged_result_stock_item_change_history_dict = generic_paged_result_stock_item_change_history_instance.to_dict()
# create an instance of GenericPagedResultStockItemChangeHistory from a dict
generic_paged_result_stock_item_change_history_from_dict = GenericPagedResultStockItemChangeHistory.from_dict(generic_paged_result_stock_item_change_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


