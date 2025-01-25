# DateRangeFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value_from** | **datetime** |  | [optional] 
**value_to** | **datetime** |  | [optional] 
**days** | **int** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.importexport.models.date_range_filter import DateRangeFilter

# TODO update the JSON string below
json = "{}"
# create an instance of DateRangeFilter from a JSON string
date_range_filter_instance = DateRangeFilter.from_json(json)
# print the JSON string representation of the object
print(DateRangeFilter.to_json())

# convert the object into a dict
date_range_filter_dict = date_range_filter_instance.to_dict()
# create an instance of DateRangeFilter from a dict
date_range_filter_from_dict = DateRangeFilter.from_dict(date_range_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


