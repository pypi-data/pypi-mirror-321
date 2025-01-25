# NumericFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**value** | **float** |  | [optional] 

## Example

```python
from linnworks_api.generated.importexport.models.numeric_filter import NumericFilter

# TODO update the JSON string below
json = "{}"
# create an instance of NumericFilter from a JSON string
numeric_filter_instance = NumericFilter.from_json(json)
# print the JSON string representation of the object
print(NumericFilter.to_json())

# convert the object into a dict
numeric_filter_dict = numeric_filter_instance.to_dict()
# create an instance of NumericFilter from a dict
numeric_filter_from_dict = NumericFilter.from_dict(numeric_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


