# UpdateOrderShippingInfoRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**postal_service_id** | **str** | Postal service ID | [optional] 
**total_weight** | **float** | Order total weight | [optional] 
**item_weight** | **float** | If order is processed | [optional] 
**postage_cost** | **float** | Order postage cost | [optional] 
**tracking_number** | **str** | Order tracking number provided by courier | [optional] 
**manual_adjust** | **bool** | If there is an adjustment to shipping cost was made | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.update_order_shipping_info_request import UpdateOrderShippingInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOrderShippingInfoRequest from a JSON string
update_order_shipping_info_request_instance = UpdateOrderShippingInfoRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateOrderShippingInfoRequest.to_json())

# convert the object into a dict
update_order_shipping_info_request_dict = update_order_shipping_info_request_instance.to_dict()
# create an instance of UpdateOrderShippingInfoRequest from a dict
update_order_shipping_info_request_from_dict = UpdateOrderShippingInfoRequest.from_dict(update_order_shipping_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


