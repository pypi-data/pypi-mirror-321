# ParameterInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameter_type** | **str** |  | [optional] [readonly] 
**name** | **str** |  | [optional] [readonly] 
**has_default_value** | **bool** |  | [optional] [readonly] 
**default_value** | **object** |  | [optional] [readonly] 
**raw_default_value** | **object** |  | [optional] [readonly] 
**position** | **int** |  | [optional] [readonly] 
**attributes** | **str** |  | [optional] [readonly] 
**member** | [**MemberInfo**](MemberInfo.md) |  | [optional] 
**is_in** | **bool** |  | [optional] [readonly] 
**is_out** | **bool** |  | [optional] [readonly] 
**is_lcid** | **bool** |  | [optional] [readonly] 
**is_retval** | **bool** |  | [optional] [readonly] 
**is_optional** | **bool** |  | [optional] [readonly] 
**metadata_token** | **int** |  | [optional] [readonly] 
**custom_attributes** | [**List[CustomAttributeData]**](CustomAttributeData.md) |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.inventory.models.parameter_info import ParameterInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ParameterInfo from a JSON string
parameter_info_instance = ParameterInfo.from_json(json)
# print the JSON string representation of the object
print(ParameterInfo.to_json())

# convert the object into a dict
parameter_info_dict = parameter_info_instance.to_dict()
# create an instance of ParameterInfo from a dict
parameter_info_from_dict = ParameterInfo.from_dict(parameter_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


