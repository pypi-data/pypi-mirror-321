# BatchStockLevelDetaRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_level_deltas** | [**List[BatchStockLevelDelta]**](BatchStockLevelDelta.md) |  | [optional] 
**stock_location_id** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.batch_stock_level_deta_request import BatchStockLevelDetaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BatchStockLevelDetaRequest from a JSON string
batch_stock_level_deta_request_instance = BatchStockLevelDetaRequest.from_json(json)
# print the JSON string representation of the object
print(BatchStockLevelDetaRequest.to_json())

# convert the object into a dict
batch_stock_level_deta_request_dict = batch_stock_level_deta_request_instance.to_dict()
# create an instance of BatchStockLevelDetaRequest from a dict
batch_stock_level_deta_request_from_dict = BatchStockLevelDetaRequest.from_dict(batch_stock_level_deta_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


