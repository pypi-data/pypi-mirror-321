# CancelOrderShippingLabelRequest

Class used for reqeust parameters for CancelOrderShippingLabel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_order_id** | **str** | Unique Order id | [optional] 

## Example

```python
from linnworks_api.generated.shippingservice.models.cancel_order_shipping_label_request import CancelOrderShippingLabelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CancelOrderShippingLabelRequest from a JSON string
cancel_order_shipping_label_request_instance = CancelOrderShippingLabelRequest.from_json(json)
# print the JSON string representation of the object
print(CancelOrderShippingLabelRequest.to_json())

# convert the object into a dict
cancel_order_shipping_label_request_dict = cancel_order_shipping_label_request_instance.to_dict()
# create an instance of CancelOrderShippingLabelRequest from a dict
cancel_order_shipping_label_request_from_dict = CancelOrderShippingLabelRequest.from_dict(cancel_order_shipping_label_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


