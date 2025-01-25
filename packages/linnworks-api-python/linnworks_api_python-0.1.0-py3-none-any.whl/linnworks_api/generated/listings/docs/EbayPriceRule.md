# EbayPriceRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_price** | **float** |  | [optional] 
**to_price** | **float** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.ebay_price_rule import EbayPriceRule

# TODO update the JSON string below
json = "{}"
# create an instance of EbayPriceRule from a JSON string
ebay_price_rule_instance = EbayPriceRule.from_json(json)
# print the JSON string representation of the object
print(EbayPriceRule.to_json())

# convert the object into a dict
ebay_price_rule_dict = ebay_price_rule_instance.to_dict()
# create an instance of EbayPriceRule from a dict
ebay_price_rule_from_dict = EbayPriceRule.from_dict(ebay_price_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


