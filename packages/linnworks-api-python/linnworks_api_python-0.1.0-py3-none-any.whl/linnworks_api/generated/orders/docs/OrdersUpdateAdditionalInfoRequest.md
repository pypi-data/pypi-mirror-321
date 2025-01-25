# OrdersUpdateAdditionalInfoRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**UpdateAdditionalInfoRequest**](UpdateAdditionalInfoRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_update_additional_info_request import OrdersUpdateAdditionalInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersUpdateAdditionalInfoRequest from a JSON string
orders_update_additional_info_request_instance = OrdersUpdateAdditionalInfoRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersUpdateAdditionalInfoRequest.to_json())

# convert the object into a dict
orders_update_additional_info_request_dict = orders_update_additional_info_request_instance.to_dict()
# create an instance of OrdersUpdateAdditionalInfoRequest from a dict
orders_update_additional_info_request_from_dict = OrdersUpdateAdditionalInfoRequest.from_dict(orders_update_additional_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


