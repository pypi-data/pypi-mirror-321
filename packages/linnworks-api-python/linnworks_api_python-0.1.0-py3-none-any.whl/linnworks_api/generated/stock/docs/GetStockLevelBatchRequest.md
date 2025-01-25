# GetStockLevelBatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_item_ids** | **List[str]** | List of stock item ids to get stock level | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.get_stock_level_batch_request import GetStockLevelBatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetStockLevelBatchRequest from a JSON string
get_stock_level_batch_request_instance = GetStockLevelBatchRequest.from_json(json)
# print the JSON string representation of the object
print(GetStockLevelBatchRequest.to_json())

# convert the object into a dict
get_stock_level_batch_request_dict = get_stock_level_batch_request_instance.to_dict()
# create an instance of GetStockLevelBatchRequest from a dict
get_stock_level_batch_request_from_dict = GetStockLevelBatchRequest.from_dict(get_stock_level_batch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


