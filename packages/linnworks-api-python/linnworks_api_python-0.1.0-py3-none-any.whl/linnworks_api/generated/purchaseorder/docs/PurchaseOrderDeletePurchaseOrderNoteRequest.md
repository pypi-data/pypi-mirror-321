# PurchaseOrderDeletePurchaseOrderNoteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_purchase_id** | **str** | Purchase order unique identifier | [optional] 
**pk_purchase_order_note_id** | **str** | Purchase order note unique identifier | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.purchase_order_delete_purchase_order_note_request import PurchaseOrderDeletePurchaseOrderNoteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderDeletePurchaseOrderNoteRequest from a JSON string
purchase_order_delete_purchase_order_note_request_instance = PurchaseOrderDeletePurchaseOrderNoteRequest.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderDeletePurchaseOrderNoteRequest.to_json())

# convert the object into a dict
purchase_order_delete_purchase_order_note_request_dict = purchase_order_delete_purchase_order_note_request_instance.to_dict()
# create an instance of PurchaseOrderDeletePurchaseOrderNoteRequest from a dict
purchase_order_delete_purchase_order_note_request_from_dict = PurchaseOrderDeletePurchaseOrderNoteRequest.from_dict(purchase_order_delete_purchase_order_note_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


