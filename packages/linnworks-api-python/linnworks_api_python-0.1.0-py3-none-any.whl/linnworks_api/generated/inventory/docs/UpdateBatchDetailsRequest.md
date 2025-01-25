# UpdateBatchDetailsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_item_id** | **str** |  | [optional] 
**inventory_tracking_type** | **int** |  | [optional] 
**batch_number_scan_required** | **bool** |  | [optional] 
**reset_batch_dates** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.update_batch_details_request import UpdateBatchDetailsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateBatchDetailsRequest from a JSON string
update_batch_details_request_instance = UpdateBatchDetailsRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateBatchDetailsRequest.to_json())

# convert the object into a dict
update_batch_details_request_dict = update_batch_details_request_instance.to_dict()
# create an instance of UpdateBatchDetailsRequest from a dict
update_batch_details_request_from_dict = UpdateBatchDetailsRequest.from_dict(update_batch_details_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


