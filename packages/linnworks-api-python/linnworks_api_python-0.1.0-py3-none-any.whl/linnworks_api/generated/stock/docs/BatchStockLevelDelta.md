# BatchStockLevelDelta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sku** | **str** |  | [optional] 
**batch_number** | **str** |  | [optional] 
**bin_rack** | **str** |  | [optional] 
**delta_quantity** | **int** |  | [optional] 
**reason** | **str** |  | [optional] 
**pk_batch_inventory_id** | **int** |  | [optional] [readonly] 
**quantity** | **int** |  | [optional] [readonly] 
**stock_value** | **float** |  | [optional] [readonly] 
**errors** | **List[str]** |  | [optional] 
**new_level** | **int** |  | [optional] [readonly] 
**batch_status** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.batch_stock_level_delta import BatchStockLevelDelta

# TODO update the JSON string below
json = "{}"
# create an instance of BatchStockLevelDelta from a JSON string
batch_stock_level_delta_instance = BatchStockLevelDelta.from_json(json)
# print the JSON string representation of the object
print(BatchStockLevelDelta.to_json())

# convert the object into a dict
batch_stock_level_delta_dict = batch_stock_level_delta_instance.to_dict()
# create an instance of BatchStockLevelDelta from a dict
batch_stock_level_delta_from_dict = BatchStockLevelDelta.from_dict(batch_stock_level_delta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


