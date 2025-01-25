# DeliverPurchaseOrderItemAllResponse

Response from delivering all items in an open/partial PO

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purchase_order_items** | [**List[CommonPurchaseOrderItem]**](CommonPurchaseOrderItem.md) | Delivered items | [optional] 
**purchase_order_header** | [**CommonPurchaseOrderHeader**](CommonPurchaseOrderHeader.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.deliver_purchase_order_item_all_response import DeliverPurchaseOrderItemAllResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeliverPurchaseOrderItemAllResponse from a JSON string
deliver_purchase_order_item_all_response_instance = DeliverPurchaseOrderItemAllResponse.from_json(json)
# print the JSON string representation of the object
print(DeliverPurchaseOrderItemAllResponse.to_json())

# convert the object into a dict
deliver_purchase_order_item_all_response_dict = deliver_purchase_order_item_all_response_instance.to_dict()
# create an instance of DeliverPurchaseOrderItemAllResponse from a dict
deliver_purchase_order_item_all_response_from_dict = DeliverPurchaseOrderItemAllResponse.from_dict(deliver_purchase_order_item_all_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


