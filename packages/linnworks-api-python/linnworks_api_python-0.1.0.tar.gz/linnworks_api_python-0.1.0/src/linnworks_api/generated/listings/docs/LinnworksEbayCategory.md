# LinnworksEbayCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_default** | **bool** |  | [optional] 
**lot_size_disabled** | **bool** |  | [optional] 
**is_product_required** | **bool** |  | [optional] 
**variations_enabled** | **bool** |  | [optional] 
**site_supported** | **bool** |  | [optional] 
**category_id** | **str** |  | [optional] 
**category_name** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.linnworks_ebay_category import LinnworksEbayCategory

# TODO update the JSON string below
json = "{}"
# create an instance of LinnworksEbayCategory from a JSON string
linnworks_ebay_category_instance = LinnworksEbayCategory.from_json(json)
# print the JSON string representation of the object
print(LinnworksEbayCategory.to_json())

# convert the object into a dict
linnworks_ebay_category_dict = linnworks_ebay_category_instance.to_dict()
# create an instance of LinnworksEbayCategory from a dict
linnworks_ebay_category_from_dict = LinnworksEbayCategory.from_dict(linnworks_ebay_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


