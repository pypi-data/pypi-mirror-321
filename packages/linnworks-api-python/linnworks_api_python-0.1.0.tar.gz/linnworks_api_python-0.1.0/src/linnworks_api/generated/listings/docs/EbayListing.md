# EbayListing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_created_with_mapping_tool** | **bool** |  | [optional] 
**template_id** | **str** |  | [optional] 
**inventory_item_id** | **str** |  | [optional] 
**variation_group_name** | **str** |  | [optional] 
**config_id** | **str** |  | [optional] 
**config_name** | **str** |  | [optional] 
**listing_ids** | **List[str]** |  | [optional] 
**sku** | **str** |  | [optional] 
**account_id** | **str** |  | [optional] 
**barcode** | **str** |  | [optional] 
**barcode_error_message** | **str** |  | [optional] 
**multiple_identifiers** | [**List[KeyValue]**](KeyValue.md) |  | [optional] 
**price** | [**EbayPrices**](EbayPrices.md) |  | [optional] 
**available_quantity** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**sub_title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**e_pid** | **str** |  | [optional] 
**is_catalog_match** | **bool** |  | [optional] 
**is_product_required** | **bool** |  | [optional] 
**attributes** | [**List[EbayAttribute]**](EbayAttribute.md) |  | [optional] 
**pictures** | [**List[ImageData]**](ImageData.md) |  | [optional] 
**categories** | [**List[LinnworksEbayCategory]**](LinnworksEbayCategory.md) |  | [optional] 
**store_categories** | [**List[LinnworksEbayCategory]**](LinnworksEbayCategory.md) |  | [optional] 
**dont_use_variation_pictures** | **bool** |  | [optional] 
**variation_picture_specific** | **str** |  | [optional] 
**variations** | [**List[EbayVariation]**](EbayVariation.md) |  | [optional] 
**variations_positions** | [**List[KeyList]**](KeyList.md) |  | [optional] 
**old_variations** | [**List[EbayVariation]**](EbayVariation.md) |  | [optional] 
**old_variation_specifics** | [**List[KeyList]**](KeyList.md) |  | [optional] 
**is_product_confirmation_required** | **bool** |  | [optional] 
**status** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 
**adjustments** | **int** |  | [optional] 
**title_source** | **str** |  | [optional] 
**is_pending_relist** | **bool** |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**is_read_only** | **bool** |  | [optional] 
**is_virtual_template** | **bool** |  | [optional] 
**site** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**use_suggested_category** | **bool** |  | [optional] 
**allow_category_change** | **bool** |  | [optional] 
**lot_size** | **int** |  | [optional] 
**is_recommendation** | **bool** |  | [optional] 
**recommendation_message** | **str** |  | [optional] 
**use_new_api** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.ebay_listing import EbayListing

# TODO update the JSON string below
json = "{}"
# create an instance of EbayListing from a JSON string
ebay_listing_instance = EbayListing.from_json(json)
# print the JSON string representation of the object
print(EbayListing.to_json())

# convert the object into a dict
ebay_listing_dict = ebay_listing_instance.to_dict()
# create an instance of EbayListing from a dict
ebay_listing_from_dict = EbayListing.from_dict(ebay_listing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


