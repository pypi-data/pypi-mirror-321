# ShippingServiceCancelOrderShippingLabelRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**CancelOrderShippingLabelRequest**](CancelOrderShippingLabelRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.shippingservice.models.shipping_service_cancel_order_shipping_label_request import ShippingServiceCancelOrderShippingLabelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingServiceCancelOrderShippingLabelRequest from a JSON string
shipping_service_cancel_order_shipping_label_request_instance = ShippingServiceCancelOrderShippingLabelRequest.from_json(json)
# print the JSON string representation of the object
print(ShippingServiceCancelOrderShippingLabelRequest.to_json())

# convert the object into a dict
shipping_service_cancel_order_shipping_label_request_dict = shipping_service_cancel_order_shipping_label_request_instance.to_dict()
# create an instance of ShippingServiceCancelOrderShippingLabelRequest from a dict
shipping_service_cancel_order_shipping_label_request_from_dict = ShippingServiceCancelOrderShippingLabelRequest.from_dict(shipping_service_cancel_order_shipping_label_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


