# linnworks_api.generated.postalservices.PostalServicesApi

All URIs are relative to *https://eu-ext.linnworks.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_postal_service**](PostalServicesApi.md#create_postal_service) | **POST** /api/PostalServices/CreatePostalService | CreatePostalService
[**delete_postal_service**](PostalServicesApi.md#delete_postal_service) | **POST** /api/PostalServices/DeletePostalService | DeletePostalService
[**get_channel_links**](PostalServicesApi.md#get_channel_links) | **GET** /api/PostalServices/GetChannelLinks | GetChannelLinks
[**get_postal_services**](PostalServicesApi.md#get_postal_services) | **GET** /api/PostalServices/GetPostalServices | GetPostalServices
[**update_postal_service**](PostalServicesApi.md#update_postal_service) | **POST** /api/PostalServices/UpdatePostalService | UpdatePostalService


# **create_postal_service**
> PostalService create_postal_service(postal_services_create_postal_service_request)

CreatePostalService

Adds a new postal service to the database <b>Permissions Required: </b> GlobalPermissions.ShippingService.PostalServicesNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.postalservices
from linnworks_api.generated.postalservices.models.postal_service import PostalService
from linnworks_api.generated.postalservices.models.postal_services_create_postal_service_request import PostalServicesCreatePostalServiceRequest
from linnworks_api.generated.postalservices.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.postalservices.Configuration(
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
with linnworks_api.generated.postalservices.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.postalservices.PostalServicesApi(api_client)
    postal_services_create_postal_service_request = linnworks_api.generated.postalservices.PostalServicesCreatePostalServiceRequest() # PostalServicesCreatePostalServiceRequest | 

    try:
        # CreatePostalService
        api_response = api_instance.create_postal_service(postal_services_create_postal_service_request)
        print("The response of PostalServicesApi->create_postal_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostalServicesApi->create_postal_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **postal_services_create_postal_service_request** | [**PostalServicesCreatePostalServiceRequest**](PostalServicesCreatePostalServiceRequest.md)|  | 

### Return type

[**PostalService**](PostalService.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_postal_service**
> delete_postal_service(postal_services_delete_postal_service_request)

DeletePostalService

Changes an existing postal service in the database <b>Permissions Required: </b> GlobalPermissions.ShippingService.PostalServicesNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.postalservices
from linnworks_api.generated.postalservices.models.postal_services_delete_postal_service_request import PostalServicesDeletePostalServiceRequest
from linnworks_api.generated.postalservices.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.postalservices.Configuration(
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
with linnworks_api.generated.postalservices.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.postalservices.PostalServicesApi(api_client)
    postal_services_delete_postal_service_request = linnworks_api.generated.postalservices.PostalServicesDeletePostalServiceRequest() # PostalServicesDeletePostalServiceRequest | 

    try:
        # DeletePostalService
        api_instance.delete_postal_service(postal_services_delete_postal_service_request)
    except Exception as e:
        print("Exception when calling PostalServicesApi->delete_postal_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **postal_services_delete_postal_service_request** | [**PostalServicesDeletePostalServiceRequest**](PostalServicesDeletePostalServiceRequest.md)|  | 

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

# **get_channel_links**
> List[ChannelServiceLinks] get_channel_links(postal_service_id=postal_service_id)

GetChannelLinks

Returns Channel Service Link Information <b>Permissions Required: </b> GlobalPermissions.ShippingService.PostalServicesNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.postalservices
from linnworks_api.generated.postalservices.models.channel_service_links import ChannelServiceLinks
from linnworks_api.generated.postalservices.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.postalservices.Configuration(
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
with linnworks_api.generated.postalservices.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.postalservices.PostalServicesApi(api_client)
    postal_service_id = 'postal_service_id_example' # str | Postal service ID (optional)

    try:
        # GetChannelLinks
        api_response = api_instance.get_channel_links(postal_service_id=postal_service_id)
        print("The response of PostalServicesApi->get_channel_links:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostalServicesApi->get_channel_links: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **postal_service_id** | **str**| Postal service ID | [optional] 

### Return type

[**List[ChannelServiceLinks]**](ChannelServiceLinks.md)

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

# **get_postal_services**
> List[PostalServiceWithChannelAndShippingLinks] get_postal_services()

GetPostalServices

Gets a list of the users postal services and information on channels and couriers linked to each service <b>Permissions Required: </b> GlobalPermissions.ShippingService.PostalServicesNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.postalservices
from linnworks_api.generated.postalservices.models.postal_service_with_channel_and_shipping_links import PostalServiceWithChannelAndShippingLinks
from linnworks_api.generated.postalservices.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.postalservices.Configuration(
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
with linnworks_api.generated.postalservices.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.postalservices.PostalServicesApi(api_client)

    try:
        # GetPostalServices
        api_response = api_instance.get_postal_services()
        print("The response of PostalServicesApi->get_postal_services:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostalServicesApi->get_postal_services: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[PostalServiceWithChannelAndShippingLinks]**](PostalServiceWithChannelAndShippingLinks.md)

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

# **update_postal_service**
> update_postal_service(postal_services_update_postal_service_request)

UpdatePostalService

Changes an existing postal service in the database <b>Permissions Required: </b> GlobalPermissions.ShippingService.PostalServicesNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.postalservices
from linnworks_api.generated.postalservices.models.postal_services_update_postal_service_request import PostalServicesUpdatePostalServiceRequest
from linnworks_api.generated.postalservices.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.postalservices.Configuration(
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
with linnworks_api.generated.postalservices.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.postalservices.PostalServicesApi(api_client)
    postal_services_update_postal_service_request = linnworks_api.generated.postalservices.PostalServicesUpdatePostalServiceRequest() # PostalServicesUpdatePostalServiceRequest | 

    try:
        # UpdatePostalService
        api_instance.update_postal_service(postal_services_update_postal_service_request)
    except Exception as e:
        print("Exception when calling PostalServicesApi->update_postal_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **postal_services_update_postal_service_request** | [**PostalServicesUpdatePostalServiceRequest**](PostalServicesUpdatePostalServiceRequest.md)|  | 

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

