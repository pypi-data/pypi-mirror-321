# GetStockItemsFullByIdsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_items_full_extended** | [**List[StockItemFullExtended]**](StockItemFullExtended.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.get_stock_items_full_by_ids_response import GetStockItemsFullByIdsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetStockItemsFullByIdsResponse from a JSON string
get_stock_items_full_by_ids_response_instance = GetStockItemsFullByIdsResponse.from_json(json)
# print the JSON string representation of the object
print(GetStockItemsFullByIdsResponse.to_json())

# convert the object into a dict
get_stock_items_full_by_ids_response_dict = get_stock_items_full_by_ids_response_instance.to_dict()
# create an instance of GetStockItemsFullByIdsResponse from a dict
get_stock_items_full_by_ids_response_from_dict = GetStockItemsFullByIdsResponse.from_dict(get_stock_items_full_by_ids_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


