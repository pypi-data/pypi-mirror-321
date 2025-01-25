# linnworks_api.generated.warehousetransfer_new.FbaShippingLocationApi

All URIs are relative to *https://eu-api.linnworks.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**warehousetransfer_fbainbound_fbashippinglocations_contact_put**](FbaShippingLocationApi.md#warehousetransfer_fbainbound_fbashippinglocations_contact_put) | **PUT** /warehousetransfer/fbainbound/fbashippinglocations/contact | UpdateShippingLocationContact
[**warehousetransfer_fbainbound_fbashippinglocations_countries_get**](FbaShippingLocationApi.md#warehousetransfer_fbainbound_fbashippinglocations_countries_get) | **GET** /warehousetransfer/fbainbound/fbashippinglocations/countries | GetCountries
[**warehousetransfer_fbainbound_fbashippinglocations_stock_location_id_contact_get**](FbaShippingLocationApi.md#warehousetransfer_fbainbound_fbashippinglocations_stock_location_id_contact_get) | **GET** /warehousetransfer/fbainbound/fbashippinglocations/{stockLocationId}/contact | GetShippingLocationContactDetails


# **warehousetransfer_fbainbound_fbashippinglocations_contact_put**
> warehousetransfer_fbainbound_fbashippinglocations_contact_put(update_shipping_location_contact_request=update_shipping_location_contact_request)

UpdateShippingLocationContact

Used to update shipping location address<br>Deprecated - please use v2 - [API Docs v2](https://apidocs.linnworks.net/v2/)

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.update_shipping_location_contact_request import UpdateShippingLocationContactRequest
from linnworks_api.generated.warehousetransfer_new.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-api.linnworks.net/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.warehousetransfer_new.Configuration(
    host = "https://eu-api.linnworks.net/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Linnworks
configuration.api_key['Linnworks'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Linnworks'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.warehousetransfer_new.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.warehousetransfer_new.FbaShippingLocationApi(api_client)
    update_shipping_location_contact_request = linnworks_api.generated.warehousetransfer_new.UpdateShippingLocationContactRequest() # UpdateShippingLocationContactRequest |  (optional)

    try:
        # UpdateShippingLocationContact
        api_instance.warehousetransfer_fbainbound_fbashippinglocations_contact_put(update_shipping_location_contact_request=update_shipping_location_contact_request)
    except Exception as e:
        print("Exception when calling FbaShippingLocationApi->warehousetransfer_fbainbound_fbashippinglocations_contact_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_shipping_location_contact_request** | [**UpdateShippingLocationContactRequest**](UpdateShippingLocationContactRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Linnworks](../README.md#Linnworks)

### HTTP request headers

 - **Content-Type**: application/json-patch+json; x-api-version=1.0, application/json; x-api-version=1.0, text/json; x-api-version=1.0, application/*+json; x-api-version=1.0
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehousetransfer_fbainbound_fbashippinglocations_countries_get**
> List[GetCountriesResponse] warehousetransfer_fbainbound_fbashippinglocations_countries_get()

GetCountries

Used to get list of contries<br>Deprecated - please use v2 - [API Docs v2](https://apidocs.linnworks.net/v2/)

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.get_countries_response import GetCountriesResponse
from linnworks_api.generated.warehousetransfer_new.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-api.linnworks.net/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.warehousetransfer_new.Configuration(
    host = "https://eu-api.linnworks.net/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Linnworks
configuration.api_key['Linnworks'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Linnworks'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.warehousetransfer_new.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.warehousetransfer_new.FbaShippingLocationApi(api_client)

    try:
        # GetCountries
        api_response = api_instance.warehousetransfer_fbainbound_fbashippinglocations_countries_get()
        print("The response of FbaShippingLocationApi->warehousetransfer_fbainbound_fbashippinglocations_countries_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FbaShippingLocationApi->warehousetransfer_fbainbound_fbashippinglocations_countries_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GetCountriesResponse]**](GetCountriesResponse.md)

### Authorization

[Linnworks](../README.md#Linnworks)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehousetransfer_fbainbound_fbashippinglocations_stock_location_id_contact_get**
> ShippingLocationModel warehousetransfer_fbainbound_fbashippinglocations_stock_location_id_contact_get(stock_location_id)

GetShippingLocationContactDetails

Used to get shipping location address<br>Deprecated - please use v2 - [API Docs v2](https://apidocs.linnworks.net/v2/)

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.shipping_location_model import ShippingLocationModel
from linnworks_api.generated.warehousetransfer_new.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-api.linnworks.net/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.warehousetransfer_new.Configuration(
    host = "https://eu-api.linnworks.net/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Linnworks
configuration.api_key['Linnworks'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Linnworks'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.warehousetransfer_new.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.warehousetransfer_new.FbaShippingLocationApi(api_client)
    stock_location_id = 'stock_location_id_example' # str | 

    try:
        # GetShippingLocationContactDetails
        api_response = api_instance.warehousetransfer_fbainbound_fbashippinglocations_stock_location_id_contact_get(stock_location_id)
        print("The response of FbaShippingLocationApi->warehousetransfer_fbainbound_fbashippinglocations_stock_location_id_contact_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FbaShippingLocationApi->warehousetransfer_fbainbound_fbashippinglocations_stock_location_id_contact_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_location_id** | **str**|  | 

### Return type

[**ShippingLocationModel**](ShippingLocationModel.md)

### Authorization

[Linnworks](../README.md#Linnworks)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

