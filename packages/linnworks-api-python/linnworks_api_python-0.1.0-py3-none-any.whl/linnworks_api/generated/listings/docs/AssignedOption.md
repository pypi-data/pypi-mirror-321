# AssignedOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_v3** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**values** | [**List[OptionValue]**](OptionValue.md) |  | [optional] 
**option_display_name** | **str** |  | [optional] 
**option_name** | **str** |  | [optional] 
**mapped_from_bc** | **bool** |  | [optional] 
**assignment_id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.assigned_option import AssignedOption

# TODO update the JSON string below
json = "{}"
# create an instance of AssignedOption from a JSON string
assigned_option_instance = AssignedOption.from_json(json)
# print the JSON string representation of the object
print(AssignedOption.to_json())

# convert the object into a dict
assigned_option_dict = assigned_option_instance.to_dict()
# create an instance of AssignedOption from a dict
assigned_option_from_dict = AssignedOption.from_dict(assigned_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


