# BatchDatesUpdateItemResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **List[str]** |  | [optional] 
**has_error** | **bool** |  | [optional] [readonly] 
**row_index** | **int** |  | [optional] 
**batch_number** | **str** |  | [optional] 
**sell_by** | **datetime** |  | [optional] 
**expiry** | **datetime** |  | [optional] 
**sku** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.batch_dates_update_item_result import BatchDatesUpdateItemResult

# TODO update the JSON string below
json = "{}"
# create an instance of BatchDatesUpdateItemResult from a JSON string
batch_dates_update_item_result_instance = BatchDatesUpdateItemResult.from_json(json)
# print the JSON string representation of the object
print(BatchDatesUpdateItemResult.to_json())

# convert the object into a dict
batch_dates_update_item_result_dict = batch_dates_update_item_result_instance.to_dict()
# create an instance of BatchDatesUpdateItemResult from a dict
batch_dates_update_item_result_from_dict = BatchDatesUpdateItemResult.from_dict(batch_dates_update_item_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


