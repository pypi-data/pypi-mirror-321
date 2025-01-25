# DeliverPurchaseOrderItemAllNoBatchResponse

Response from delivering all items in an open/partial PO except Batch itesm

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**po_header_and_items** | [**DeliverPurchaseOrderItemAllResponse**](DeliverPurchaseOrderItemAllResponse.md) |  | [optional] 
**all_items_delivered** | **bool** | Set to true if all items in the PO have been marked as delivered | [optional] 
**message** | **str** | Informs customers why not all items have been marked as delivered | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.deliver_purchase_order_item_all_no_batch_response import DeliverPurchaseOrderItemAllNoBatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeliverPurchaseOrderItemAllNoBatchResponse from a JSON string
deliver_purchase_order_item_all_no_batch_response_instance = DeliverPurchaseOrderItemAllNoBatchResponse.from_json(json)
# print the JSON string representation of the object
print(DeliverPurchaseOrderItemAllNoBatchResponse.to_json())

# convert the object into a dict
deliver_purchase_order_item_all_no_batch_response_dict = deliver_purchase_order_item_all_no_batch_response_instance.to_dict()
# create an instance of DeliverPurchaseOrderItemAllNoBatchResponse from a dict
deliver_purchase_order_item_all_no_batch_response_from_dict = DeliverPurchaseOrderItemAllNoBatchResponse.from_dict(deliver_purchase_order_item_all_no_batch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


