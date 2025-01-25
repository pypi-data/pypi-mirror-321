# OrdersSetExtendedPropertiesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | Order id (pkOrderID) | [optional] 
**extended_properties** | [**List[ExtendedProperty]**](ExtendedProperty.md) | Extended property information | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_set_extended_properties_request import OrdersSetExtendedPropertiesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersSetExtendedPropertiesRequest from a JSON string
orders_set_extended_properties_request_instance = OrdersSetExtendedPropertiesRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersSetExtendedPropertiesRequest.to_json())

# convert the object into a dict
orders_set_extended_properties_request_dict = orders_set_extended_properties_request_instance.to_dict()
# create an instance of OrdersSetExtendedPropertiesRequest from a dict
orders_set_extended_properties_request_from_dict = OrdersSetExtendedPropertiesRequest.from_dict(orders_set_extended_properties_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


