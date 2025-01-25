# SearchPurchaseOrder2Request

Search Purchase order class

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_from** | **datetime** | Purchase order date range from (optional) | [optional] 
**date_to** | **datetime** | Purchase order date range to (optional) | [optional] 
**status** | **str** | Purchase order status: PENDING - purchase order can be changed, not yet affecting stock levels  OPEN - purchase order is created and stock levels Due are reflected  PARTIAL - partially delivered   DELIVERED - fully delivered | [optional] 
**search_value** | **str** | Specifies search value to filter with result set | [optional] 
**search_type** | **str** | Specifies search value type for search value | [optional] 
**entries_per_page** | **int** | Number of records returned, sorted by Purchase Order Date | [optional] 
**page_number** | **int** | Page Number | [optional] 
**location** | **List[str]** | Current Location | [optional] 
**supplier** | **List[str]** | Current Supplier | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.search_purchase_order2_request import SearchPurchaseOrder2Request

# TODO update the JSON string below
json = "{}"
# create an instance of SearchPurchaseOrder2Request from a JSON string
search_purchase_order2_request_instance = SearchPurchaseOrder2Request.from_json(json)
# print the JSON string representation of the object
print(SearchPurchaseOrder2Request.to_json())

# convert the object into a dict
search_purchase_order2_request_dict = search_purchase_order2_request_instance.to_dict()
# create an instance of SearchPurchaseOrder2Request from a dict
search_purchase_order2_request_from_dict = SearchPurchaseOrder2Request.from_dict(search_purchase_order2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


