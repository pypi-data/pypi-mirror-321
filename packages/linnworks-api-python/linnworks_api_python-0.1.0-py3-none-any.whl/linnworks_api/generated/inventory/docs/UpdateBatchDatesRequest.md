# UpdateBatchDatesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[BatchDatesUpdateItem]**](BatchDatesUpdateItem.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.update_batch_dates_request import UpdateBatchDatesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateBatchDatesRequest from a JSON string
update_batch_dates_request_instance = UpdateBatchDatesRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateBatchDatesRequest.to_json())

# convert the object into a dict
update_batch_dates_request_dict = update_batch_dates_request_instance.to_dict()
# create an instance of UpdateBatchDatesRequest from a dict
update_batch_dates_request_from_dict = UpdateBatchDatesRequest.from_dict(update_batch_dates_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


