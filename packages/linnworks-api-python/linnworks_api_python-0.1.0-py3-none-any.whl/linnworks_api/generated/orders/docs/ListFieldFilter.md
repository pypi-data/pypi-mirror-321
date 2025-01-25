# ListFieldFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**field_code** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.list_field_filter import ListFieldFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ListFieldFilter from a JSON string
list_field_filter_instance = ListFieldFilter.from_json(json)
# print the JSON string representation of the object
print(ListFieldFilter.to_json())

# convert the object into a dict
list_field_filter_dict = list_field_filter_instance.to_dict()
# create an instance of ListFieldFilter from a dict
list_field_filter_from_dict = ListFieldFilter.from_dict(list_field_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


