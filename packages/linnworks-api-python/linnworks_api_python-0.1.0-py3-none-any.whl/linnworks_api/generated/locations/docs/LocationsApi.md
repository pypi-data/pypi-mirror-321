# linnworks_api.generated.locations.LocationsApi

All URIs are relative to *https://eu-ext.linnworks.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_location**](LocationsApi.md#add_location) | **POST** /api/Locations/AddLocation | AddLocation
[**delete_location**](LocationsApi.md#delete_location) | **POST** /api/Locations/DeleteLocation | DeleteLocation
[**delete_warehouse_tote**](LocationsApi.md#delete_warehouse_tote) | **POST** /api/Locations/DeleteWarehouseTOTE | DeleteWarehouseTOTE
[**get_location**](LocationsApi.md#get_location) | **GET** /api/Locations/GetLocation | GetLocation
[**get_warehouse_totes**](LocationsApi.md#get_warehouse_totes) | **POST** /api/Locations/GetWarehouseTOTEs | GetWarehouseTOTEs
[**update_location**](LocationsApi.md#update_location) | **POST** /api/Locations/UpdateLocation | UpdateLocation


# **add_location**
> add_location(locations_add_location_request)

AddLocation

Use this call to add a new location. <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.locations
from linnworks_api.generated.locations.models.locations_add_location_request import LocationsAddLocationRequest
from linnworks_api.generated.locations.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.locations.Configuration(
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
with linnworks_api.generated.locations.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.locations.LocationsApi(api_client)
    locations_add_location_request = linnworks_api.generated.locations.LocationsAddLocationRequest() # LocationsAddLocationRequest | 

    try:
        # AddLocation
        api_instance.add_location(locations_add_location_request)
    except Exception as e:
        print("Exception when calling LocationsApi->add_location: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locations_add_location_request** | [**LocationsAddLocationRequest**](LocationsAddLocationRequest.md)|  | 

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

# **delete_location**
> delete_location(locations_delete_location_request)

DeleteLocation

Use this call to delete a location by its id <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.locations
from linnworks_api.generated.locations.models.locations_delete_location_request import LocationsDeleteLocationRequest
from linnworks_api.generated.locations.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.locations.Configuration(
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
with linnworks_api.generated.locations.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.locations.LocationsApi(api_client)
    locations_delete_location_request = linnworks_api.generated.locations.LocationsDeleteLocationRequest() # LocationsDeleteLocationRequest | 

    try:
        # DeleteLocation
        api_instance.delete_location(locations_delete_location_request)
    except Exception as e:
        print("Exception when calling LocationsApi->delete_location: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locations_delete_location_request** | [**LocationsDeleteLocationRequest**](LocationsDeleteLocationRequest.md)|  | 

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

# **delete_warehouse_tote**
> DeleteWarehouseToteResponse delete_warehouse_tote(locations_delete_warehouse_tote_request)

DeleteWarehouseTOTE

Delete existing Tote from location <b>Permissions Required: </b> GlobalPermissions.Inventory.InventorySettings.LocationsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.locations
from linnworks_api.generated.locations.models.delete_warehouse_tote_response import DeleteWarehouseToteResponse
from linnworks_api.generated.locations.models.locations_delete_warehouse_tote_request import LocationsDeleteWarehouseTOTERequest
from linnworks_api.generated.locations.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.locations.Configuration(
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
with linnworks_api.generated.locations.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.locations.LocationsApi(api_client)
    locations_delete_warehouse_tote_request = linnworks_api.generated.locations.LocationsDeleteWarehouseTOTERequest() # LocationsDeleteWarehouseTOTERequest | 

    try:
        # DeleteWarehouseTOTE
        api_response = api_instance.delete_warehouse_tote(locations_delete_warehouse_tote_request)
        print("The response of LocationsApi->delete_warehouse_tote:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->delete_warehouse_tote: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locations_delete_warehouse_tote_request** | [**LocationsDeleteWarehouseTOTERequest**](LocationsDeleteWarehouseTOTERequest.md)|  | 

### Return type

[**DeleteWarehouseToteResponse**](DeleteWarehouseToteResponse.md)

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

# **get_location**
> StockLocation get_location(pk_stock_location_id=pk_stock_location_id)

GetLocation

Use this call to retrieve a location and basic information about it from your Linnworks account. <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.locations
from linnworks_api.generated.locations.models.stock_location import StockLocation
from linnworks_api.generated.locations.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.locations.Configuration(
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
with linnworks_api.generated.locations.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.locations.LocationsApi(api_client)
    pk_stock_location_id = 'pk_stock_location_id_example' # str | The pkStockLocationId which identifies the location (optional)

    try:
        # GetLocation
        api_response = api_instance.get_location(pk_stock_location_id=pk_stock_location_id)
        print("The response of LocationsApi->get_location:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->get_location: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pk_stock_location_id** | **str**| The pkStockLocationId which identifies the location | [optional] 

### Return type

[**StockLocation**](StockLocation.md)

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

# **get_warehouse_totes**
> GetWarehouseTotesResponse get_warehouse_totes(request=request)

GetWarehouseTOTEs

Gets list of tots for a specific location or find a specific tot depending on the request parameters. Specify tot id or tot barcode to find specific tot in the location or   if nothing is specified or parameters are omitted, all tots for the location will be returned <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.locations
from linnworks_api.generated.locations.models.get_warehouse_totes_request import GetWarehouseTotesRequest
from linnworks_api.generated.locations.models.get_warehouse_totes_response import GetWarehouseTotesResponse
from linnworks_api.generated.locations.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.locations.Configuration(
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
with linnworks_api.generated.locations.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.locations.LocationsApi(api_client)
    request = linnworks_api.generated.locations.GetWarehouseTotesRequest() # GetWarehouseTotesRequest |  (optional)

    try:
        # GetWarehouseTOTEs
        api_response = api_instance.get_warehouse_totes(request=request)
        print("The response of LocationsApi->get_warehouse_totes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->get_warehouse_totes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**GetWarehouseTotesRequest**](GetWarehouseTotesRequest.md)|  | [optional] 

### Return type

[**GetWarehouseTotesResponse**](GetWarehouseTotesResponse.md)

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

# **update_location**
> update_location(locations_update_location_request)

UpdateLocation

Use this call to update a location's name and/or details <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.locations
from linnworks_api.generated.locations.models.locations_update_location_request import LocationsUpdateLocationRequest
from linnworks_api.generated.locations.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.locations.Configuration(
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
with linnworks_api.generated.locations.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.locations.LocationsApi(api_client)
    locations_update_location_request = linnworks_api.generated.locations.LocationsUpdateLocationRequest() # LocationsUpdateLocationRequest | 

    try:
        # UpdateLocation
        api_instance.update_location(locations_update_location_request)
    except Exception as e:
        print("Exception when calling LocationsApi->update_location: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locations_update_location_request** | [**LocationsUpdateLocationRequest**](LocationsUpdateLocationRequest.md)|  | 

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

