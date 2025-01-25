# GetStockItemsByIdsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[StockItemHeader]**](StockItemHeader.md) | List of stock item headers. | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.get_stock_items_by_ids_response import GetStockItemsByIdsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetStockItemsByIdsResponse from a JSON string
get_stock_items_by_ids_response_instance = GetStockItemsByIdsResponse.from_json(json)
# print the JSON string representation of the object
print(GetStockItemsByIdsResponse.to_json())

# convert the object into a dict
get_stock_items_by_ids_response_dict = get_stock_items_by_ids_response_instance.to_dict()
# create an instance of GetStockItemsByIdsResponse from a dict
get_stock_items_by_ids_response_from_dict = GetStockItemsByIdsResponse.from_dict(get_stock_items_by_ids_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


