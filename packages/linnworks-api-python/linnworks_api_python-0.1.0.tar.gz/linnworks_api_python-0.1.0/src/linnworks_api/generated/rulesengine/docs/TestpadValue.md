# TestpadValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** |  | [optional] 
**key** | **str** |  | [optional] 
**values** | **List[str]** |  | [optional] 

## Example

```python
from linnworks_api.generated.rulesengine.models.testpad_value import TestpadValue

# TODO update the JSON string below
json = "{}"
# create an instance of TestpadValue from a JSON string
testpad_value_instance = TestpadValue.from_json(json)
# print the JSON string representation of the object
print(TestpadValue.to_json())

# convert the object into a dict
testpad_value_dict = testpad_value_instance.to_dict()
# create an instance of TestpadValue from a dict
testpad_value_from_dict = TestpadValue.from_dict(testpad_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


