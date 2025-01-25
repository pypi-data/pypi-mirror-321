# BatchStockLevelDeltaResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**processed_deltas** | [**List[BatchStockLevelDelta]**](BatchStockLevelDelta.md) |  | [optional] 
**processed_contains_errors** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.batch_stock_level_delta_response import BatchStockLevelDeltaResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BatchStockLevelDeltaResponse from a JSON string
batch_stock_level_delta_response_instance = BatchStockLevelDeltaResponse.from_json(json)
# print the JSON string representation of the object
print(BatchStockLevelDeltaResponse.to_json())

# convert the object into a dict
batch_stock_level_delta_response_dict = batch_stock_level_delta_response_instance.to_dict()
# create an instance of BatchStockLevelDeltaResponse from a dict
batch_stock_level_delta_response_from_dict = BatchStockLevelDeltaResponse.from_dict(batch_stock_level_delta_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


