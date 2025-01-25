# SearchSorting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sort_field** | **str** |  | [optional] 
**sort_direction** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.processedorders.models.search_sorting import SearchSorting

# TODO update the JSON string below
json = "{}"
# create an instance of SearchSorting from a JSON string
search_sorting_instance = SearchSorting.from_json(json)
# print the JSON string representation of the object
print(SearchSorting.to_json())

# convert the object into a dict
search_sorting_dict = search_sorting_instance.to_dict()
# create an instance of SearchSorting from a dict
search_sorting_from_dict = SearchSorting.from_dict(search_sorting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


