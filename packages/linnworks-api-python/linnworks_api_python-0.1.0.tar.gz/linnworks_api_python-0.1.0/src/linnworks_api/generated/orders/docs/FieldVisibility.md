# FieldVisibility


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**visible** | **bool** |  | [optional] 
**can_filter** | **bool** |  | [optional] 
**can_sort** | **bool** |  | [optional] 
**field_type** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**sub_fields** | [**List[FieldVisibility]**](FieldVisibility.md) |  | [optional] 
**is_filter_only** | **bool** |  | [optional] 
**hot_button_icon** | **str** |  | [optional] 
**hot_button_key** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.field_visibility import FieldVisibility

# TODO update the JSON string below
json = "{}"
# create an instance of FieldVisibility from a JSON string
field_visibility_instance = FieldVisibility.from_json(json)
# print the JSON string representation of the object
print(FieldVisibility.to_json())

# convert the object into a dict
field_visibility_dict = field_visibility_instance.to_dict()
# create an instance of FieldVisibility from a dict
field_visibility_from_dict = FieldVisibility.from_dict(field_visibility_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


