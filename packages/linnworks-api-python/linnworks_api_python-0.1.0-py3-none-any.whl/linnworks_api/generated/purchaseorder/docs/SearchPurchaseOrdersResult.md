# SearchPurchaseOrdersResult

Search_PurchaseOrders result class. Contains the Result - the list of returned purchase order headers, and current paging information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[CommonPurchaseOrderHeader]**](CommonPurchaseOrderHeader.md) | List of purchase order headers | [optional] 
**total_pages** | **int** | Total number of pages | [optional] 
**current_page_number** | **int** | Currently request page number | [optional] 
**entries_per_page** | **int** | Requested entries per page | [optional] 
**total_number_of_records** | **int** | Total number of records matching the search request | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.search_purchase_orders_result import SearchPurchaseOrdersResult

# TODO update the JSON string below
json = "{}"
# create an instance of SearchPurchaseOrdersResult from a JSON string
search_purchase_orders_result_instance = SearchPurchaseOrdersResult.from_json(json)
# print the JSON string representation of the object
print(SearchPurchaseOrdersResult.to_json())

# convert the object into a dict
search_purchase_orders_result_dict = search_purchase_orders_result_instance.to_dict()
# create an instance of SearchPurchaseOrdersResult from a dict
search_purchase_orders_result_from_dict = SearchPurchaseOrdersResult.from_dict(search_purchase_orders_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


