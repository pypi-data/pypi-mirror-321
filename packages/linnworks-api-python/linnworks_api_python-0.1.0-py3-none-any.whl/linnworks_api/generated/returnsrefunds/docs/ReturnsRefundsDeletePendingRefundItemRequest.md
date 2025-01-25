# ReturnsRefundsDeletePendingRefundItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fk_order_id** | **str** | unique order ID of the refund order | [optional] 
**pk_refund_row_id** | **str** | unique refund row ID of the refund item to delete | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.returns_refunds_delete_pending_refund_item_request import ReturnsRefundsDeletePendingRefundItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnsRefundsDeletePendingRefundItemRequest from a JSON string
returns_refunds_delete_pending_refund_item_request_instance = ReturnsRefundsDeletePendingRefundItemRequest.from_json(json)
# print the JSON string representation of the object
print(ReturnsRefundsDeletePendingRefundItemRequest.to_json())

# convert the object into a dict
returns_refunds_delete_pending_refund_item_request_dict = returns_refunds_delete_pending_refund_item_request_instance.to_dict()
# create an instance of ReturnsRefundsDeletePendingRefundItemRequest from a dict
returns_refunds_delete_pending_refund_item_request_from_dict = ReturnsRefundsDeletePendingRefundItemRequest.from_dict(returns_refunds_delete_pending_refund_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


