# CheckAllocatableToPickwaveRequest

Request for allocatioable orders to pickwave.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_ids** | **List[int]** | List of integer order ids | [optional] 

## Example

```python
from linnworks_api.generated.picking.models.check_allocatable_to_pickwave_request import CheckAllocatableToPickwaveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CheckAllocatableToPickwaveRequest from a JSON string
check_allocatable_to_pickwave_request_instance = CheckAllocatableToPickwaveRequest.from_json(json)
# print the JSON string representation of the object
print(CheckAllocatableToPickwaveRequest.to_json())

# convert the object into a dict
check_allocatable_to_pickwave_request_dict = check_allocatable_to_pickwave_request_instance.to_dict()
# create an instance of CheckAllocatableToPickwaveRequest from a dict
check_allocatable_to_pickwave_request_from_dict = CheckAllocatableToPickwaveRequest.from_dict(check_allocatable_to_pickwave_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


