# GenericPagedResultOpenOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_number** | **int** |  | [optional] 
**entries_per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] [readonly] 
**data** | [**List[OpenOrder]**](OpenOrder.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.generic_paged_result_open_order import GenericPagedResultOpenOrder

# TODO update the JSON string below
json = "{}"
# create an instance of GenericPagedResultOpenOrder from a JSON string
generic_paged_result_open_order_instance = GenericPagedResultOpenOrder.from_json(json)
# print the JSON string representation of the object
print(GenericPagedResultOpenOrder.to_json())

# convert the object into a dict
generic_paged_result_open_order_dict = generic_paged_result_open_order_instance.to_dict()
# create an instance of GenericPagedResultOpenOrder from a dict
generic_paged_result_open_order_from_dict = GenericPagedResultOpenOrder.from_dict(generic_paged_result_open_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


