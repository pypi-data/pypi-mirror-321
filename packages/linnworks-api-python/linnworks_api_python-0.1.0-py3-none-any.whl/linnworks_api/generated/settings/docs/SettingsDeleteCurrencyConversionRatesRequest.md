# SettingsDeleteCurrencyConversionRatesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currencies** | **List[str]** | Currencies to delete | [optional] 

## Example

```python
from linnworks_api.generated.settings.models.settings_delete_currency_conversion_rates_request import SettingsDeleteCurrencyConversionRatesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SettingsDeleteCurrencyConversionRatesRequest from a JSON string
settings_delete_currency_conversion_rates_request_instance = SettingsDeleteCurrencyConversionRatesRequest.from_json(json)
# print the JSON string representation of the object
print(SettingsDeleteCurrencyConversionRatesRequest.to_json())

# convert the object into a dict
settings_delete_currency_conversion_rates_request_dict = settings_delete_currency_conversion_rates_request_instance.to_dict()
# create an instance of SettingsDeleteCurrencyConversionRatesRequest from a dict
settings_delete_currency_conversion_rates_request_from_dict = SettingsDeleteCurrencyConversionRatesRequest.from_dict(settings_delete_currency_conversion_rates_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


