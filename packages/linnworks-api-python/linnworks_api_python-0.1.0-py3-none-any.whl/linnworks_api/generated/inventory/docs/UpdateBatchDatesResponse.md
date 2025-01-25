# UpdateBatchDatesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[BatchDatesUpdateItemResult]**](BatchDatesUpdateItemResult.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.update_batch_dates_response import UpdateBatchDatesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateBatchDatesResponse from a JSON string
update_batch_dates_response_instance = UpdateBatchDatesResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateBatchDatesResponse.to_json())

# convert the object into a dict
update_batch_dates_response_dict = update_batch_dates_response_instance.to_dict()
# create an instance of UpdateBatchDatesResponse from a dict
update_batch_dates_response_from_dict = UpdateBatchDatesResponse.from_dict(update_batch_dates_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


