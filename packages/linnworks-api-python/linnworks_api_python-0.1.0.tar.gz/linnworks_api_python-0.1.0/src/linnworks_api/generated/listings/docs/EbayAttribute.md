# EbayAttribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr_name** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 
**current_product_value** | **str** |  | [optional] 
**is_user_defined** | **bool** |  | [optional] 
**is_required** | **bool** |  | [optional] 
**valid_values** | **List[str]** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.ebay_attribute import EbayAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of EbayAttribute from a JSON string
ebay_attribute_instance = EbayAttribute.from_json(json)
# print the JSON string representation of the object
print(EbayAttribute.to_json())

# convert the object into a dict
ebay_attribute_dict = ebay_attribute_instance.to_dict()
# create an instance of EbayAttribute from a dict
ebay_attribute_from_dict = EbayAttribute.from_dict(ebay_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


