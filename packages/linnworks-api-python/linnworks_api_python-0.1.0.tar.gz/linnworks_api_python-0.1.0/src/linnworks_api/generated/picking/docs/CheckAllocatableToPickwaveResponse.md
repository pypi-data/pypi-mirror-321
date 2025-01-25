# CheckAllocatableToPickwaveResponse

Check allocatable to pickwave response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[PickWaveAllocateCheckResult]**](PickWaveAllocateCheckResult.md) | List of results | [optional] 

## Example

```python
from linnworks_api.generated.picking.models.check_allocatable_to_pickwave_response import CheckAllocatableToPickwaveResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CheckAllocatableToPickwaveResponse from a JSON string
check_allocatable_to_pickwave_response_instance = CheckAllocatableToPickwaveResponse.from_json(json)
# print the JSON string representation of the object
print(CheckAllocatableToPickwaveResponse.to_json())

# convert the object into a dict
check_allocatable_to_pickwave_response_dict = check_allocatable_to_pickwave_response_instance.to_dict()
# create an instance of CheckAllocatableToPickwaveResponse from a dict
check_allocatable_to_pickwave_response_from_dict = CheckAllocatableToPickwaveResponse.from_dict(check_allocatable_to_pickwave_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


