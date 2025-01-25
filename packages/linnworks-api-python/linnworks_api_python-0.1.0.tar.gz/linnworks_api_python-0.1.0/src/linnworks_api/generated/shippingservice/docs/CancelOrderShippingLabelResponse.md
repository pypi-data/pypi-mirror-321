# CancelOrderShippingLabelResponse

Class used for getting shipping label cancelation parameter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label_canceled** | **bool** | Identifies that the label is canceled successfully in the courier system | [optional] 
**must_cancel_manually** | **bool** | Identifies that the label is canceled in Linnworks Only and must also be canceled manually with the courier. This normally indicates that the courier does not support label cancelation. | [optional] 
**is_error** | **bool** | Is error | [optional] 
**error_message** | **str** | Error Message if IsError is true | [optional] 

## Example

```python
from linnworks_api.generated.shippingservice.models.cancel_order_shipping_label_response import CancelOrderShippingLabelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CancelOrderShippingLabelResponse from a JSON string
cancel_order_shipping_label_response_instance = CancelOrderShippingLabelResponse.from_json(json)
# print the JSON string representation of the object
print(CancelOrderShippingLabelResponse.to_json())

# convert the object into a dict
cancel_order_shipping_label_response_dict = cancel_order_shipping_label_response_instance.to_dict()
# create an instance of CancelOrderShippingLabelResponse from a dict
cancel_order_shipping_label_response_from_dict = CancelOrderShippingLabelResponse.from_dict(cancel_order_shipping_label_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


