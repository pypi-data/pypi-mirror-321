# ConfigButton


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** |  | [optional] 
**group_name** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**function_name** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.config_button import ConfigButton

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigButton from a JSON string
config_button_instance = ConfigButton.from_json(json)
# print the JSON string representation of the object
print(ConfigButton.to_json())

# convert the object into a dict
config_button_dict = config_button_instance.to_dict()
# create an instance of ConfigButton from a dict
config_button_from_dict = ConfigButton.from_dict(config_button_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


