# ProcessedOrdersRefundShippingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_order_id** | **str** | The id of the order whose shipping needs to be refunded | [optional] 

## Example

```python
from linnworks_api.generated.processedorders.models.processed_orders_refund_shipping_request import ProcessedOrdersRefundShippingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessedOrdersRefundShippingRequest from a JSON string
processed_orders_refund_shipping_request_instance = ProcessedOrdersRefundShippingRequest.from_json(json)
# print the JSON string representation of the object
print(ProcessedOrdersRefundShippingRequest.to_json())

# convert the object into a dict
processed_orders_refund_shipping_request_dict = processed_orders_refund_shipping_request_instance.to_dict()
# create an instance of ProcessedOrdersRefundShippingRequest from a dict
processed_orders_refund_shipping_request_from_dict = ProcessedOrdersRefundShippingRequest.from_dict(processed_orders_refund_shipping_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


