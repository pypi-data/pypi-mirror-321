# Measures


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimension** | **str** | Dimension measures | [optional] 
**weight** | **str** | Weight measures | [optional] 

## Example

```python
from linnworks_api.generated.settings.models.measures import Measures

# TODO update the JSON string below
json = "{}"
# create an instance of Measures from a JSON string
measures_instance = Measures.from_json(json)
# print the JSON string representation of the object
print(Measures.to_json())

# convert the object into a dict
measures_dict = measures_instance.to_dict()
# create an instance of Measures from a dict
measures_from_dict = Measures.from_dict(measures_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


