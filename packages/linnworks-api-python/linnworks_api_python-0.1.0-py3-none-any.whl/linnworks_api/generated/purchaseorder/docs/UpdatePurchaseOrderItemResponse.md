# UpdatePurchaseOrderItemResponse

Response from update/add purchase order item, contains newly added purchase order item line and Purchase order header with recaluclated totals

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_purchase_order_item** | [**CommonPurchaseOrderItem**](CommonPurchaseOrderItem.md) |  | [optional] 
**purchase_order_header** | [**CommonPurchaseOrderHeader**](CommonPurchaseOrderHeader.md) |  | [optional] 
**batch_inventory_id** | **int** | If the item was batched or booked into a WMS location, this is the batch inventory id for the booked in stock.   If an item was not delivered or was a non batched item, this will be null. | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.update_purchase_order_item_response import UpdatePurchaseOrderItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePurchaseOrderItemResponse from a JSON string
update_purchase_order_item_response_instance = UpdatePurchaseOrderItemResponse.from_json(json)
# print the JSON string representation of the object
print(UpdatePurchaseOrderItemResponse.to_json())

# convert the object into a dict
update_purchase_order_item_response_dict = update_purchase_order_item_response_instance.to_dict()
# create an instance of UpdatePurchaseOrderItemResponse from a dict
update_purchase_order_item_response_from_dict = UpdatePurchaseOrderItemResponse.from_dict(update_purchase_order_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


