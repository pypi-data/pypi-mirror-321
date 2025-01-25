# DeliverPurchaseOrderItemResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_purchase_order_item** | [**PurchaseOrderItem**](PurchaseOrderItem.md) |  | [optional] 
**purchase_order_header** | [**PurchaseOrderHeader**](PurchaseOrderHeader.md) |  | [optional] 
**batch_inventory_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.deliver_purchase_order_item_response import DeliverPurchaseOrderItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeliverPurchaseOrderItemResponse from a JSON string
deliver_purchase_order_item_response_instance = DeliverPurchaseOrderItemResponse.from_json(json)
# print the JSON string representation of the object
print(DeliverPurchaseOrderItemResponse.to_json())

# convert the object into a dict
deliver_purchase_order_item_response_dict = deliver_purchase_order_item_response_instance.to_dict()
# create an instance of DeliverPurchaseOrderItemResponse from a dict
deliver_purchase_order_item_response_from_dict = DeliverPurchaseOrderItemResponse.from_dict(deliver_purchase_order_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


