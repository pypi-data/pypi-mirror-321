# BatchActionResultInt32Int32


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**processed_orders** | **List[int]** |  | [optional] 
**unprocessed_orders** | **Dict[str, List[int]]** |  | [optional] 

## Example

```python
from linnworks_api.generated.openorders.models.batch_action_result_int32_int32 import BatchActionResultInt32Int32

# TODO update the JSON string below
json = "{}"
# create an instance of BatchActionResultInt32Int32 from a JSON string
batch_action_result_int32_int32_instance = BatchActionResultInt32Int32.from_json(json)
# print the JSON string representation of the object
print(BatchActionResultInt32Int32.to_json())

# convert the object into a dict
batch_action_result_int32_int32_dict = batch_action_result_int32_int32_instance.to_dict()
# create an instance of BatchActionResultInt32Int32 from a dict
batch_action_result_int32_int32_from_dict = BatchActionResultInt32Int32.from_dict(batch_action_result_int32_int32_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


