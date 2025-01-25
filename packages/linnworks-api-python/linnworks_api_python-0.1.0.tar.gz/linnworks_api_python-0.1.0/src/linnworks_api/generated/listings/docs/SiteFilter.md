# SiteFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | [optional] 
**sub_source** | **str** |  | [optional] 
**sites** | **str** |  | [optional] 
**selected_sites** | **List[str]** |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.listings.models.site_filter import SiteFilter

# TODO update the JSON string below
json = "{}"
# create an instance of SiteFilter from a JSON string
site_filter_instance = SiteFilter.from_json(json)
# print the JSON string representation of the object
print(SiteFilter.to_json())

# convert the object into a dict
site_filter_dict = site_filter_instance.to_dict()
# create an instance of SiteFilter from a dict
site_filter_from_dict = SiteFilter.from_dict(site_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


