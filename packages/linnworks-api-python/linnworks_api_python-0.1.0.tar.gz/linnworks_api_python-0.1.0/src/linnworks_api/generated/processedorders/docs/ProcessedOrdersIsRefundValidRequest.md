# ProcessedOrdersIsRefundValidRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_order_id** | **str** | The id of the order to validate the refund with | [optional] 
**refund_items** | [**List[RefundItem]**](RefundItem.md) | The refund rows | [optional] 

## Example

```python
from linnworks_api.generated.processedorders.models.processed_orders_is_refund_valid_request import ProcessedOrdersIsRefundValidRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessedOrdersIsRefundValidRequest from a JSON string
processed_orders_is_refund_valid_request_instance = ProcessedOrdersIsRefundValidRequest.from_json(json)
# print the JSON string representation of the object
print(ProcessedOrdersIsRefundValidRequest.to_json())

# convert the object into a dict
processed_orders_is_refund_valid_request_dict = processed_orders_is_refund_valid_request_instance.to_dict()
# create an instance of ProcessedOrdersIsRefundValidRequest from a dict
processed_orders_is_refund_valid_request_from_dict = ProcessedOrdersIsRefundValidRequest.from_dict(processed_orders_is_refund_valid_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


