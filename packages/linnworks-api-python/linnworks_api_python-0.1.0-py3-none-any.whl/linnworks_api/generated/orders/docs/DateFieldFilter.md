# DateFieldFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_from** | **datetime** |  | [optional] 
**date_to** | **datetime** |  | [optional] 
**type** | **str** |  | [optional] 
**value** | **int** |  | [optional] 
**field_code** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.date_field_filter import DateFieldFilter

# TODO update the JSON string below
json = "{}"
# create an instance of DateFieldFilter from a JSON string
date_field_filter_instance = DateFieldFilter.from_json(json)
# print the JSON string representation of the object
print(DateFieldFilter.to_json())

# convert the object into a dict
date_field_filter_dict = date_field_filter_instance.to_dict()
# create an instance of DateFieldFilter from a dict
date_field_filter_from_dict = DateFieldFilter.from_dict(date_field_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


