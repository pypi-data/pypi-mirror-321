# AnyConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_version** | [**ConfigItemString**](ConfigItemString.md) |  | [optional] 
**enabled** | [**ConfigItemBoolean**](ConfigItemBoolean.md) |  | [optional] 
**channel_tag** | [**ConfigItemString**](ConfigItemString.md) |  | [optional] 
**channel_location_binding** | [**ConfigChannelLocationBinding**](ConfigChannelLocationBinding.md) |  | [optional] 
**is_multi_location** | [**ConfigItemBoolean**](ConfigItemBoolean.md) |  | [optional] 
**auto_populated_locations** | [**ConfigItemBoolean**](ConfigItemBoolean.md) |  | [optional] 
**can_modify_locations_on_channel** | [**ConfigItemBoolean**](ConfigItemBoolean.md) |  | [optional] 
**bopis_supported** | [**ConfigItemBoolean**](ConfigItemBoolean.md) |  | [optional] 
**process_pos_orders** | [**ConfigPropertyBoolean**](ConfigPropertyBoolean.md) |  | [optional] 
**despatch_notes** | [**ConfigItemBoolean**](ConfigItemBoolean.md) |  | [optional] 
**cancellation_notes** | [**ConfigItemBoolean**](ConfigItemBoolean.md) |  | [optional] 
**auto_respond_cancellation_requests** | [**ConfigItemBoolean**](ConfigItemBoolean.md) |  | [optional] 
**cancellation_response_type** | [**ConfigPropertySelectionListSelectStringValueOptionString**](ConfigPropertySelectionListSelectStringValueOptionString.md) |  | [optional] 
**refund_notes** | [**ConfigItemBoolean**](ConfigItemBoolean.md) |  | [optional] 
**download_refunds** | [**ConfigItemBoolean**](ConfigItemBoolean.md) |  | [optional] 
**return_notes** | [**ConfigItemBoolean**](ConfigItemBoolean.md) |  | [optional] 
**download_returns** | [**ConfigItemBoolean**](ConfigItemBoolean.md) |  | [optional] 
**order_save_location** | [**ConfigPropertySelectionListSelectStringValueOptionGuid**](ConfigPropertySelectionListSelectStringValueOptionGuid.md) |  | [optional] 
**order_sync_date** | [**ConfigItemDateTime**](ConfigItemDateTime.md) |  | [optional] 
**order_cancellation_check_date** | [**ConfigItemDateTime**](ConfigItemDateTime.md) |  | [optional] 
**config_discount** | [**ConfigPropertySelectionListSelectStringValueOptionString**](ConfigPropertySelectionListSelectStringValueOptionString.md) |  | [optional] 
**order_download_error_count** | [**ConfigItemInt32**](ConfigItemInt32.md) |  | [optional] 
**order_download_global_error_count** | [**ConfigItemInt32**](ConfigItemInt32.md) |  | [optional] 
**order_despatch_error_count** | [**ConfigItemInt32**](ConfigItemInt32.md) |  | [optional] 
**order_despatch_global_error_count** | [**ConfigItemInt32**](ConfigItemInt32.md) |  | [optional] 
**order_cancellation_check_error_count** | [**ConfigItemInt32**](ConfigItemInt32.md) |  | [optional] 
**order_cancellation_check_global_error_count** | [**ConfigItemInt32**](ConfigItemInt32.md) |  | [optional] 
**rma_download_error_count** | [**ConfigItemInt32**](ConfigItemInt32.md) |  | [optional] 
**rma_download_global_error_count** | [**ConfigItemInt32**](ConfigItemInt32.md) |  | [optional] 
**hides_header_attributes** | [**ConfigPropertyBoolean**](ConfigPropertyBoolean.md) |  | [optional] 
**inventory_sync** | [**ConfigItemBoolean**](ConfigItemBoolean.md) |  | [optional] 
**stock_location_binding** | [**ConfigStockLocationBinding**](ConfigStockLocationBinding.md) |  | [optional] 
**max_listed** | [**ConfigItemInt32**](ConfigItemInt32.md) |  | [optional] 
**stock_percentage** | [**ConfigItemDouble**](ConfigItemDouble.md) |  | [optional] 
**end_when** | [**ConfigItemInt32**](ConfigItemInt32.md) |  | [optional] 
**inv_sync_error_count** | [**ConfigItemInt32**](ConfigItemInt32.md) |  | [optional] 
**extract_inventory** | [**ConfigPropertyBoolean**](ConfigPropertyBoolean.md) |  | [optional] 
**extract_inventory_variation_mapping_property_name** | [**ConfigPropertyString**](ConfigPropertyString.md) |  | [optional] 
**price_change** | [**ConfigItemBoolean**](ConfigItemBoolean.md) |  | [optional] 
**price_change_error_count** | [**ConfigItemInt32**](ConfigItemInt32.md) |  | [optional] 
**is_inventory_sync_trigger_enabled** | [**ConfigPropertyBoolean**](ConfigPropertyBoolean.md) |  | [optional] 
**is_listing_scan_running** | [**ConfigItemBoolean**](ConfigItemBoolean.md) |  | [optional] 
**listing_scan_start_update_date** | [**ConfigItemDateTime**](ConfigItemDateTime.md) |  | [optional] 
**last_listing_update_date** | [**ConfigItemDateTime**](ConfigItemDateTime.md) |  | [optional] 
**estimated_inventory_scan_complete** | [**ConfigItemDateTime**](ConfigItemDateTime.md) |  | [optional] 
**is_header_only** | **bool** |  | [optional] [readonly] 
**is_hidden** | **bool** |  | [optional] 
**display_name** | **str** |  | [optional] [readonly] 
**dynamic_properties** | [**List[ConfigItemExternal]**](ConfigItemExternal.md) |  | [optional] 
**config_discount_typed** | **str** |  | [optional] 
**postal_service_mapping** | [**ConfigPostalServiceMapping**](ConfigPostalServiceMapping.md) |  | [optional] 
**payment_method_mapping** | [**ConfigPaymentMethodMapping**](ConfigPaymentMethodMapping.md) |  | [optional] 
**pk_channel_id** | **int** |  | [optional] 
**source** | **str** |  | [optional] [readonly] 
**source_type** | **str** |  | [optional] [readonly] 
**fulfillment_service_enabled** | **bool** |  | [optional] [readonly] 
**fulfillment_location** | **str** |  | [optional] [readonly] 
**concurrency_key** | **str** |  | [optional] [readonly] 
**rules** | [**List[ConfigRule]**](ConfigRule.md) |  | [optional] [readonly] 
**buttons** | [**List[ConfigButton]**](ConfigButton.md) |  | [optional] [readonly] 
**sub_source** | **str** |  | [optional] 
**header_audit_values** | [**List[ChannelSettingAudit]**](ChannelSettingAudit.md) |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.inventory.models.any_config import AnyConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AnyConfig from a JSON string
any_config_instance = AnyConfig.from_json(json)
# print the JSON string representation of the object
print(AnyConfig.to_json())

# convert the object into a dict
any_config_dict = any_config_instance.to_dict()
# create an instance of AnyConfig from a dict
any_config_from_dict = AnyConfig.from_dict(any_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


