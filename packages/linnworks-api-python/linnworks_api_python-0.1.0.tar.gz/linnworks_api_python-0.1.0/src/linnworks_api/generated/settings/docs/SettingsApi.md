# linnworks_api.generated.settings.SettingsApi

All URIs are relative to *https://eu-ext.linnworks.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_currency_conversion_rates**](SettingsApi.md#delete_currency_conversion_rates) | **POST** /api/Settings/DeleteCurrencyConversionRates | DeleteCurrencyConversionRates
[**get_available_time_zones**](SettingsApi.md#get_available_time_zones) | **GET** /api/Settings/GetAvailableTimeZones | GetAvailableTimeZones
[**get_currency_conversion_rates**](SettingsApi.md#get_currency_conversion_rates) | **GET** /api/Settings/GetCurrencyConversionRates | GetCurrencyConversionRates
[**get_latest_currency_rate**](SettingsApi.md#get_latest_currency_rate) | **GET** /api/Settings/GetLatestCurrencyRate | GetLatestCurrencyRate
[**get_measures**](SettingsApi.md#get_measures) | **GET** /api/Settings/GetMeasures | GetMeasures
[**insert_currency_conversion_rates**](SettingsApi.md#insert_currency_conversion_rates) | **POST** /api/Settings/InsertCurrencyConversionRates | InsertCurrencyConversionRates
[**update_currency_conversion_rates**](SettingsApi.md#update_currency_conversion_rates) | **POST** /api/Settings/UpdateCurrencyConversionRates | UpdateCurrencyConversionRates


# **delete_currency_conversion_rates**
> delete_currency_conversion_rates(settings_delete_currency_conversion_rates_request)

DeleteCurrencyConversionRates

Delete currency conversion rates <b>Permissions Required: </b> GlobalPermissions.Settings.CurrencyRates.EditCurrencyRatesNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.settings
from linnworks_api.generated.settings.models.settings_delete_currency_conversion_rates_request import SettingsDeleteCurrencyConversionRatesRequest
from linnworks_api.generated.settings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.settings.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.settings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.settings.SettingsApi(api_client)
    settings_delete_currency_conversion_rates_request = linnworks_api.generated.settings.SettingsDeleteCurrencyConversionRatesRequest() # SettingsDeleteCurrencyConversionRatesRequest | 

    try:
        # DeleteCurrencyConversionRates
        api_instance.delete_currency_conversion_rates(settings_delete_currency_conversion_rates_request)
    except Exception as e:
        print("Exception when calling SettingsApi->delete_currency_conversion_rates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_delete_currency_conversion_rates_request** | [**SettingsDeleteCurrencyConversionRatesRequest**](SettingsDeleteCurrencyConversionRatesRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_time_zones**
> GetAvailableTimeZonesResponse get_available_time_zones()

GetAvailableTimeZones

 <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.settings
from linnworks_api.generated.settings.models.get_available_time_zones_response import GetAvailableTimeZonesResponse
from linnworks_api.generated.settings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.settings.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.settings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.settings.SettingsApi(api_client)

    try:
        # GetAvailableTimeZones
        api_response = api_instance.get_available_time_zones()
        print("The response of SettingsApi->get_available_time_zones:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->get_available_time_zones: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetAvailableTimeZonesResponse**](GetAvailableTimeZonesResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_currency_conversion_rates**
> List[CurrencyConversionRate] get_currency_conversion_rates(get_currencies_from_orders=get_currencies_from_orders, currency=currency)

GetCurrencyConversionRates

Get Currency Conversion Rates <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>250</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.settings
from linnworks_api.generated.settings.models.currency_conversion_rate import CurrencyConversionRate
from linnworks_api.generated.settings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.settings.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.settings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.settings.SettingsApi(api_client)
    get_currencies_from_orders = True # bool | If you want to get currencies from orders (optional)
    currency = 'currency_example' # str | Currency (optional)

    try:
        # GetCurrencyConversionRates
        api_response = api_instance.get_currency_conversion_rates(get_currencies_from_orders=get_currencies_from_orders, currency=currency)
        print("The response of SettingsApi->get_currency_conversion_rates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->get_currency_conversion_rates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_currencies_from_orders** | **bool**| If you want to get currencies from orders | [optional] 
 **currency** | **str**| Currency | [optional] 

### Return type

[**List[CurrencyConversionRate]**](CurrencyConversionRate.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_currency_rate**
> GetLatestCurrencyRateResponse get_latest_currency_rate(base_currency=base_currency)

GetLatestCurrencyRate

Gets latest conversion rates for all known currencies. The rate is updated every couple of hours. <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.settings
from linnworks_api.generated.settings.models.get_latest_currency_rate_response import GetLatestCurrencyRateResponse
from linnworks_api.generated.settings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.settings.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.settings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.settings.SettingsApi(api_client)
    base_currency = 'base_currency_example' # str | Base currency for conversion rates, if null, USD is used (optional)

    try:
        # GetLatestCurrencyRate
        api_response = api_instance.get_latest_currency_rate(base_currency=base_currency)
        print("The response of SettingsApi->get_latest_currency_rate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->get_latest_currency_rate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_currency** | **str**| Base currency for conversion rates, if null, USD is used | [optional] 

### Return type

[**GetLatestCurrencyRateResponse**](GetLatestCurrencyRateResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_measures**
> Measures get_measures()

GetMeasures

Get user measures units from the database <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.settings
from linnworks_api.generated.settings.models.measures import Measures
from linnworks_api.generated.settings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.settings.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.settings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.settings.SettingsApi(api_client)

    try:
        # GetMeasures
        api_response = api_instance.get_measures()
        print("The response of SettingsApi->get_measures:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->get_measures: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Measures**](Measures.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_currency_conversion_rates**
> insert_currency_conversion_rates(settings_insert_currency_conversion_rates_request)

InsertCurrencyConversionRates

Insert currency conversion rates <b>Permissions Required: </b> GlobalPermissions.Settings.CurrencyRates.EditCurrencyRatesNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.settings
from linnworks_api.generated.settings.models.settings_insert_currency_conversion_rates_request import SettingsInsertCurrencyConversionRatesRequest
from linnworks_api.generated.settings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.settings.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.settings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.settings.SettingsApi(api_client)
    settings_insert_currency_conversion_rates_request = linnworks_api.generated.settings.SettingsInsertCurrencyConversionRatesRequest() # SettingsInsertCurrencyConversionRatesRequest | 

    try:
        # InsertCurrencyConversionRates
        api_instance.insert_currency_conversion_rates(settings_insert_currency_conversion_rates_request)
    except Exception as e:
        print("Exception when calling SettingsApi->insert_currency_conversion_rates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_insert_currency_conversion_rates_request** | [**SettingsInsertCurrencyConversionRatesRequest**](SettingsInsertCurrencyConversionRatesRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_currency_conversion_rates**
> update_currency_conversion_rates(settings_update_currency_conversion_rates_request)

UpdateCurrencyConversionRates

Update Currency Conversion Rates <b>Permissions Required: </b> GlobalPermissions.Settings.CurrencyRates.EditCurrencyRatesNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.settings
from linnworks_api.generated.settings.models.settings_update_currency_conversion_rates_request import SettingsUpdateCurrencyConversionRatesRequest
from linnworks_api.generated.settings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.settings.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.settings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.settings.SettingsApi(api_client)
    settings_update_currency_conversion_rates_request = linnworks_api.generated.settings.SettingsUpdateCurrencyConversionRatesRequest() # SettingsUpdateCurrencyConversionRatesRequest | 

    try:
        # UpdateCurrencyConversionRates
        api_instance.update_currency_conversion_rates(settings_update_currency_conversion_rates_request)
    except Exception as e:
        print("Exception when calling SettingsApi->update_currency_conversion_rates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_update_currency_conversion_rates_request** | [**SettingsUpdateCurrencyConversionRatesRequest**](SettingsUpdateCurrencyConversionRatesRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

