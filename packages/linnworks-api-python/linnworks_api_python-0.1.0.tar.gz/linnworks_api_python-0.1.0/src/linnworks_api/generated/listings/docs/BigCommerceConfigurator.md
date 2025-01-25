# BigCommerceConfigurator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**List[BigCommerceConfigAttributes]**](BigCommerceConfigAttributes.md) |  | [optional] 
**option_set_name** | **str** |  | [optional] 
**var_attributes** | [**List[VarAttribute]**](VarAttribute.md) |  | [optional] 
**user_attributes** | [**List[ConfigUserAttributes]**](ConfigUserAttributes.md) |  | [optional] 
**pk_configid** | **str** |  | [optional] 
**categories** | [**List[ConfigCategory]**](ConfigCategory.md) |  | [optional] 
**site** | **str** |  | [optional] 
**config_name** | **str** |  | [optional] 
**category_extended_property** | **str** |  | [optional] 
**manage_stock** | **bool** |  | [optional] 
**show_in_inventory** | **bool** |  | [optional] 
**is_changed** | **bool** |  | [optional] 
**last_update_time** | **int** |  | [optional] 
**last_update_session_id** | **str** |  | [optional] 
**associated_single** | **int** |  | [optional] 
**associated_variation** | **int** |  | [optional] 
**total_attributes** | **int** |  | [optional] 
**total_var_attributes** | **int** |  | [optional] 
**var_title_ext_property** | **str** |  | [optional] 
**use_main_item_images** | **bool** |  | [optional] 
**glt_configurator_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.big_commerce_configurator import BigCommerceConfigurator

# TODO update the JSON string below
json = "{}"
# create an instance of BigCommerceConfigurator from a JSON string
big_commerce_configurator_instance = BigCommerceConfigurator.from_json(json)
# print the JSON string representation of the object
print(BigCommerceConfigurator.to_json())

# convert the object into a dict
big_commerce_configurator_dict = big_commerce_configurator_instance.to_dict()
# create an instance of BigCommerceConfigurator from a dict
big_commerce_configurator_from_dict = BigCommerceConfigurator.from_dict(big_commerce_configurator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


