# ConfigCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**default** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.config_category import ConfigCategory

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigCategory from a JSON string
config_category_instance = ConfigCategory.from_json(json)
# print the JSON string representation of the object
print(ConfigCategory.to_json())

# convert the object into a dict
config_category_dict = config_category_instance.to_dict()
# create an instance of ConfigCategory from a dict
config_category_from_dict = ConfigCategory.from_dict(config_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


