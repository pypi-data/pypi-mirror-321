# PurchaseOrderAddPurchaseOrderNoteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_purchase_id** | **str** | Purchase order unique identifier | [optional] 
**note** | **str** | Note text, 2000 chars max (longer notes are truncated) | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.purchase_order_add_purchase_order_note_request import PurchaseOrderAddPurchaseOrderNoteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderAddPurchaseOrderNoteRequest from a JSON string
purchase_order_add_purchase_order_note_request_instance = PurchaseOrderAddPurchaseOrderNoteRequest.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderAddPurchaseOrderNoteRequest.to_json())

# convert the object into a dict
purchase_order_add_purchase_order_note_request_dict = purchase_order_add_purchase_order_note_request_instance.to_dict()
# create an instance of PurchaseOrderAddPurchaseOrderNoteRequest from a dict
purchase_order_add_purchase_order_note_request_from_dict = PurchaseOrderAddPurchaseOrderNoteRequest.from_dict(purchase_order_add_purchase_order_note_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


