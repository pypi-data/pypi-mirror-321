# DeliverPurchaseOrderItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_number** | **str** |  | [optional] 
**bin_rack** | **str** |  | [optional] 
**priority_sequence** | **int** |  | [optional] 
**batch_status** | **str** |  | [optional] 
**pk_purchase_id** | **str** |  | [optional] 
**pk_purchase_item_id** | **str** |  | [optional] 
**delivered** | **int** |  | [optional] 
**add_to_delivered** | **int** |  | [optional] 
**delivery_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.deliver_purchase_order_item_request import DeliverPurchaseOrderItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeliverPurchaseOrderItemRequest from a JSON string
deliver_purchase_order_item_request_instance = DeliverPurchaseOrderItemRequest.from_json(json)
# print the JSON string representation of the object
print(DeliverPurchaseOrderItemRequest.to_json())

# convert the object into a dict
deliver_purchase_order_item_request_dict = deliver_purchase_order_item_request_instance.to_dict()
# create an instance of DeliverPurchaseOrderItemRequest from a dict
deliver_purchase_order_item_request_from_dict = DeliverPurchaseOrderItemRequest.from_dict(deliver_purchase_order_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


