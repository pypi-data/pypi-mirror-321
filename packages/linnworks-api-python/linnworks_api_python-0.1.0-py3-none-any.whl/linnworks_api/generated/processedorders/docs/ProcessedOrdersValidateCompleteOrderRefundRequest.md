# ProcessedOrdersValidateCompleteOrderRefundRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_order_id** | **str** | The id of the order | [optional] 

## Example

```python
from linnworks_api.generated.processedorders.models.processed_orders_validate_complete_order_refund_request import ProcessedOrdersValidateCompleteOrderRefundRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessedOrdersValidateCompleteOrderRefundRequest from a JSON string
processed_orders_validate_complete_order_refund_request_instance = ProcessedOrdersValidateCompleteOrderRefundRequest.from_json(json)
# print the JSON string representation of the object
print(ProcessedOrdersValidateCompleteOrderRefundRequest.to_json())

# convert the object into a dict
processed_orders_validate_complete_order_refund_request_dict = processed_orders_validate_complete_order_refund_request_instance.to_dict()
# create an instance of ProcessedOrdersValidateCompleteOrderRefundRequest from a dict
processed_orders_validate_complete_order_refund_request_from_dict = ProcessedOrdersValidateCompleteOrderRefundRequest.from_dict(processed_orders_validate_complete_order_refund_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


