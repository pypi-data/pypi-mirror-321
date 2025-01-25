# GenericPagedResultGuid


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_number** | **int** |  | [optional] 
**entries_per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] [readonly] 
**data** | **List[str]** |  | [optional] 

## Example

```python
from linnworks_api.generated.openorders.models.generic_paged_result_guid import GenericPagedResultGuid

# TODO update the JSON string below
json = "{}"
# create an instance of GenericPagedResultGuid from a JSON string
generic_paged_result_guid_instance = GenericPagedResultGuid.from_json(json)
# print the JSON string representation of the object
print(GenericPagedResultGuid.to_json())

# convert the object into a dict
generic_paged_result_guid_dict = generic_paged_result_guid_instance.to_dict()
# create an instance of GenericPagedResultGuid from a dict
generic_paged_result_guid_from_dict = GenericPagedResultGuid.from_dict(generic_paged_result_guid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


