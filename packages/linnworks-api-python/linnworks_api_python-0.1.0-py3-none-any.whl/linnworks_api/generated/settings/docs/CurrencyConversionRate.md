# CurrencyConversionRate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** |  | [optional] 
**conversion_rate** | **float** |  | [optional] 

## Example

```python
from linnworks_api.generated.settings.models.currency_conversion_rate import CurrencyConversionRate

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyConversionRate from a JSON string
currency_conversion_rate_instance = CurrencyConversionRate.from_json(json)
# print the JSON string representation of the object
print(CurrencyConversionRate.to_json())

# convert the object into a dict
currency_conversion_rate_dict = currency_conversion_rate_instance.to_dict()
# create an instance of CurrencyConversionRate from a dict
currency_conversion_rate_from_dict = CurrencyConversionRate.from_dict(currency_conversion_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


