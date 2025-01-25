# AmazonConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fulfillment_type** | **str** |  | [optional] 
**fulfillment_extended_property_name** | **str** |  | [optional] 
**pk_config_id** | **str** |  | [optional] 
**config_name** | **str** |  | [optional] 
**version** | **int** |  | [optional] 
**site** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**sub_type** | **str** |  | [optional] 
**associated_templates** | **int** |  | [optional] 
**associated_variations** | **int** |  | [optional] 
**picture_attributes** | [**List[AmazonAttribute]**](AmazonAttribute.md) |  | [optional] 
**attributes** | [**List[AmazonAttribute]**](AmazonAttribute.md) |  | [optional] 
**variation_theme_attribute** | [**AmazonAttribute**](AmazonAttribute.md) |  | [optional] 
**parentage_attribute** | [**AmazonAttribute**](AmazonAttribute.md) |  | [optional] 
**variation_theme** | **str** |  | [optional] 
**variations** | [**List[AmazonAttribute]**](AmazonAttribute.md) |  | [optional] 
**browse_nodes** | [**List[AmazonBNode]**](AmazonBNode.md) |  | [optional] 
**contains_browse_nodes** | **bool** |  | [optional] 
**first_browse_node_extended_property** | **str** |  | [optional] 
**second_browse_node_extended_property** | **str** |  | [optional] 
**variation_title_extended_property** | **str** |  | [optional] 
**is_configurator_edited** | **bool** |  | [optional] 
**show_in_inventory** | **bool** |  | [optional] 
**last_update_time** | **int** |  | [optional] 
**last_update_session_id** | **str** |  | [optional] 
**shipping_override_method** | **str** |  | [optional] 
**shipping_option** | [**SimpleShipping**](SimpleShipping.md) |  | [optional] 
**shippings** | [**List[AmazonShipping]**](AmazonShipping.md) |  | [optional] 
**use_main_item_images** | **bool** |  | [optional] 
**ignore_incorrect_variation_children** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.amazon_config import AmazonConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AmazonConfig from a JSON string
amazon_config_instance = AmazonConfig.from_json(json)
# print the JSON string representation of the object
print(AmazonConfig.to_json())

# convert the object into a dict
amazon_config_dict = amazon_config_instance.to_dict()
# create an instance of AmazonConfig from a dict
amazon_config_from_dict = AmazonConfig.from_dict(amazon_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


