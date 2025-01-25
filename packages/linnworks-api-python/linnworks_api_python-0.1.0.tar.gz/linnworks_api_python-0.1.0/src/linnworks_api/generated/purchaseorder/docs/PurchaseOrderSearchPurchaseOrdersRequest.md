# PurchaseOrderSearchPurchaseOrdersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_parameter** | [**SearchPurchaseOrderParameter**](SearchPurchaseOrderParameter.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.purchase_order_search_purchase_orders_request import PurchaseOrderSearchPurchaseOrdersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderSearchPurchaseOrdersRequest from a JSON string
purchase_order_search_purchase_orders_request_instance = PurchaseOrderSearchPurchaseOrdersRequest.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderSearchPurchaseOrdersRequest.to_json())

# convert the object into a dict
purchase_order_search_purchase_orders_request_dict = purchase_order_search_purchase_orders_request_instance.to_dict()
# create an instance of PurchaseOrderSearchPurchaseOrdersRequest from a dict
purchase_order_search_purchase_orders_request_from_dict = PurchaseOrderSearchPurchaseOrdersRequest.from_dict(purchase_order_search_purchase_orders_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


