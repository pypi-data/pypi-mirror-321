# ProcessedOrdersRefundServicesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_order_id** | **str** | The id of the order to refund services for. | [optional] 
**refund_items** | [**List[RefundItem]**](RefundItem.md) | Refunds for service items | [optional] 

## Example

```python
from linnworks_api.generated.processedorders.models.processed_orders_refund_services_request import ProcessedOrdersRefundServicesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessedOrdersRefundServicesRequest from a JSON string
processed_orders_refund_services_request_instance = ProcessedOrdersRefundServicesRequest.from_json(json)
# print the JSON string representation of the object
print(ProcessedOrdersRefundServicesRequest.to_json())

# convert the object into a dict
processed_orders_refund_services_request_dict = processed_orders_refund_services_request_instance.to_dict()
# create an instance of ProcessedOrdersRefundServicesRequest from a dict
processed_orders_refund_services_request_from_dict = ProcessedOrdersRefundServicesRequest.from_dict(processed_orders_refund_services_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


