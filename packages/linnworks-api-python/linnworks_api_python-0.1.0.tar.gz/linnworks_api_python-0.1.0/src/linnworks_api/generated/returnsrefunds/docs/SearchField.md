# SearchField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**allow_for_all_dates** | **bool** |  | [optional] 
**exact_search_optional** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.search_field import SearchField

# TODO update the JSON string below
json = "{}"
# create an instance of SearchField from a JSON string
search_field_instance = SearchField.from_json(json)
# print the JSON string representation of the object
print(SearchField.to_json())

# convert the object into a dict
search_field_dict = search_field_instance.to_dict()
# create an instance of SearchField from a dict
search_field_from_dict = SearchField.from_dict(search_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


