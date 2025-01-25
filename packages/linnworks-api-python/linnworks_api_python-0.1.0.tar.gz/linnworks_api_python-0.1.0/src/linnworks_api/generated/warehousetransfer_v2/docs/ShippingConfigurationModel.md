# ShippingConfigurationModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipping_mode** | [**ShippingMode**](ShippingMode.md) |  | [optional] 
**shipping_solution** | [**ShippingSolution**](ShippingSolution.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_v2.models.shipping_configuration_model import ShippingConfigurationModel

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingConfigurationModel from a JSON string
shipping_configuration_model_instance = ShippingConfigurationModel.from_json(json)
# print the JSON string representation of the object
print(ShippingConfigurationModel.to_json())

# convert the object into a dict
shipping_configuration_model_dict = shipping_configuration_model_instance.to_dict()
# create an instance of ShippingConfigurationModel from a dict
shipping_configuration_model_from_dict = ShippingConfigurationModel.from_dict(shipping_configuration_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


