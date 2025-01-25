# GetStockItemBatchesByLocationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batches** | [**List[StockItemBatch]**](StockItemBatch.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.get_stock_item_batches_by_location_response import GetStockItemBatchesByLocationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetStockItemBatchesByLocationResponse from a JSON string
get_stock_item_batches_by_location_response_instance = GetStockItemBatchesByLocationResponse.from_json(json)
# print the JSON string representation of the object
print(GetStockItemBatchesByLocationResponse.to_json())

# convert the object into a dict
get_stock_item_batches_by_location_response_dict = get_stock_item_batches_by_location_response_instance.to_dict()
# create an instance of GetStockItemBatchesByLocationResponse from a dict
get_stock_item_batches_by_location_response_from_dict = GetStockItemBatchesByLocationResponse.from_dict(get_stock_item_batches_by_location_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


