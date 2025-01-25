# GetLatestCurrencyRateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_currency** | **str** | Base currency for conversion rates, if null, USD is used | [optional] 

## Example

```python
from linnworks_api.generated.settings.models.get_latest_currency_rate_request import GetLatestCurrencyRateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetLatestCurrencyRateRequest from a JSON string
get_latest_currency_rate_request_instance = GetLatestCurrencyRateRequest.from_json(json)
# print the JSON string representation of the object
print(GetLatestCurrencyRateRequest.to_json())

# convert the object into a dict
get_latest_currency_rate_request_dict = get_latest_currency_rate_request_instance.to_dict()
# create an instance of GetLatestCurrencyRateRequest from a dict
get_latest_currency_rate_request_from_dict = GetLatestCurrencyRateRequest.from_dict(get_latest_currency_rate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


