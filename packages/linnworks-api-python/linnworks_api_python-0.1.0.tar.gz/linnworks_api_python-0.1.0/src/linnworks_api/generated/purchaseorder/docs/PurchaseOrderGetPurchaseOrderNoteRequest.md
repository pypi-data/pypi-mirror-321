# PurchaseOrderGetPurchaseOrderNoteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_purchase_id** | **str** | Purchase order unique identifier | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.purchase_order_get_purchase_order_note_request import PurchaseOrderGetPurchaseOrderNoteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderGetPurchaseOrderNoteRequest from a JSON string
purchase_order_get_purchase_order_note_request_instance = PurchaseOrderGetPurchaseOrderNoteRequest.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderGetPurchaseOrderNoteRequest.to_json())

# convert the object into a dict
purchase_order_get_purchase_order_note_request_dict = purchase_order_get_purchase_order_note_request_instance.to_dict()
# create an instance of PurchaseOrderGetPurchaseOrderNoteRequest from a dict
purchase_order_get_purchase_order_note_request_from_dict = PurchaseOrderGetPurchaseOrderNoteRequest.from_dict(purchase_order_get_purchase_order_note_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


