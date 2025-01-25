# ConfigPaymentMethodMappingItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fk_channel_id** | **int** |  | [optional] 
**pk_row_id** | **int** |  | [optional] 
**tag** | **str** |  | [optional] 
**fk_bank_id** | **str** |  | [optional] 
**payment_method_name** | **str** |  | [optional] 
**site** | **str** |  | [optional] 
**is_changed** | **bool** |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.inventory.models.config_payment_method_mapping_item import ConfigPaymentMethodMappingItem

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigPaymentMethodMappingItem from a JSON string
config_payment_method_mapping_item_instance = ConfigPaymentMethodMappingItem.from_json(json)
# print the JSON string representation of the object
print(ConfigPaymentMethodMappingItem.to_json())

# convert the object into a dict
config_payment_method_mapping_item_dict = config_payment_method_mapping_item_instance.to_dict()
# create an instance of ConfigPaymentMethodMappingItem from a dict
config_payment_method_mapping_item_from_dict = ConfigPaymentMethodMappingItem.from_dict(config_payment_method_mapping_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


