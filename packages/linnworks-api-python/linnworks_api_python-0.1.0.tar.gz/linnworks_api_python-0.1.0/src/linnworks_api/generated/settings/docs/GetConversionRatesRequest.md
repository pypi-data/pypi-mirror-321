# GetConversionRatesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**get_currencies_from_orders** | **bool** | If you want to get currencies from orders | [optional] 
**currency** | **str** | Currency | [optional] 

## Example

```python
from linnworks_api.generated.settings.models.get_conversion_rates_request import GetConversionRatesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetConversionRatesRequest from a JSON string
get_conversion_rates_request_instance = GetConversionRatesRequest.from_json(json)
# print the JSON string representation of the object
print(GetConversionRatesRequest.to_json())

# convert the object into a dict
get_conversion_rates_request_dict = get_conversion_rates_request_instance.to_dict()
# create an instance of GetConversionRatesRequest from a dict
get_conversion_rates_request_from_dict = GetConversionRatesRequest.from_dict(get_conversion_rates_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


