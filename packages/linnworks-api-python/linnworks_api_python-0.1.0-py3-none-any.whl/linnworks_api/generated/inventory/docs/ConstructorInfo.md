# ConstructorInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_type** | **str** |  | [optional] [readonly] 
**method_implementation_flags** | **str** |  | [optional] [readonly] 
**method_handle** | **object** |  | [optional] [readonly] 
**attributes** | **str** |  | [optional] [readonly] 
**calling_convention** | **str** |  | [optional] [readonly] 
**is_generic_method_definition** | **bool** |  | [optional] [readonly] 
**contains_generic_parameters** | **bool** |  | [optional] [readonly] 
**is_generic_method** | **bool** |  | [optional] [readonly] 
**is_security_critical** | **bool** |  | [optional] [readonly] 
**is_security_safe_critical** | **bool** |  | [optional] [readonly] 
**is_security_transparent** | **bool** |  | [optional] [readonly] 
**is_public** | **bool** |  | [optional] [readonly] 
**is_private** | **bool** |  | [optional] [readonly] 
**is_family** | **bool** |  | [optional] [readonly] 
**is_assembly** | **bool** |  | [optional] [readonly] 
**is_family_and_assembly** | **bool** |  | [optional] [readonly] 
**is_family_or_assembly** | **bool** |  | [optional] [readonly] 
**is_static** | **bool** |  | [optional] [readonly] 
**is_final** | **bool** |  | [optional] [readonly] 
**is_virtual** | **bool** |  | [optional] [readonly] 
**is_hide_by_sig** | **bool** |  | [optional] [readonly] 
**is_abstract** | **bool** |  | [optional] [readonly] 
**is_special_name** | **bool** |  | [optional] [readonly] 
**is_constructor** | **bool** |  | [optional] [readonly] 
**name** | **str** |  | [optional] [readonly] 
**declaring_type** | **str** |  | [optional] [readonly] 
**reflected_type** | **str** |  | [optional] [readonly] 
**custom_attributes** | [**List[CustomAttributeData]**](CustomAttributeData.md) |  | [optional] [readonly] 
**metadata_token** | **int** |  | [optional] [readonly] 
**module** | **object** |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.inventory.models.constructor_info import ConstructorInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ConstructorInfo from a JSON string
constructor_info_instance = ConstructorInfo.from_json(json)
# print the JSON string representation of the object
print(ConstructorInfo.to_json())

# convert the object into a dict
constructor_info_dict = constructor_info_instance.to_dict()
# create an instance of ConstructorInfo from a dict
constructor_info_from_dict = ConstructorInfo.from_dict(constructor_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


