# SearchPurchaseOrderParameter

Search Purchase order class

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_from** | **datetime** | Purchase order date range from (optional) | [optional] 
**date_to** | **datetime** | Purchase order date range to (optional) | [optional] 
**status** | **str** | Purchase order status: PENDING - purchase order can be changed, not yet affecting stock levels  OPEN - purchase order is created and stock levels Due are reflected  PARTIAL - partially delivered   DELIVERED - fully delivered | [optional] 
**reference_like** | **str** | Purchase order reference or Supplier PO reference, works as a like will return all POs that contain ReferenceLike value | [optional] 
**entries_per_page** | **int** | Number of records returned, sorted by Purchase Order Date | [optional] 
**page_number** | **int** | Page Number | [optional] 
**location** | **List[str]** | Current Location | [optional] 
**supplier** | **List[str]** | Current Supplier | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.search_purchase_order_parameter import SearchPurchaseOrderParameter

# TODO update the JSON string below
json = "{}"
# create an instance of SearchPurchaseOrderParameter from a JSON string
search_purchase_order_parameter_instance = SearchPurchaseOrderParameter.from_json(json)
# print the JSON string representation of the object
print(SearchPurchaseOrderParameter.to_json())

# convert the object into a dict
search_purchase_order_parameter_dict = search_purchase_order_parameter_instance.to_dict()
# create an instance of SearchPurchaseOrderParameter from a dict
search_purchase_order_parameter_from_dict = SearchPurchaseOrderParameter.from_dict(search_purchase_order_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


