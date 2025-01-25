# SettingsUpdateCurrencyConversionRatesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rates** | [**List[CurrencyConversionRate]**](CurrencyConversionRate.md) | Rates to update. Currency is the key | [optional] 

## Example

```python
from linnworks_api.generated.settings.models.settings_update_currency_conversion_rates_request import SettingsUpdateCurrencyConversionRatesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SettingsUpdateCurrencyConversionRatesRequest from a JSON string
settings_update_currency_conversion_rates_request_instance = SettingsUpdateCurrencyConversionRatesRequest.from_json(json)
# print the JSON string representation of the object
print(SettingsUpdateCurrencyConversionRatesRequest.to_json())

# convert the object into a dict
settings_update_currency_conversion_rates_request_dict = settings_update_currency_conversion_rates_request_instance.to_dict()
# create an instance of SettingsUpdateCurrencyConversionRatesRequest from a dict
settings_update_currency_conversion_rates_request_from_dict = SettingsUpdateCurrencyConversionRatesRequest.from_dict(settings_update_currency_conversion_rates_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


