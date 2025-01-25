# BooleanFieldFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **bool** |  | [optional] 
**field_code** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.boolean_field_filter import BooleanFieldFilter

# TODO update the JSON string below
json = "{}"
# create an instance of BooleanFieldFilter from a JSON string
boolean_field_filter_instance = BooleanFieldFilter.from_json(json)
# print the JSON string representation of the object
print(BooleanFieldFilter.to_json())

# convert the object into a dict
boolean_field_filter_dict = boolean_field_filter_instance.to_dict()
# create an instance of BooleanFieldFilter from a dict
boolean_field_filter_from_dict = BooleanFieldFilter.from_dict(boolean_field_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


