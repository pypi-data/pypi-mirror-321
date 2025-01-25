# TextFieldFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**field_code** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.text_field_filter import TextFieldFilter

# TODO update the JSON string below
json = "{}"
# create an instance of TextFieldFilter from a JSON string
text_field_filter_instance = TextFieldFilter.from_json(json)
# print the JSON string representation of the object
print(TextFieldFilter.to_json())

# convert the object into a dict
text_field_filter_dict = text_field_filter_instance.to_dict()
# create an instance of TextFieldFilter from a dict
text_field_filter_from_dict = TextFieldFilter.from_dict(text_field_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


