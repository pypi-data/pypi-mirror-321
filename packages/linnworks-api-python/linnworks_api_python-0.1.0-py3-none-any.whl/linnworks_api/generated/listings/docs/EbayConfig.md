# EbayConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_config_id** | **str** |  | [optional] 
**config_name** | **str** |  | [optional] 
**ebay_account** | **str** |  | [optional] 
**site** | **str** |  | [optional] 
**original_config_id** | **str** |  | [optional] 
**original_site** | **str** |  | [optional] 
**is_out_of_stock_feature_enabled** | **bool** |  | [optional] 
**max_quantity** | **int** |  | [optional] 
**min_quantity** | **int** |  | [optional] 
**max_quantity_per_buyer** | **int** |  | [optional] 
**is_max_quantity_per_buyer_enabled** | **bool** |  | [optional] 
**show_in_inventory** | **bool** |  | [optional] 
**associated_templates** | **int** |  | [optional] 
**associated_variations** | **int** |  | [optional] 
**listing_type** | **str** |  | [optional] 
**listing_duration** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**product_location_country** | **str** |  | [optional] 
**product_location** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**product_location_country_extended_property** | **str** |  | [optional] 
**product_location_extended_property** | **str** |  | [optional] 
**postal_code_extended_property** | **str** |  | [optional] 
**payment_methods** | [**List[KeyValue]**](KeyValue.md) |  | [optional] 
**paypal_email** | **str** |  | [optional] 
**cod_cost** | **float** |  | [optional] 
**is_immediate_payment_required** | **bool** |  | [optional] 
**in_store_pickup** | **bool** |  | [optional] 
**sold_one_bay** | **bool** |  | [optional] 
**return_accepted** | [**KeyValue**](KeyValue.md) |  | [optional] 
**return_refund** | [**KeyValue**](KeyValue.md) |  | [optional] 
**return_paid_by** | [**KeyValue**](KeyValue.md) |  | [optional] 
**return_within** | [**KeyValue**](KeyValue.md) |  | [optional] 
**restocking_fee** | [**KeyValue**](KeyValue.md) |  | [optional] 
**return_policy** | **str** |  | [optional] 
**additional_checkout_instructions** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**global_shipping_program** | **bool** |  | [optional] 
**promotional_shipping_discount** | **bool** |  | [optional] 
**international_promotional_shipping_discount** | **bool** |  | [optional] 
**domestic_shipping_rate_table** | **bool** |  | [optional] 
**international_shipping_rate_table** | **bool** |  | [optional] 
**domestic_shipping_profile_id** | **str** |  | [optional] 
**international_shipping_profile_id** | **str** |  | [optional] 
**domestic_shipping_profile_id_extended_property** | **str** |  | [optional] 
**international_shipping_profile_id_extended_property** | **str** |  | [optional] 
**maximum_dispatch_time** | [**KeyValue**](KeyValue.md) |  | [optional] 
**maximum_dispatch_time_extended_property** | **str** |  | [optional] 
**domestic_shippings** | [**List[Shipping]**](Shipping.md) |  | [optional] 
**international_shippings** | [**List[Shipping]**](Shipping.md) |  | [optional] 
**flat_calculated_shipping** | **str** |  | [optional] 
**shipping_package_type** | **str** |  | [optional] 
**excluded_locations** | **List[str]** |  | [optional] 
**shipping_locations** | **List[str]** |  | [optional] 
**free_calculated_shipping_service_id** | **str** |  | [optional] 
**is_extended_property_splittable** | **bool** |  | [optional] 
**is_auto_mapping_ext_prop_to_spec_enabled** | **bool** |  | [optional] 
**is_variation_specification_limit_increased** | **bool** |  | [optional] 
**is_catalog** | **bool** |  | [optional] 
**is_private_listing_enabled** | **bool** |  | [optional] 
**is_list_internationally_enabled** | **bool** |  | [optional] 
**is_best_offer_enabled** | **bool** |  | [optional] 
**is_tax_table_enabled** | **bool** |  | [optional] 
**is_vat_enabled** | **bool** |  | [optional] 
**vat** | **float** |  | [optional] 
**vat_extended_property** | **str** |  | [optional] 
**categories** | [**List[LinnworksEbayCategory]**](LinnworksEbayCategory.md) |  | [optional] 
**store_categories** | [**List[LinnworksEbayCategory]**](LinnworksEbayCategory.md) |  | [optional] 
**old_categories** | [**List[LinnworksEbayCategory]**](LinnworksEbayCategory.md) |  | [optional] 
**use_suggested_category** | **bool** |  | [optional] 
**auto_convert_categories** | **bool** |  | [optional] 
**primary_category_extended_property** | **str** |  | [optional] 
**secondary_category_extended_property** | **str** |  | [optional] 
**store_primary_category_extended_property** | **str** |  | [optional] 
**store_secondary_category_extended_property** | **str** |  | [optional] 
**variation_title_extended_property** | **str** |  | [optional] 
**condition** | [**KeyValue**](KeyValue.md) |  | [optional] 
**condition_extended_property** | **str** |  | [optional] 
**condition_note_extended_property** | **str** |  | [optional] 
**barcode_extended_property** | **str** |  | [optional] 
**multiple_identifiers_enabled** | **bool** |  | [optional] 
**multiple_product_identifiers** | **List[str]** |  | [optional] 
**specifications** | [**List[EbaySpecification]**](EbaySpecification.md) |  | [optional] 
**variations** | [**List[EbaySpecification]**](EbaySpecification.md) |  | [optional] 
**dont_use_variation_pictures** | **bool** |  | [optional] 
**photo_display_code_type** | **str** |  | [optional] 
**auto_select_images** | **bool** |  | [optional] 
**charity_organisation_id** | **str** |  | [optional] 
**charity_donation_percent** | **float** |  | [optional] 
**last_update_time** | **int** |  | [optional] 
**last_update_session_id** | **str** |  | [optional] 
**payment_profile** | [**EbaySellerProfile**](EbaySellerProfile.md) |  | [optional] 
**return_profile** | [**EbaySellerProfile**](EbaySellerProfile.md) |  | [optional] 
**shipping_profile** | [**EbaySellerProfile**](EbaySellerProfile.md) |  | [optional] 
**pickup_location_times** | [**List[PickupLocationTime]**](PickupLocationTime.md) |  | [optional] 
**is_configurator_edited** | **bool** |  | [optional] 
**is_mapping_configurator** | **bool** |  | [optional] 
**scheduling_enabled** | **bool** |  | [optional] 
**use_lots_enabled** | **bool** |  | [optional] 
**use_new_api** | **bool** |  | [optional] 
**channel_location_identifier** | **str** |  | [optional] 
**dimension_measure** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.ebay_config import EbayConfig

# TODO update the JSON string below
json = "{}"
# create an instance of EbayConfig from a JSON string
ebay_config_instance = EbayConfig.from_json(json)
# print the JSON string representation of the object
print(EbayConfig.to_json())

# convert the object into a dict
ebay_config_dict = ebay_config_instance.to_dict()
# create an instance of EbayConfig from a dict
ebay_config_from_dict = EbayConfig.from_dict(ebay_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


