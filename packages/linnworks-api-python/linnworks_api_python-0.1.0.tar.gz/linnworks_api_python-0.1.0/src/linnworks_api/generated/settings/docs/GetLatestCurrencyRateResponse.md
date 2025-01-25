# GetLatestCurrencyRateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_currency** | **str** |  | [optional] 
**rates** | [**List[CurrencyRate]**](CurrencyRate.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.settings.models.get_latest_currency_rate_response import GetLatestCurrencyRateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetLatestCurrencyRateResponse from a JSON string
get_latest_currency_rate_response_instance = GetLatestCurrencyRateResponse.from_json(json)
# print the JSON string representation of the object
print(GetLatestCurrencyRateResponse.to_json())

# convert the object into a dict
get_latest_currency_rate_response_dict = get_latest_currency_rate_response_instance.to_dict()
# create an instance of GetLatestCurrencyRateResponse from a dict
get_latest_currency_rate_response_from_dict = GetLatestCurrencyRateResponse.from_dict(get_latest_currency_rate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


