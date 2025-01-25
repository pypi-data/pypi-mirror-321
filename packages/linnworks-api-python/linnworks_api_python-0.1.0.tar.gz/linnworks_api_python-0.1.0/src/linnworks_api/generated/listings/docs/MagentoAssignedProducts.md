# MagentoAssignedProducts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**child_id** | **str** |  | [optional] 
**collision_number** | **int** |  | [optional] 
**add_website** | **bool** |  | [optional] 
**is_assigned** | **bool** |  | [optional] 
**custom_price** | **bool** |  | [optional] 
**calculated_price** | **float** |  | [optional] 
**converted_weight** | **float** |  | [optional] 
**attributes** | [**List[ListingAttributes]**](ListingAttributes.md) |  | [optional] 
**identifier_type** | **str** |  | [optional] 
**version** | **int** |  | [optional] 
**listing_id** | **str** |  | [optional] 
**template_id** | **str** |  | [optional] 
**inventory_item_id** | **str** |  | [optional] 
**config_id** | **str** |  | [optional] 
**used_config_name** | **str** |  | [optional] 
**product_id** | **int** |  | [optional] 
**update_config** | **bool** |  | [optional] 
**type** | **str** |  | [optional] 
**listing_url** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**short_description** | **str** |  | [optional] 
**sku** | **str** |  | [optional] 
**barcode** | **str** |  | [optional] 
**title_source** | **str** |  | [optional] 
**price** | **float** |  | [optional] 
**weight** | **float** |  | [optional] 
**show_listing** | **bool** |  | [optional] 
**manage_stock** | **bool** |  | [optional] 
**quantity** | **int** |  | [optional] 
**is_read_only** | **bool** |  | [optional] 
**categories** | [**List[ConfigCategory]**](ConfigCategory.md) |  | [optional] 
**has_collisions** | **bool** |  | [optional] 
**use_main_item_images** | **bool** |  | [optional] 
**status** | **str** |  | [optional] 
**site** | **str** |  | [optional] 
**is_error_msg** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.magento_assigned_products import MagentoAssignedProducts

# TODO update the JSON string below
json = "{}"
# create an instance of MagentoAssignedProducts from a JSON string
magento_assigned_products_instance = MagentoAssignedProducts.from_json(json)
# print the JSON string representation of the object
print(MagentoAssignedProducts.to_json())

# convert the object into a dict
magento_assigned_products_dict = magento_assigned_products_instance.to_dict()
# create an instance of MagentoAssignedProducts from a dict
magento_assigned_products_from_dict = MagentoAssignedProducts.from_dict(magento_assigned_products_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


