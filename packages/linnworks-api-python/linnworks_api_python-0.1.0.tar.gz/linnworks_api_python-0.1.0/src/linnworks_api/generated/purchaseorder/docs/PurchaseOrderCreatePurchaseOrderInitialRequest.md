# PurchaseOrderCreatePurchaseOrderInitialRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_parameters** | [**CreatePurchaseOrderInitialParameter**](CreatePurchaseOrderInitialParameter.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.purchase_order_create_purchase_order_initial_request import PurchaseOrderCreatePurchaseOrderInitialRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderCreatePurchaseOrderInitialRequest from a JSON string
purchase_order_create_purchase_order_initial_request_instance = PurchaseOrderCreatePurchaseOrderInitialRequest.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderCreatePurchaseOrderInitialRequest.to_json())

# convert the object into a dict
purchase_order_create_purchase_order_initial_request_dict = purchase_order_create_purchase_order_initial_request_instance.to_dict()
# create an instance of PurchaseOrderCreatePurchaseOrderInitialRequest from a dict
purchase_order_create_purchase_order_initial_request_from_dict = PurchaseOrderCreatePurchaseOrderInitialRequest.from_dict(purchase_order_create_purchase_order_initial_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


