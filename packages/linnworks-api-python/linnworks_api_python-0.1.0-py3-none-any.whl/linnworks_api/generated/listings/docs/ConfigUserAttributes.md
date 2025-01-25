# ConfigUserAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**extended_property** | **str** |  | [optional] 
**is_required** | **bool** |  | [optional] 
**max_file_size** | **int** |  | [optional] 
**allowed_file_types** | **str** |  | [optional] 
**select_options** | **str** |  | [optional] 
**sort_order** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.config_user_attributes import ConfigUserAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigUserAttributes from a JSON string
config_user_attributes_instance = ConfigUserAttributes.from_json(json)
# print the JSON string representation of the object
print(ConfigUserAttributes.to_json())

# convert the object into a dict
config_user_attributes_dict = config_user_attributes_instance.to_dict()
# create an instance of ConfigUserAttributes from a dict
config_user_attributes_from_dict = ConfigUserAttributes.from_dict(config_user_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


