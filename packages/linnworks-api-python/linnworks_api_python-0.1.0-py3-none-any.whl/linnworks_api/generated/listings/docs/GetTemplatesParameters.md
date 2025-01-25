# GetTemplatesParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_ids** | **List[str]** |  | [optional] 
**only_with_errors** | **bool** |  | [optional] 
**source** | **str** |  | [optional] 
**sub_source** | **str** |  | [optional] 
**config_id** | **str** |  | [optional] 
**inventory_item_ids** | **List[str]** |  | [optional] 
**selected_regions** | [**List[TupleInt32Int32]**](TupleInt32Int32.md) |  | [optional] 
**token** | **str** |  | [optional] 
**templates_type** | **str** |  | [optional] 
**page_number** | **int** |  | [optional] 
**entries_per_page** | **int** |  | [optional] 
**is_migrated** | **bool** |  | [optional] 
**site_filter** | [**SiteFilter**](SiteFilter.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.get_templates_parameters import GetTemplatesParameters

# TODO update the JSON string below
json = "{}"
# create an instance of GetTemplatesParameters from a JSON string
get_templates_parameters_instance = GetTemplatesParameters.from_json(json)
# print the JSON string representation of the object
print(GetTemplatesParameters.to_json())

# convert the object into a dict
get_templates_parameters_dict = get_templates_parameters_instance.to_dict()
# create an instance of GetTemplatesParameters from a dict
get_templates_parameters_from_dict = GetTemplatesParameters.from_dict(get_templates_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


