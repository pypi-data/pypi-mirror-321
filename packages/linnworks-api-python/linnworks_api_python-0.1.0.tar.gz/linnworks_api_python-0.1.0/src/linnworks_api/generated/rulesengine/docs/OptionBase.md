# OptionBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.rulesengine.models.option_base import OptionBase

# TODO update the JSON string below
json = "{}"
# create an instance of OptionBase from a JSON string
option_base_instance = OptionBase.from_json(json)
# print the JSON string representation of the object
print(OptionBase.to_json())

# convert the object into a dict
option_base_dict = option_base_instance.to_dict()
# create an instance of OptionBase from a dict
option_base_from_dict = OptionBase.from_dict(option_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


