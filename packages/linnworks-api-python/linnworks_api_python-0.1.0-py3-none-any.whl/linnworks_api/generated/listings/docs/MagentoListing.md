# MagentoListing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adjustments** | **int** |  | [optional] 
**images** | [**List[MagentoImageData]**](MagentoImageData.md) |  | [optional] 
**var_attributes** | [**List[MagentoVariationsAttributes]**](MagentoVariationsAttributes.md) |  | [optional] 
**attributes_set_id** | **str** |  | [optional] 
**attributes_set_name** | **str** |  | [optional] 
**parent_template_id** | **str** |  | [optional] 
**related_products** | [**List[RelatedProduct]**](RelatedProduct.md) |  | [optional] 
**old_related_products** | [**List[RelatedProduct]**](RelatedProduct.md) |  | [optional] 
**associated_templates** | [**List[AssociatedTemplate]**](AssociatedTemplate.md) |  | [optional] 
**children** | [**List[MagentoAssignedProducts]**](MagentoAssignedProducts.md) |  | [optional] 
**old_children** | [**List[MagentoAssignedProducts]**](MagentoAssignedProducts.md) |  | [optional] 
**children_images** | [**List[ChildImagesList]**](ChildImagesList.md) |  | [optional] 
**store** | **str** |  | [optional] 
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
from linnworks_api.generated.listings.models.magento_listing import MagentoListing

# TODO update the JSON string below
json = "{}"
# create an instance of MagentoListing from a JSON string
magento_listing_instance = MagentoListing.from_json(json)
# print the JSON string representation of the object
print(MagentoListing.to_json())

# convert the object into a dict
magento_listing_dict = magento_listing_instance.to_dict()
# create an instance of MagentoListing from a dict
magento_listing_from_dict = MagentoListing.from_dict(magento_listing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


