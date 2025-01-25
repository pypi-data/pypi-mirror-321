# ShippingLocationModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_location_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**company** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**address1** | **str** |  | [optional] 
**address2** | **str** |  | [optional] 
**postcode** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.shipping_location_model import ShippingLocationModel

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingLocationModel from a JSON string
shipping_location_model_instance = ShippingLocationModel.from_json(json)
# print the JSON string representation of the object
print(ShippingLocationModel.to_json())

# convert the object into a dict
shipping_location_model_dict = shipping_location_model_instance.to_dict()
# create an instance of ShippingLocationModel from a dict
shipping_location_model_from_dict = ShippingLocationModel.from_dict(shipping_location_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


