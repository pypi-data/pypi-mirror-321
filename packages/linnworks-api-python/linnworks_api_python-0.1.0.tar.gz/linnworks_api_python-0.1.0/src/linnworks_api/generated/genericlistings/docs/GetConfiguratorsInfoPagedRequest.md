# GetConfiguratorsInfoPagedRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_type** | **str** |  | [optional] 
**channel_name** | **str** |  | [optional] 
**pagination_parameters** | [**PaginationParameters**](PaginationParameters.md) |  | [optional] 
**is_by_configurator_ids** | **bool** |  | [optional] 
**configurator_ids** | **List[int]** |  | [optional] 
**selected_regions** | [**List[TupleInt32Int32]**](TupleInt32Int32.md) |  | [optional] 
**token** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.genericlistings.models.get_configurators_info_paged_request import GetConfiguratorsInfoPagedRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetConfiguratorsInfoPagedRequest from a JSON string
get_configurators_info_paged_request_instance = GetConfiguratorsInfoPagedRequest.from_json(json)
# print the JSON string representation of the object
print(GetConfiguratorsInfoPagedRequest.to_json())

# convert the object into a dict
get_configurators_info_paged_request_dict = get_configurators_info_paged_request_instance.to_dict()
# create an instance of GetConfiguratorsInfoPagedRequest from a dict
get_configurators_info_paged_request_from_dict = GetConfiguratorsInfoPagedRequest.from_dict(get_configurators_info_paged_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


