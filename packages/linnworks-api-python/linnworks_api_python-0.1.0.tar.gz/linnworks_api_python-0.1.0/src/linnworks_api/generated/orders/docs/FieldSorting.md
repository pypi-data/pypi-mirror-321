# FieldSorting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_code** | **str** |  | [optional] 
**direction** | **str** |  | [optional] 
**order** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.field_sorting import FieldSorting

# TODO update the JSON string below
json = "{}"
# create an instance of FieldSorting from a JSON string
field_sorting_instance = FieldSorting.from_json(json)
# print the JSON string representation of the object
print(FieldSorting.to_json())

# convert the object into a dict
field_sorting_dict = field_sorting_instance.to_dict()
# create an instance of FieldSorting from a dict
field_sorting_from_dict = FieldSorting.from_dict(field_sorting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


