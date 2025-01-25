# VariationsAttributesPrices


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**select_value** | **str** |  | [optional] 
**select_label** | **str** |  | [optional] 
**price_diff** | **float** |  | [optional] 
**is_fixed** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.variations_attributes_prices import VariationsAttributesPrices

# TODO update the JSON string below
json = "{}"
# create an instance of VariationsAttributesPrices from a JSON string
variations_attributes_prices_instance = VariationsAttributesPrices.from_json(json)
# print the JSON string representation of the object
print(VariationsAttributesPrices.to_json())

# convert the object into a dict
variations_attributes_prices_dict = variations_attributes_prices_instance.to_dict()
# create an instance of VariationsAttributesPrices from a dict
variations_attributes_prices_from_dict = VariationsAttributesPrices.from_dict(variations_attributes_prices_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


