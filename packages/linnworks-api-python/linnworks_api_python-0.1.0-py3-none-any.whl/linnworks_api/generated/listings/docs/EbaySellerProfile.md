# EbaySellerProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_id** | **int** |  | [optional] 
**profile_type** | **str** |  | [optional] 
**profile_name** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 
**seller_profile_extended_property** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.ebay_seller_profile import EbaySellerProfile

# TODO update the JSON string below
json = "{}"
# create an instance of EbaySellerProfile from a JSON string
ebay_seller_profile_instance = EbaySellerProfile.from_json(json)
# print the JSON string representation of the object
print(EbaySellerProfile.to_json())

# convert the object into a dict
ebay_seller_profile_dict = ebay_seller_profile_instance.to_dict()
# create an instance of EbaySellerProfile from a dict
ebay_seller_profile_from_dict = EbaySellerProfile.from_dict(ebay_seller_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


