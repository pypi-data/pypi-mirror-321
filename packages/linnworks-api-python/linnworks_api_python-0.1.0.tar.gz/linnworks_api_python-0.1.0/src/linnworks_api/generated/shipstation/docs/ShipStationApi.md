# linnworks_api.generated.shipstation.ShipStationApi

All URIs are relative to *https://eu-ext.linnworks.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ship_station_integration**](ShipStationApi.md#create_ship_station_integration) | **POST** /api/ShipStation/CreateShipStationIntegration | CreateShipStationIntegration
[**delete_ship_station_integration**](ShipStationApi.md#delete_ship_station_integration) | **POST** /api/ShipStation/DeleteShipStationIntegration | DeleteShipStationIntegration
[**edit_ship_station_integration**](ShipStationApi.md#edit_ship_station_integration) | **POST** /api/ShipStation/EditShipStationIntegration | EditShipStationIntegration
[**get_ship_station_integration**](ShipStationApi.md#get_ship_station_integration) | **GET** /api/ShipStation/GetShipStationIntegration | GetShipStationIntegration
[**get_ship_station_integrations**](ShipStationApi.md#get_ship_station_integrations) | **GET** /api/ShipStation/GetShipStationIntegrations | GetShipStationIntegrations


# **create_ship_station_integration**
> ShipStationConfig create_ship_station_integration(ship_station_create_ship_station_integration_request)

CreateShipStationIntegration

Used for ShipStation to create a new ShipStation integration <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.shipstation
from linnworks_api.generated.shipstation.models.ship_station_config import ShipStationConfig
from linnworks_api.generated.shipstation.models.ship_station_create_ship_station_integration_request import ShipStationCreateShipStationIntegrationRequest
from linnworks_api.generated.shipstation.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.shipstation.Configuration(
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
with linnworks_api.generated.shipstation.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.shipstation.ShipStationApi(api_client)
    ship_station_create_ship_station_integration_request = linnworks_api.generated.shipstation.ShipStationCreateShipStationIntegrationRequest() # ShipStationCreateShipStationIntegrationRequest | 

    try:
        # CreateShipStationIntegration
        api_response = api_instance.create_ship_station_integration(ship_station_create_ship_station_integration_request)
        print("The response of ShipStationApi->create_ship_station_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipStationApi->create_ship_station_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ship_station_create_ship_station_integration_request** | [**ShipStationCreateShipStationIntegrationRequest**](ShipStationCreateShipStationIntegrationRequest.md)|  | 

### Return type

[**ShipStationConfig**](ShipStationConfig.md)

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

# **delete_ship_station_integration**
> delete_ship_station_integration(ship_station_delete_ship_station_integration_request)

DeleteShipStationIntegration

Used for ShipStation to delete a ShipStation integration by its id <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.shipstation
from linnworks_api.generated.shipstation.models.ship_station_delete_ship_station_integration_request import ShipStationDeleteShipStationIntegrationRequest
from linnworks_api.generated.shipstation.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.shipstation.Configuration(
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
with linnworks_api.generated.shipstation.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.shipstation.ShipStationApi(api_client)
    ship_station_delete_ship_station_integration_request = linnworks_api.generated.shipstation.ShipStationDeleteShipStationIntegrationRequest() # ShipStationDeleteShipStationIntegrationRequest | 

    try:
        # DeleteShipStationIntegration
        api_instance.delete_ship_station_integration(ship_station_delete_ship_station_integration_request)
    except Exception as e:
        print("Exception when calling ShipStationApi->delete_ship_station_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ship_station_delete_ship_station_integration_request** | [**ShipStationDeleteShipStationIntegrationRequest**](ShipStationDeleteShipStationIntegrationRequest.md)|  | 

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

# **edit_ship_station_integration**
> bool edit_ship_station_integration(ship_station_edit_ship_station_integration_request)

EditShipStationIntegration

Used for ShipStation to update a ShipStation integration <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.shipstation
from linnworks_api.generated.shipstation.models.ship_station_edit_ship_station_integration_request import ShipStationEditShipStationIntegrationRequest
from linnworks_api.generated.shipstation.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.shipstation.Configuration(
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
with linnworks_api.generated.shipstation.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.shipstation.ShipStationApi(api_client)
    ship_station_edit_ship_station_integration_request = linnworks_api.generated.shipstation.ShipStationEditShipStationIntegrationRequest() # ShipStationEditShipStationIntegrationRequest | 

    try:
        # EditShipStationIntegration
        api_response = api_instance.edit_ship_station_integration(ship_station_edit_ship_station_integration_request)
        print("The response of ShipStationApi->edit_ship_station_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipStationApi->edit_ship_station_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ship_station_edit_ship_station_integration_request** | [**ShipStationEditShipStationIntegrationRequest**](ShipStationEditShipStationIntegrationRequest.md)|  | 

### Return type

**bool**

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

# **get_ship_station_integration**
> ShipStationConfig get_ship_station_integration(integration_id=integration_id)

GetShipStationIntegration

Used for ShipStation to get single ShipStation integration by its id <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>250</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.shipstation
from linnworks_api.generated.shipstation.models.ship_station_config import ShipStationConfig
from linnworks_api.generated.shipstation.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.shipstation.Configuration(
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
with linnworks_api.generated.shipstation.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.shipstation.ShipStationApi(api_client)
    integration_id = 'integration_id_example' # str | Id of the integration to retrieve (optional)

    try:
        # GetShipStationIntegration
        api_response = api_instance.get_ship_station_integration(integration_id=integration_id)
        print("The response of ShipStationApi->get_ship_station_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipStationApi->get_ship_station_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **str**| Id of the integration to retrieve | [optional] 

### Return type

[**ShipStationConfig**](ShipStationConfig.md)

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

# **get_ship_station_integrations**
> List[ShipStationConfig] get_ship_station_integrations()

GetShipStationIntegrations

Used for ShipStation to get all ShipStation integrations <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.shipstation
from linnworks_api.generated.shipstation.models.ship_station_config import ShipStationConfig
from linnworks_api.generated.shipstation.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.shipstation.Configuration(
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
with linnworks_api.generated.shipstation.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.shipstation.ShipStationApi(api_client)

    try:
        # GetShipStationIntegrations
        api_response = api_instance.get_ship_station_integrations()
        print("The response of ShipStationApi->get_ship_station_integrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipStationApi->get_ship_station_integrations: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ShipStationConfig]**](ShipStationConfig.md)

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

