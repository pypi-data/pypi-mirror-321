# EbayWeightRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabled** | **bool** |  | [optional] 
**from_weight** | **float** |  | [optional] 
**to_weight** | **float** |  | [optional] 
**price** | **float** |  | [optional] 
**additional_price** | **float** |  | [optional] 
**is_first** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.ebay_weight_rule import EbayWeightRule

# TODO update the JSON string below
json = "{}"
# create an instance of EbayWeightRule from a JSON string
ebay_weight_rule_instance = EbayWeightRule.from_json(json)
# print the JSON string representation of the object
print(EbayWeightRule.to_json())

# convert the object into a dict
ebay_weight_rule_dict = ebay_weight_rule_instance.to_dict()
# create an instance of EbayWeightRule from a dict
ebay_weight_rule_from_dict = EbayWeightRule.from_dict(ebay_weight_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


