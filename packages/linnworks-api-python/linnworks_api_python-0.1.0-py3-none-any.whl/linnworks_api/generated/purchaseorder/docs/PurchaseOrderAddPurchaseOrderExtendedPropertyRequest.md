# PurchaseOrderAddPurchaseOrderExtendedPropertyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**AddPurchaseOrderExtendedPropertyRequest**](AddPurchaseOrderExtendedPropertyRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.purchase_order_add_purchase_order_extended_property_request import PurchaseOrderAddPurchaseOrderExtendedPropertyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderAddPurchaseOrderExtendedPropertyRequest from a JSON string
purchase_order_add_purchase_order_extended_property_request_instance = PurchaseOrderAddPurchaseOrderExtendedPropertyRequest.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderAddPurchaseOrderExtendedPropertyRequest.to_json())

# convert the object into a dict
purchase_order_add_purchase_order_extended_property_request_dict = purchase_order_add_purchase_order_extended_property_request_instance.to_dict()
# create an instance of PurchaseOrderAddPurchaseOrderExtendedPropertyRequest from a dict
purchase_order_add_purchase_order_extended_property_request_from_dict = PurchaseOrderAddPurchaseOrderExtendedPropertyRequest.from_dict(purchase_order_add_purchase_order_extended_property_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


