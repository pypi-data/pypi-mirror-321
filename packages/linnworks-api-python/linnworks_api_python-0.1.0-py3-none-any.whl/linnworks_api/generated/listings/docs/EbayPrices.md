# EbayPrices


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_price** | **float** |  | [optional] 
**reserve_price** | **float** |  | [optional] 
**bin_price** | **float** |  | [optional] 
**auto_accept** | **float** |  | [optional] 
**auto_decline** | **float** |  | [optional] 
**original_retail_price** | **float** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.ebay_prices import EbayPrices

# TODO update the JSON string below
json = "{}"
# create an instance of EbayPrices from a JSON string
ebay_prices_instance = EbayPrices.from_json(json)
# print the JSON string representation of the object
print(EbayPrices.to_json())

# convert the object into a dict
ebay_prices_dict = ebay_prices_instance.to_dict()
# create an instance of EbayPrices from a dict
ebay_prices_from_dict = EbayPrices.from_dict(ebay_prices_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


