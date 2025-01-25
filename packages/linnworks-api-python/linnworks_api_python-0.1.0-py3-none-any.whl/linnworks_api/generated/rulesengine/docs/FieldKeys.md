# FieldKeys


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** |  | [optional] 
**keys** | **List[str]** |  | [optional] 

## Example

```python
from linnworks_api.generated.rulesengine.models.field_keys import FieldKeys

# TODO update the JSON string below
json = "{}"
# create an instance of FieldKeys from a JSON string
field_keys_instance = FieldKeys.from_json(json)
# print the JSON string representation of the object
print(FieldKeys.to_json())

# convert the object into a dict
field_keys_dict = field_keys_instance.to_dict()
# create an instance of FieldKeys from a dict
field_keys_from_dict = FieldKeys.from_dict(field_keys_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


