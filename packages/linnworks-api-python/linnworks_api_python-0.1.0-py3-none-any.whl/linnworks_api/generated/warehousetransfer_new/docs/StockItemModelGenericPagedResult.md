# StockItemModelGenericPagedResult

Order item object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_number** | **int** | Result page number | [optional] 
**entries_per_page** | **int** | Result page size, quantity of records per page | [optional] 
**total_entries** | **int** | Total records | [optional] 
**total_pages** | **int** | Total pages | [optional] [readonly] 
**data** | [**List[StockItemModel]**](StockItemModel.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.stock_item_model_generic_paged_result import StockItemModelGenericPagedResult

# TODO update the JSON string below
json = "{}"
# create an instance of StockItemModelGenericPagedResult from a JSON string
stock_item_model_generic_paged_result_instance = StockItemModelGenericPagedResult.from_json(json)
# print the JSON string representation of the object
print(StockItemModelGenericPagedResult.to_json())

# convert the object into a dict
stock_item_model_generic_paged_result_dict = stock_item_model_generic_paged_result_instance.to_dict()
# create an instance of StockItemModelGenericPagedResult from a dict
stock_item_model_generic_paged_result_from_dict = StockItemModelGenericPagedResult.from_dict(stock_item_model_generic_paged_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


