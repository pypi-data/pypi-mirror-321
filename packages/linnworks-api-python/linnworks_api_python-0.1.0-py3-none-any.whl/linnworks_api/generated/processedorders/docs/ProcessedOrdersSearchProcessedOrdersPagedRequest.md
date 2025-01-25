# ProcessedOrdersSearchProcessedOrdersPagedRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **datetime** | The lower end of the date range to search. Can be null if searching for &#39;all dates&#39;. Maximum range is 3 months. | [optional] 
**to** | **datetime** | The upper end of the date range to search. Can be null if searching for &#39;all dates&#39;. Maximum range is 3 months. | [optional] 
**date_type** | **str** | The search type (e.g. ALLDATES) | [optional] 
**search_field** | **str** | The field to search by. Can be found by calling GetSearchTypes. | [optional] 
**exact_match** | **bool** | Set to true if an exact match is required for the search data. | [optional] 
**search_term** | **str** | The term which you are searching for. | [optional] 
**page_num** | **int** | The page number of the request. | [optional] 
**num_entries_per_page** | **int** | The number of entries required on a page. Maximum 200. | [optional] 

## Example

```python
from linnworks_api.generated.processedorders.models.processed_orders_search_processed_orders_paged_request import ProcessedOrdersSearchProcessedOrdersPagedRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessedOrdersSearchProcessedOrdersPagedRequest from a JSON string
processed_orders_search_processed_orders_paged_request_instance = ProcessedOrdersSearchProcessedOrdersPagedRequest.from_json(json)
# print the JSON string representation of the object
print(ProcessedOrdersSearchProcessedOrdersPagedRequest.to_json())

# convert the object into a dict
processed_orders_search_processed_orders_paged_request_dict = processed_orders_search_processed_orders_paged_request_instance.to_dict()
# create an instance of ProcessedOrdersSearchProcessedOrdersPagedRequest from a dict
processed_orders_search_processed_orders_paged_request_from_dict = ProcessedOrdersSearchProcessedOrdersPagedRequest.from_dict(processed_orders_search_processed_orders_paged_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


