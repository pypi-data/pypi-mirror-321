# OrdersAddExtendedPropertiesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**AddExtendedPropertiesRequest**](AddExtendedPropertiesRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_add_extended_properties_request import OrdersAddExtendedPropertiesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersAddExtendedPropertiesRequest from a JSON string
orders_add_extended_properties_request_instance = OrdersAddExtendedPropertiesRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersAddExtendedPropertiesRequest.to_json())

# convert the object into a dict
orders_add_extended_properties_request_dict = orders_add_extended_properties_request_instance.to_dict()
# create an instance of OrdersAddExtendedPropertiesRequest from a dict
orders_add_extended_properties_request_from_dict = OrdersAddExtendedPropertiesRequest.from_dict(orders_add_extended_properties_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


