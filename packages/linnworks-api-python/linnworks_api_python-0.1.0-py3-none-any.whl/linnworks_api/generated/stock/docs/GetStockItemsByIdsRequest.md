# GetStockItemsByIdsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_item_ids** | **List[str]** | Collection of Stock item id (uniqueidentifier) | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.get_stock_items_by_ids_request import GetStockItemsByIdsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetStockItemsByIdsRequest from a JSON string
get_stock_items_by_ids_request_instance = GetStockItemsByIdsRequest.from_json(json)
# print the JSON string representation of the object
print(GetStockItemsByIdsRequest.to_json())

# convert the object into a dict
get_stock_items_by_ids_request_dict = get_stock_items_by_ids_request_instance.to_dict()
# create an instance of GetStockItemsByIdsRequest from a dict
get_stock_items_by_ids_request_from_dict = GetStockItemsByIdsRequest.from_dict(get_stock_items_by_ids_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


