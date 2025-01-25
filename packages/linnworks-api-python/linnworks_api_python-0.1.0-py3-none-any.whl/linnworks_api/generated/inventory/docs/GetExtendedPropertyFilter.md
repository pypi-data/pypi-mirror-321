# GetExtendedPropertyFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_name** | **str** |  | [optional] 
**property_type** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.get_extended_property_filter import GetExtendedPropertyFilter

# TODO update the JSON string below
json = "{}"
# create an instance of GetExtendedPropertyFilter from a JSON string
get_extended_property_filter_instance = GetExtendedPropertyFilter.from_json(json)
# print the JSON string representation of the object
print(GetExtendedPropertyFilter.to_json())

# convert the object into a dict
get_extended_property_filter_dict = get_extended_property_filter_instance.to_dict()
# create an instance of GetExtendedPropertyFilter from a dict
get_extended_property_filter_from_dict = GetExtendedPropertyFilter.from_dict(get_extended_property_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


