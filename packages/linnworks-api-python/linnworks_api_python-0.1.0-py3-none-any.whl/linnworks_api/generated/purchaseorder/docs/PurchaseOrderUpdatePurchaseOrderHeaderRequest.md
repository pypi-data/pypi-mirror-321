# PurchaseOrderUpdatePurchaseOrderHeaderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**update_parameter** | [**UpdatePurchaseOrderHeaderParameter**](UpdatePurchaseOrderHeaderParameter.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.purchase_order_update_purchase_order_header_request import PurchaseOrderUpdatePurchaseOrderHeaderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderUpdatePurchaseOrderHeaderRequest from a JSON string
purchase_order_update_purchase_order_header_request_instance = PurchaseOrderUpdatePurchaseOrderHeaderRequest.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderUpdatePurchaseOrderHeaderRequest.to_json())

# convert the object into a dict
purchase_order_update_purchase_order_header_request_dict = purchase_order_update_purchase_order_header_request_instance.to_dict()
# create an instance of PurchaseOrderUpdatePurchaseOrderHeaderRequest from a dict
purchase_order_update_purchase_order_header_request_from_dict = PurchaseOrderUpdatePurchaseOrderHeaderRequest.from_dict(purchase_order_update_purchase_order_header_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


