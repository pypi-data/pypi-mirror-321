# PostFilterPagedResponseOpenOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result_count_removed_by_post_filter** | **int** |  | [optional] [readonly] 
**page_number** | **int** |  | [optional] 
**entries_per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] [readonly] 
**data** | [**List[OpenOrder]**](OpenOrder.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.openorders.models.post_filter_paged_response_open_order import PostFilterPagedResponseOpenOrder

# TODO update the JSON string below
json = "{}"
# create an instance of PostFilterPagedResponseOpenOrder from a JSON string
post_filter_paged_response_open_order_instance = PostFilterPagedResponseOpenOrder.from_json(json)
# print the JSON string representation of the object
print(PostFilterPagedResponseOpenOrder.to_json())

# convert the object into a dict
post_filter_paged_response_open_order_dict = post_filter_paged_response_open_order_instance.to_dict()
# create an instance of PostFilterPagedResponseOpenOrder from a dict
post_filter_paged_response_open_order_from_dict = PostFilterPagedResponseOpenOrder.from_dict(post_filter_paged_response_open_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


