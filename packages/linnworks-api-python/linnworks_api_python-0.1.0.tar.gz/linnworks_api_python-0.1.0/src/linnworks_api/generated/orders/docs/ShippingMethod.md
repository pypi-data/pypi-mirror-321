# ShippingMethod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor** | **str** |  | [optional] 
**postal_services** | [**List[PostageService]**](PostageService.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.shipping_method import ShippingMethod

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingMethod from a JSON string
shipping_method_instance = ShippingMethod.from_json(json)
# print the JSON string representation of the object
print(ShippingMethod.to_json())

# convert the object into a dict
shipping_method_dict = shipping_method_instance.to_dict()
# create an instance of ShippingMethod from a dict
shipping_method_from_dict = ShippingMethod.from_dict(shipping_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


