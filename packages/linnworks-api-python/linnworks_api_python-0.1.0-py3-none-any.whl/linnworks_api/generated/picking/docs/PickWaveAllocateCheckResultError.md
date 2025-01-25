# PickWaveAllocateCheckResultError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | [optional] 
**error_type** | **str** |  | [optional] 
**order_item_row_id** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.picking.models.pick_wave_allocate_check_result_error import PickWaveAllocateCheckResultError

# TODO update the JSON string below
json = "{}"
# create an instance of PickWaveAllocateCheckResultError from a JSON string
pick_wave_allocate_check_result_error_instance = PickWaveAllocateCheckResultError.from_json(json)
# print the JSON string representation of the object
print(PickWaveAllocateCheckResultError.to_json())

# convert the object into a dict
pick_wave_allocate_check_result_error_dict = pick_wave_allocate_check_result_error_instance.to_dict()
# create an instance of PickWaveAllocateCheckResultError from a dict
pick_wave_allocate_check_result_error_from_dict = PickWaveAllocateCheckResultError.from_dict(pick_wave_allocate_check_result_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


