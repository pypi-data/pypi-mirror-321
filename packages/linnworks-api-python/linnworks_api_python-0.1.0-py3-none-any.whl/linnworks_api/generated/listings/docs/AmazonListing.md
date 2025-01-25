# AmazonListing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **str** |  | [optional] 
**inventory_item_id** | **str** |  | [optional] 
**variation_group_name** | **str** |  | [optional] 
**version** | **int** |  | [optional] 
**merchant_name** | **str** |  | [optional] 
**config_id** | **str** |  | [optional] 
**config_name** | **str** |  | [optional] 
**product_url** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**asin** | **str** |  | [optional] 
**sku** | **str** |  | [optional] 
**barcode** | **str** |  | [optional] 
**barcode_type** | **str** |  | [optional] 
**title_source** | **str** |  | [optional] 
**price** | **float** |  | [optional] 
**business_price** | [**KeyValueGenericGuidDouble**](KeyValueGenericGuidDouble.md) |  | [optional] 
**quantity** | **int** |  | [optional] 
**category** | **str** |  | [optional] 
**sub_type** | **str** |  | [optional] 
**browse_nodes** | [**List[AmazonBNode]**](AmazonBNode.md) |  | [optional] 
**attributes** | [**List[AmazonAttribute]**](AmazonAttribute.md) |  | [optional] 
**pictures** | [**List[AmazonAttribute]**](AmazonAttribute.md) |  | [optional] 
**use_main_item_images** | **bool** |  | [optional] 
**variation_theme** | **str** |  | [optional] 
**variations** | [**List[AmazonVariation]**](AmazonVariation.md) |  | [optional] 
**old_variations** | [**List[AmazonVariation]**](AmazonVariation.md) |  | [optional] 
**status** | **str** |  | [optional] 
**is_read_only** | **bool** |  | [optional] 
**report_id** | **str** |  | [optional] 
**error_msg** | **str** |  | [optional] 
**message_ids** | **List[str]** |  | [optional] 
**ship_options** | **List[str]** |  | [optional] 
**is_catalog** | **bool** |  | [optional] 
**condition_type** | **str** |  | [optional] 
**condition_note** | **str** |  | [optional] 
**lowest_new_price_formated** | **str** |  | [optional] 
**decimal_sales_rank** | **float** |  | [optional] 
**to_list** | **bool** |  | [optional] 
**matches** | **int** |  | [optional] 
**no_matches** | **bool** |  | [optional] 
**adjustments** | **int** |  | [optional] 
**is_re_feeded** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.amazon_listing import AmazonListing

# TODO update the JSON string below
json = "{}"
# create an instance of AmazonListing from a JSON string
amazon_listing_instance = AmazonListing.from_json(json)
# print the JSON string representation of the object
print(AmazonListing.to_json())

# convert the object into a dict
amazon_listing_dict = amazon_listing_instance.to_dict()
# create an instance of AmazonListing from a dict
amazon_listing_from_dict = AmazonListing.from_dict(amazon_listing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


