# EbayListingAudit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_number** | **str** |  | [optional] 
**action_type** | **str** |  | [optional] 
**action_text** | **str** |  | [optional] 
**affectivefk_stock_item_id** | **str** |  | [optional] 
**list_id** | **str** |  | [optional] 
**action_date_time** | **datetime** |  | [optional] 
**set_quantity** | **int** |  | [optional] 
**set_price** | **float** |  | [optional] 
**is_error** | **bool** |  | [optional] 
**sku** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.ebay_listing_audit import EbayListingAudit

# TODO update the JSON string below
json = "{}"
# create an instance of EbayListingAudit from a JSON string
ebay_listing_audit_instance = EbayListingAudit.from_json(json)
# print the JSON string representation of the object
print(EbayListingAudit.to_json())

# convert the object into a dict
ebay_listing_audit_dict = ebay_listing_audit_instance.to_dict()
# create an instance of EbayListingAudit from a dict
ebay_listing_audit_from_dict = EbayListingAudit.from_dict(ebay_listing_audit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


