# PickWaveAllocateCheckResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sort_order** | **int** |  | [optional] 
**order_id** | **int** |  | [optional] 
**order_id_guid** | **str** |  | [optional] 
**errors** | [**List[PickWaveAllocateCheckResultError]**](PickWaveAllocateCheckResultError.md) |  | [optional] 
**has_errors** | **bool** |  | [optional] [readonly] 
**order_details** | [**List[PickWaveAllocateCheckResultOrderDetails]**](PickWaveAllocateCheckResultOrderDetails.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.picking.models.pick_wave_allocate_check_result import PickWaveAllocateCheckResult

# TODO update the JSON string below
json = "{}"
# create an instance of PickWaveAllocateCheckResult from a JSON string
pick_wave_allocate_check_result_instance = PickWaveAllocateCheckResult.from_json(json)
# print the JSON string representation of the object
print(PickWaveAllocateCheckResult.to_json())

# convert the object into a dict
pick_wave_allocate_check_result_dict = pick_wave_allocate_check_result_instance.to_dict()
# create an instance of PickWaveAllocateCheckResult from a dict
pick_wave_allocate_check_result_from_dict = PickWaveAllocateCheckResult.from_dict(pick_wave_allocate_check_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


