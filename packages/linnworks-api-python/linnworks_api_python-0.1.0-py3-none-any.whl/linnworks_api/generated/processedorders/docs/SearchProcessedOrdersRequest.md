# SearchProcessedOrdersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_term** | **str** | Search Term | [optional] 
**search_filters** | [**List[SearchFilters]**](SearchFilters.md) | Search Filters | [optional] 
**date_field** | **str** | Date Field Type | [optional] 
**from_date** | **datetime** | From Date | [optional] 
**to_date** | **datetime** | To Date | [optional] 
**page_number** | **int** | Page Number | [optional] 
**results_per_page** | **int** | Results Per Page | [optional] 
**search_sorting** | [**SearchSorting**](SearchSorting.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.processedorders.models.search_processed_orders_request import SearchProcessedOrdersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SearchProcessedOrdersRequest from a JSON string
search_processed_orders_request_instance = SearchProcessedOrdersRequest.from_json(json)
# print the JSON string representation of the object
print(SearchProcessedOrdersRequest.to_json())

# convert the object into a dict
search_processed_orders_request_dict = search_processed_orders_request_instance.to_dict()
# create an instance of SearchProcessedOrdersRequest from a dict
search_processed_orders_request_from_dict = SearchProcessedOrdersRequest.from_dict(search_processed_orders_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


