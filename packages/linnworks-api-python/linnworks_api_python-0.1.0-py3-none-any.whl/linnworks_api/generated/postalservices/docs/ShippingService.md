# ShippingService


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_postal_service_id** | **str** |  | [optional] 
**postal_service_name** | **str** |  | [optional] 
**vendor** | **str** |  | [optional] 
**accountid** | **str** |  | [optional] 
**vendor_friendly_name** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.postalservices.models.shipping_service import ShippingService

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingService from a JSON string
shipping_service_instance = ShippingService.from_json(json)
# print the JSON string representation of the object
print(ShippingService.to_json())

# convert the object into a dict
shipping_service_dict = shipping_service_instance.to_dict()
# create an instance of ShippingService from a dict
shipping_service_from_dict = ShippingService.from_dict(shipping_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


