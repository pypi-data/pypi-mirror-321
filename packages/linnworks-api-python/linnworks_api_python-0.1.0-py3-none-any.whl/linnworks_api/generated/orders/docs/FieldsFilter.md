# FieldsFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text_fields** | [**List[TextFieldFilter]**](TextFieldFilter.md) |  | [optional] 
**boolean_fields** | [**List[BooleanFieldFilter]**](BooleanFieldFilter.md) |  | [optional] 
**numeric_fields** | [**List[NumericFieldFilter]**](NumericFieldFilter.md) |  | [optional] 
**date_fields** | [**List[DateFieldFilter]**](DateFieldFilter.md) |  | [optional] 
**list_fields** | [**List[ListFieldFilter]**](ListFieldFilter.md) |  | [optional] 
**field_visibility** | [**List[FieldVisibility]**](FieldVisibility.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.fields_filter import FieldsFilter

# TODO update the JSON string below
json = "{}"
# create an instance of FieldsFilter from a JSON string
fields_filter_instance = FieldsFilter.from_json(json)
# print the JSON string representation of the object
print(FieldsFilter.to_json())

# convert the object into a dict
fields_filter_dict = fields_filter_instance.to_dict()
# create an instance of FieldsFilter from a dict
fields_filter_from_dict = FieldsFilter.from_dict(fields_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


