# GenericPagedResultConsignment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_number** | **int** |  | [optional] 
**entries_per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] [readonly] 
**data** | [**List[Consignment]**](Consignment.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.shippingservice.models.generic_paged_result_consignment import GenericPagedResultConsignment

# TODO update the JSON string below
json = "{}"
# create an instance of GenericPagedResultConsignment from a JSON string
generic_paged_result_consignment_instance = GenericPagedResultConsignment.from_json(json)
# print the JSON string representation of the object
print(GenericPagedResultConsignment.to_json())

# convert the object into a dict
generic_paged_result_consignment_dict = generic_paged_result_consignment_instance.to_dict()
# create an instance of GenericPagedResultConsignment from a dict
generic_paged_result_consignment_from_dict = GenericPagedResultConsignment.from_dict(generic_paged_result_consignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


