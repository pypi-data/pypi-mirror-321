# AssignedOptionSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**mapped_from_bc** | **bool** |  | [optional] 
**options** | [**List[AssignedOption]**](AssignedOption.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.assigned_option_set import AssignedOptionSet

# TODO update the JSON string below
json = "{}"
# create an instance of AssignedOptionSet from a JSON string
assigned_option_set_instance = AssignedOptionSet.from_json(json)
# print the JSON string representation of the object
print(AssignedOptionSet.to_json())

# convert the object into a dict
assigned_option_set_dict = assigned_option_set_instance.to_dict()
# create an instance of AssignedOptionSet from a dict
assigned_option_set_from_dict = AssignedOptionSet.from_dict(assigned_option_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


