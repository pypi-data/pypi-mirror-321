# BigCommerceListing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adjustments** | **int** |  | [optional] 
**width** | **float** |  | [optional] 
**height** | **float** |  | [optional] 
**depth** | **float** |  | [optional] 
**attributes** | [**List[BigCommerceConfigAttributes]**](BigCommerceConfigAttributes.md) |  | [optional] 
**var_attributes** | [**List[VarAttribute]**](VarAttribute.md) |  | [optional] 
**children** | [**List[BigCommerceAssignedProducts]**](BigCommerceAssignedProducts.md) |  | [optional] 
**old_children** | [**List[BigCommerceAssignedProducts]**](BigCommerceAssignedProducts.md) |  | [optional] 
**option_set** | [**AssignedOptionSet**](AssignedOptionSet.md) |  | [optional] 
**images** | [**List[BigCommerceImageData]**](BigCommerceImageData.md) |  | [optional] 
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
**custom_fields** | [**List[BigCommerceCustomField]**](BigCommerceCustomField.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.big_commerce_listing import BigCommerceListing

# TODO update the JSON string below
json = "{}"
# create an instance of BigCommerceListing from a JSON string
big_commerce_listing_instance = BigCommerceListing.from_json(json)
# print the JSON string representation of the object
print(BigCommerceListing.to_json())

# convert the object into a dict
big_commerce_listing_dict = big_commerce_listing_instance.to_dict()
# create an instance of BigCommerceListing from a dict
big_commerce_listing_from_dict = BigCommerceListing.from_dict(big_commerce_listing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


