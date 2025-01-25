# GenericPagedResultVariationGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_number** | **int** |  | [optional] 
**entries_per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] [readonly] 
**data** | [**List[VariationGroup]**](VariationGroup.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.generic_paged_result_variation_group import GenericPagedResultVariationGroup

# TODO update the JSON string below
json = "{}"
# create an instance of GenericPagedResultVariationGroup from a JSON string
generic_paged_result_variation_group_instance = GenericPagedResultVariationGroup.from_json(json)
# print the JSON string representation of the object
print(GenericPagedResultVariationGroup.to_json())

# convert the object into a dict
generic_paged_result_variation_group_dict = generic_paged_result_variation_group_instance.to_dict()
# create an instance of GenericPagedResultVariationGroup from a dict
generic_paged_result_variation_group_from_dict = GenericPagedResultVariationGroup.from_dict(generic_paged_result_variation_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


