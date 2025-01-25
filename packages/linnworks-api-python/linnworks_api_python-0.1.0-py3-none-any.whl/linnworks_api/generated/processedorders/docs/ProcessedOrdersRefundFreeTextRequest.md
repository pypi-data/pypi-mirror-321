# ProcessedOrdersRefundFreeTextRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_order_id** | **str** | The id of the order to add/update refunds for | [optional] 
**refund_items** | [**List[RefundItem]**](RefundItem.md) | The new/altered refund items | [optional] 

## Example

```python
from linnworks_api.generated.processedorders.models.processed_orders_refund_free_text_request import ProcessedOrdersRefundFreeTextRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessedOrdersRefundFreeTextRequest from a JSON string
processed_orders_refund_free_text_request_instance = ProcessedOrdersRefundFreeTextRequest.from_json(json)
# print the JSON string representation of the object
print(ProcessedOrdersRefundFreeTextRequest.to_json())

# convert the object into a dict
processed_orders_refund_free_text_request_dict = processed_orders_refund_free_text_request_instance.to_dict()
# create an instance of ProcessedOrdersRefundFreeTextRequest from a dict
processed_orders_refund_free_text_request_from_dict = ProcessedOrdersRefundFreeTextRequest.from_dict(processed_orders_refund_free_text_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


