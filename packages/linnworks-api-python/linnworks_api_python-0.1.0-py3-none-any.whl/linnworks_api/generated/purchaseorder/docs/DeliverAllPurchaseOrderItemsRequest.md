# DeliverAllPurchaseOrderItemsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_purchase_id** | **str** |  | [optional] 
**delivery_id** | **int** |  | [optional] 
**items** | [**List[PurchaseOrderDeliveredItem]**](PurchaseOrderDeliveredItem.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.deliver_all_purchase_order_items_request import DeliverAllPurchaseOrderItemsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeliverAllPurchaseOrderItemsRequest from a JSON string
deliver_all_purchase_order_items_request_instance = DeliverAllPurchaseOrderItemsRequest.from_json(json)
# print the JSON string representation of the object
print(DeliverAllPurchaseOrderItemsRequest.to_json())

# convert the object into a dict
deliver_all_purchase_order_items_request_dict = deliver_all_purchase_order_items_request_instance.to_dict()
# create an instance of DeliverAllPurchaseOrderItemsRequest from a dict
deliver_all_purchase_order_items_request_from_dict = DeliverAllPurchaseOrderItemsRequest.from_dict(deliver_all_purchase_order_items_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


