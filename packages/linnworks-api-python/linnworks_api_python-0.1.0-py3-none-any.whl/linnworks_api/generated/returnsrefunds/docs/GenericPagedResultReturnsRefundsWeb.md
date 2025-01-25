# GenericPagedResultReturnsRefundsWeb


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_number** | **int** |  | [optional] 
**entries_per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] [readonly] 
**data** | [**List[ReturnsRefundsWeb]**](ReturnsRefundsWeb.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.generic_paged_result_returns_refunds_web import GenericPagedResultReturnsRefundsWeb

# TODO update the JSON string below
json = "{}"
# create an instance of GenericPagedResultReturnsRefundsWeb from a JSON string
generic_paged_result_returns_refunds_web_instance = GenericPagedResultReturnsRefundsWeb.from_json(json)
# print the JSON string representation of the object
print(GenericPagedResultReturnsRefundsWeb.to_json())

# convert the object into a dict
generic_paged_result_returns_refunds_web_dict = generic_paged_result_returns_refunds_web_instance.to_dict()
# create an instance of GenericPagedResultReturnsRefundsWeb from a dict
generic_paged_result_returns_refunds_web_from_dict = GenericPagedResultReturnsRefundsWeb.from_dict(generic_paged_result_returns_refunds_web_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


