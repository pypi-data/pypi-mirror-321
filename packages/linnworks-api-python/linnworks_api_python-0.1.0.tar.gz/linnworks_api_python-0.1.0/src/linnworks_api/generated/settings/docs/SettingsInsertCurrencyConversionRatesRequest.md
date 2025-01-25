# SettingsInsertCurrencyConversionRatesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rates** | [**List[CurrencyConversionRate]**](CurrencyConversionRate.md) | Currencies to insert | [optional] 

## Example

```python
from linnworks_api.generated.settings.models.settings_insert_currency_conversion_rates_request import SettingsInsertCurrencyConversionRatesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SettingsInsertCurrencyConversionRatesRequest from a JSON string
settings_insert_currency_conversion_rates_request_instance = SettingsInsertCurrencyConversionRatesRequest.from_json(json)
# print the JSON string representation of the object
print(SettingsInsertCurrencyConversionRatesRequest.to_json())

# convert the object into a dict
settings_insert_currency_conversion_rates_request_dict = settings_insert_currency_conversion_rates_request_instance.to_dict()
# create an instance of SettingsInsertCurrencyConversionRatesRequest from a dict
settings_insert_currency_conversion_rates_request_from_dict = SettingsInsertCurrencyConversionRatesRequest.from_dict(settings_insert_currency_conversion_rates_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


