# BatchedAPIResponseGuid


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[APIResultResponseGuid]**](APIResultResponseGuid.md) |  | [optional] 
**total_results** | **int** |  | [optional] [readonly] 
**result_status** | **str** |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.inventory.models.batched_api_response_guid import BatchedAPIResponseGuid

# TODO update the JSON string below
json = "{}"
# create an instance of BatchedAPIResponseGuid from a JSON string
batched_api_response_guid_instance = BatchedAPIResponseGuid.from_json(json)
# print the JSON string representation of the object
print(BatchedAPIResponseGuid.to_json())

# convert the object into a dict
batched_api_response_guid_dict = batched_api_response_guid_instance.to_dict()
# create an instance of BatchedAPIResponseGuid from a dict
batched_api_response_guid_from_dict = BatchedAPIResponseGuid.from_dict(batched_api_response_guid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


