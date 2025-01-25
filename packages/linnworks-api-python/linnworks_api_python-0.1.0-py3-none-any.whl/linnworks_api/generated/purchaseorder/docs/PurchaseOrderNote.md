# PurchaseOrderNote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_purchase_order_note_id** | **str** |  | [optional] 
**note** | **str** |  | [optional] 
**note_date_time** | **datetime** |  | [optional] 
**user_name** | **str** |  | [optional] 
**note_date** | **str** |  | [optional] [readonly] 
**note_time** | **str** |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.purchase_order_note import PurchaseOrderNote

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderNote from a JSON string
purchase_order_note_instance = PurchaseOrderNote.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderNote.to_json())

# convert the object into a dict
purchase_order_note_dict = purchase_order_note_instance.to_dict()
# create an instance of PurchaseOrderNote from a dict
purchase_order_note_from_dict = PurchaseOrderNote.from_dict(purchase_order_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


