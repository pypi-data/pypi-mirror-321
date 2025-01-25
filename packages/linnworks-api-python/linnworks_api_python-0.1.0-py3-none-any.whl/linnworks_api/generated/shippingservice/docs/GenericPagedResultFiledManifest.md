# GenericPagedResultFiledManifest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_number** | **int** |  | [optional] 
**entries_per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] [readonly] 
**data** | [**List[FiledManifest]**](FiledManifest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.shippingservice.models.generic_paged_result_filed_manifest import GenericPagedResultFiledManifest

# TODO update the JSON string below
json = "{}"
# create an instance of GenericPagedResultFiledManifest from a JSON string
generic_paged_result_filed_manifest_instance = GenericPagedResultFiledManifest.from_json(json)
# print the JSON string representation of the object
print(GenericPagedResultFiledManifest.to_json())

# convert the object into a dict
generic_paged_result_filed_manifest_dict = generic_paged_result_filed_manifest_instance.to_dict()
# create an instance of GenericPagedResultFiledManifest from a dict
generic_paged_result_filed_manifest_from_dict = GenericPagedResultFiledManifest.from_dict(generic_paged_result_filed_manifest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


