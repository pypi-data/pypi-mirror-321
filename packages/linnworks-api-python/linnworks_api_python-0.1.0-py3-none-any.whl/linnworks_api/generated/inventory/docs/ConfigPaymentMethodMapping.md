# ConfigPaymentMethodMapping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mapping** | [**List[ConfigPaymentMethodMappingItem]**](ConfigPaymentMethodMappingItem.md) |  | [optional] [readonly] 
**channel_services** | [**List[ChannelPaymentMethod]**](ChannelPaymentMethod.md) |  | [optional] [readonly] 
**is_changed** | **bool** |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.inventory.models.config_payment_method_mapping import ConfigPaymentMethodMapping

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigPaymentMethodMapping from a JSON string
config_payment_method_mapping_instance = ConfigPaymentMethodMapping.from_json(json)
# print the JSON string representation of the object
print(ConfigPaymentMethodMapping.to_json())

# convert the object into a dict
config_payment_method_mapping_dict = config_payment_method_mapping_instance.to_dict()
# create an instance of ConfigPaymentMethodMapping from a dict
config_payment_method_mapping_from_dict = ConfigPaymentMethodMapping.from_dict(config_payment_method_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


