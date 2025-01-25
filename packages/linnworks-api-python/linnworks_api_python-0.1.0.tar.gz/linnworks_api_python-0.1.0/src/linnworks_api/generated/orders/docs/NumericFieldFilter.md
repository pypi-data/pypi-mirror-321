# NumericFieldFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**value** | **float** |  | [optional] 
**field_code** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.numeric_field_filter import NumericFieldFilter

# TODO update the JSON string below
json = "{}"
# create an instance of NumericFieldFilter from a JSON string
numeric_field_filter_instance = NumericFieldFilter.from_json(json)
# print the JSON string representation of the object
print(NumericFieldFilter.to_json())

# convert the object into a dict
numeric_field_filter_dict = numeric_field_filter_instance.to_dict()
# create an instance of NumericFieldFilter from a dict
numeric_field_filter_from_dict = NumericFieldFilter.from_dict(numeric_field_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


