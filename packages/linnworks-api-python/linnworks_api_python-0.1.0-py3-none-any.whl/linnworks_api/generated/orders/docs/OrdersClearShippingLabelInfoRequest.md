# OrdersClearShippingLabelInfoRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_ids** | **List[str]** | Order ids | [optional] 
**without_confirmation** | **bool** | skip any confirmation message | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_clear_shipping_label_info_request import OrdersClearShippingLabelInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersClearShippingLabelInfoRequest from a JSON string
orders_clear_shipping_label_info_request_instance = OrdersClearShippingLabelInfoRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersClearShippingLabelInfoRequest.to_json())

# convert the object into a dict
orders_clear_shipping_label_info_request_dict = orders_clear_shipping_label_info_request_instance.to_dict()
# create an instance of OrdersClearShippingLabelInfoRequest from a dict
orders_clear_shipping_label_info_request_from_dict = OrdersClearShippingLabelInfoRequest.from_dict(orders_clear_shipping_label_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


