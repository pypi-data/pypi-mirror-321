# MagentoConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manage_images** | **bool** |  | [optional] 
**store** | **str** |  | [optional] 
**attribute_set_name** | **str** |  | [optional] 
**attribute_set_id** | **str** |  | [optional] 
**up_sells_extended_property** | **str** |  | [optional] 
**create_up_sell_backlink** | **bool** |  | [optional] 
**related_extended_property** | **str** |  | [optional] 
**create_related_backlink** | **bool** |  | [optional] 
**cross_sells_extended_property** | **str** |  | [optional] 
**create_cross_sell_backlink** | **bool** |  | [optional] 
**grouped_extended_property** | **str** |  | [optional] 
**create_grouped_backlink** | **bool** |  | [optional] 
**attributes** | [**List[MagentoConfigAttributes]**](MagentoConfigAttributes.md) |  | [optional] 
**var_attributes** | [**List[MagentoVariationsAttributes]**](MagentoVariationsAttributes.md) |  | [optional] 
**is_children_images** | **bool** |  | [optional] 
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
from linnworks_api.generated.listings.models.magento_config import MagentoConfig

# TODO update the JSON string below
json = "{}"
# create an instance of MagentoConfig from a JSON string
magento_config_instance = MagentoConfig.from_json(json)
# print the JSON string representation of the object
print(MagentoConfig.to_json())

# convert the object into a dict
magento_config_dict = magento_config_instance.to_dict()
# create an instance of MagentoConfig from a dict
magento_config_from_dict = MagentoConfig.from_dict(magento_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


