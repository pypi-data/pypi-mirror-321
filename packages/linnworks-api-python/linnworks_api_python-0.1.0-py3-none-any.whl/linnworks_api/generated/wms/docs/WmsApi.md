# linnworks_api.generated.wms.WmsApi

All URIs are relative to *https://eu-ext.linnworks.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_warehouse_zone**](WmsApi.md#add_warehouse_zone) | **POST** /api/Wms/AddWarehouseZone | AddWarehouseZone
[**add_warehouse_zone_type**](WmsApi.md#add_warehouse_zone_type) | **POST** /api/Wms/AddWarehouseZoneType | AddWarehouseZoneType
[**delete_warehouse_zone**](WmsApi.md#delete_warehouse_zone) | **POST** /api/Wms/DeleteWarehouseZone | DeleteWarehouseZone
[**delete_warehouse_zone_type**](WmsApi.md#delete_warehouse_zone_type) | **POST** /api/Wms/DeleteWarehouseZoneType | DeleteWarehouseZoneType
[**get_binrack_zones_by_binrack_id_or_name**](WmsApi.md#get_binrack_zones_by_binrack_id_or_name) | **POST** /api/Wms/GetBinrackZonesByBinrackIdOrName | GetBinrackZonesByBinrackIdOrName
[**get_binrack_zones_by_zone_id_or_name**](WmsApi.md#get_binrack_zones_by_zone_id_or_name) | **POST** /api/Wms/GetBinrackZonesByZoneIdOrName | GetBinrackZonesByZoneIdOrName
[**get_warehouse_zone_types**](WmsApi.md#get_warehouse_zone_types) | **GET** /api/Wms/GetWarehouseZoneTypes | GetWarehouseZoneTypes
[**get_warehouse_zones_by_location**](WmsApi.md#get_warehouse_zones_by_location) | **GET** /api/Wms/GetWarehouseZonesByLocation | GetWarehouseZonesByLocation
[**update_warehouse_binrack_binrack_to_zone**](WmsApi.md#update_warehouse_binrack_binrack_to_zone) | **POST** /api/Wms/UpdateWarehouseBinrackBinrackToZone | UpdateWarehouseBinrackBinrackToZone
[**update_warehouse_zone**](WmsApi.md#update_warehouse_zone) | **POST** /api/Wms/UpdateWarehouseZone | UpdateWarehouseZone
[**update_warehouse_zone_type**](WmsApi.md#update_warehouse_zone_type) | **POST** /api/Wms/UpdateWarehouseZoneType | UpdateWarehouseZoneType


# **add_warehouse_zone**
> AddWarehouseZoneResponse add_warehouse_zone(request=request)

AddWarehouseZone

 <b>Permissions Required: </b> GlobalPermissions.Inventory.WarehouseManagement.AdministrationNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.wms
from linnworks_api.generated.wms.models.add_warehouse_zone_request import AddWarehouseZoneRequest
from linnworks_api.generated.wms.models.add_warehouse_zone_response import AddWarehouseZoneResponse
from linnworks_api.generated.wms.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.wms.Configuration(
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
with linnworks_api.generated.wms.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.wms.WmsApi(api_client)
    request = linnworks_api.generated.wms.AddWarehouseZoneRequest() # AddWarehouseZoneRequest |  (optional)

    try:
        # AddWarehouseZone
        api_response = api_instance.add_warehouse_zone(request=request)
        print("The response of WmsApi->add_warehouse_zone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WmsApi->add_warehouse_zone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**AddWarehouseZoneRequest**](AddWarehouseZoneRequest.md)|  | [optional] 

### Return type

[**AddWarehouseZoneResponse**](AddWarehouseZoneResponse.md)

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

# **add_warehouse_zone_type**
> AddWarehouseZoneTypeResponse add_warehouse_zone_type(request=request)

AddWarehouseZoneType

 <b>Permissions Required: </b> GlobalPermissions.Inventory.WarehouseManagement.AdministrationNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.wms
from linnworks_api.generated.wms.models.add_warehouse_zone_type_request import AddWarehouseZoneTypeRequest
from linnworks_api.generated.wms.models.add_warehouse_zone_type_response import AddWarehouseZoneTypeResponse
from linnworks_api.generated.wms.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.wms.Configuration(
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
with linnworks_api.generated.wms.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.wms.WmsApi(api_client)
    request = linnworks_api.generated.wms.AddWarehouseZoneTypeRequest() # AddWarehouseZoneTypeRequest |  (optional)

    try:
        # AddWarehouseZoneType
        api_response = api_instance.add_warehouse_zone_type(request=request)
        print("The response of WmsApi->add_warehouse_zone_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WmsApi->add_warehouse_zone_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**AddWarehouseZoneTypeRequest**](AddWarehouseZoneTypeRequest.md)|  | [optional] 

### Return type

[**AddWarehouseZoneTypeResponse**](AddWarehouseZoneTypeResponse.md)

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

# **delete_warehouse_zone**
> object delete_warehouse_zone(request=request)

DeleteWarehouseZone

 <b>Permissions Required: </b> GlobalPermissions.Inventory.WarehouseManagement.AdministrationNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.wms
from linnworks_api.generated.wms.models.delete_warehouse_zone_request import DeleteWarehouseZoneRequest
from linnworks_api.generated.wms.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.wms.Configuration(
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
with linnworks_api.generated.wms.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.wms.WmsApi(api_client)
    request = linnworks_api.generated.wms.DeleteWarehouseZoneRequest() # DeleteWarehouseZoneRequest |  (optional)

    try:
        # DeleteWarehouseZone
        api_response = api_instance.delete_warehouse_zone(request=request)
        print("The response of WmsApi->delete_warehouse_zone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WmsApi->delete_warehouse_zone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**DeleteWarehouseZoneRequest**](DeleteWarehouseZoneRequest.md)|  | [optional] 

### Return type

**object**

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

# **delete_warehouse_zone_type**
> object delete_warehouse_zone_type(request=request)

DeleteWarehouseZoneType

 <b>Permissions Required: </b> GlobalPermissions.Inventory.WarehouseManagement.AdministrationNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.wms
from linnworks_api.generated.wms.models.delete_warehouse_zone_type_request import DeleteWarehouseZoneTypeRequest
from linnworks_api.generated.wms.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.wms.Configuration(
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
with linnworks_api.generated.wms.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.wms.WmsApi(api_client)
    request = linnworks_api.generated.wms.DeleteWarehouseZoneTypeRequest() # DeleteWarehouseZoneTypeRequest |  (optional)

    try:
        # DeleteWarehouseZoneType
        api_response = api_instance.delete_warehouse_zone_type(request=request)
        print("The response of WmsApi->delete_warehouse_zone_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WmsApi->delete_warehouse_zone_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**DeleteWarehouseZoneTypeRequest**](DeleteWarehouseZoneTypeRequest.md)|  | [optional] 

### Return type

**object**

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

# **get_binrack_zones_by_binrack_id_or_name**
> GetBinrackZonesByBinrackIdOrNameResponse get_binrack_zones_by_binrack_id_or_name(request=request)

GetBinrackZonesByBinrackIdOrName

 <b>Permissions Required: </b> GlobalPermissions.Inventory.WarehouseManagementNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.wms
from linnworks_api.generated.wms.models.get_binrack_zones_by_binrack_id_or_name_request import GetBinrackZonesByBinrackIdOrNameRequest
from linnworks_api.generated.wms.models.get_binrack_zones_by_binrack_id_or_name_response import GetBinrackZonesByBinrackIdOrNameResponse
from linnworks_api.generated.wms.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.wms.Configuration(
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
with linnworks_api.generated.wms.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.wms.WmsApi(api_client)
    request = linnworks_api.generated.wms.GetBinrackZonesByBinrackIdOrNameRequest() # GetBinrackZonesByBinrackIdOrNameRequest |  (optional)

    try:
        # GetBinrackZonesByBinrackIdOrName
        api_response = api_instance.get_binrack_zones_by_binrack_id_or_name(request=request)
        print("The response of WmsApi->get_binrack_zones_by_binrack_id_or_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WmsApi->get_binrack_zones_by_binrack_id_or_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**GetBinrackZonesByBinrackIdOrNameRequest**](GetBinrackZonesByBinrackIdOrNameRequest.md)|  | [optional] 

### Return type

[**GetBinrackZonesByBinrackIdOrNameResponse**](GetBinrackZonesByBinrackIdOrNameResponse.md)

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

# **get_binrack_zones_by_zone_id_or_name**
> GetBinrackZonesByZoneIdOrNameResponse get_binrack_zones_by_zone_id_or_name(request=request)

GetBinrackZonesByZoneIdOrName

 <b>Permissions Required: </b> GlobalPermissions.Inventory.WarehouseManagementNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.wms
from linnworks_api.generated.wms.models.get_binrack_zones_by_zone_id_or_name_request import GetBinrackZonesByZoneIdOrNameRequest
from linnworks_api.generated.wms.models.get_binrack_zones_by_zone_id_or_name_response import GetBinrackZonesByZoneIdOrNameResponse
from linnworks_api.generated.wms.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.wms.Configuration(
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
with linnworks_api.generated.wms.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.wms.WmsApi(api_client)
    request = linnworks_api.generated.wms.GetBinrackZonesByZoneIdOrNameRequest() # GetBinrackZonesByZoneIdOrNameRequest |  (optional)

    try:
        # GetBinrackZonesByZoneIdOrName
        api_response = api_instance.get_binrack_zones_by_zone_id_or_name(request=request)
        print("The response of WmsApi->get_binrack_zones_by_zone_id_or_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WmsApi->get_binrack_zones_by_zone_id_or_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**GetBinrackZonesByZoneIdOrNameRequest**](GetBinrackZonesByZoneIdOrNameRequest.md)|  | [optional] 

### Return type

[**GetBinrackZonesByZoneIdOrNameResponse**](GetBinrackZonesByZoneIdOrNameResponse.md)

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

# **get_warehouse_zone_types**
> GetWarehouseZoneTypesResponse get_warehouse_zone_types()

GetWarehouseZoneTypes

 <b>Permissions Required: </b> GlobalPermissions.Inventory.WarehouseManagementNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.wms
from linnworks_api.generated.wms.models.get_warehouse_zone_types_response import GetWarehouseZoneTypesResponse
from linnworks_api.generated.wms.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.wms.Configuration(
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
with linnworks_api.generated.wms.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.wms.WmsApi(api_client)

    try:
        # GetWarehouseZoneTypes
        api_response = api_instance.get_warehouse_zone_types()
        print("The response of WmsApi->get_warehouse_zone_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WmsApi->get_warehouse_zone_types: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetWarehouseZoneTypesResponse**](GetWarehouseZoneTypesResponse.md)

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

# **get_warehouse_zones_by_location**
> GetWarehouseZonesByLocationResponse get_warehouse_zones_by_location(stock_location_int_id=stock_location_int_id, only_binrack_assignable=only_binrack_assignable)

GetWarehouseZonesByLocation

 <b>Permissions Required: </b> GlobalPermissions.Inventory.WarehouseManagementNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.wms
from linnworks_api.generated.wms.models.get_warehouse_zones_by_location_response import GetWarehouseZonesByLocationResponse
from linnworks_api.generated.wms.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.wms.Configuration(
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
with linnworks_api.generated.wms.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.wms.WmsApi(api_client)
    stock_location_int_id = 56 # int |  (optional)
    only_binrack_assignable = True # bool |  (optional)

    try:
        # GetWarehouseZonesByLocation
        api_response = api_instance.get_warehouse_zones_by_location(stock_location_int_id=stock_location_int_id, only_binrack_assignable=only_binrack_assignable)
        print("The response of WmsApi->get_warehouse_zones_by_location:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WmsApi->get_warehouse_zones_by_location: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_location_int_id** | **int**|  | [optional] 
 **only_binrack_assignable** | **bool**|  | [optional] 

### Return type

[**GetWarehouseZonesByLocationResponse**](GetWarehouseZonesByLocationResponse.md)

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

# **update_warehouse_binrack_binrack_to_zone**
> UpdateWarehouseBinrackBinrackToZoneResponse update_warehouse_binrack_binrack_to_zone(request=request)

UpdateWarehouseBinrackBinrackToZone

 <b>Permissions Required: </b> GlobalPermissions.Inventory.WarehouseManagementNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.wms
from linnworks_api.generated.wms.models.update_warehouse_binrack_binrack_to_zone_request import UpdateWarehouseBinrackBinrackToZoneRequest
from linnworks_api.generated.wms.models.update_warehouse_binrack_binrack_to_zone_response import UpdateWarehouseBinrackBinrackToZoneResponse
from linnworks_api.generated.wms.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.wms.Configuration(
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
with linnworks_api.generated.wms.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.wms.WmsApi(api_client)
    request = linnworks_api.generated.wms.UpdateWarehouseBinrackBinrackToZoneRequest() # UpdateWarehouseBinrackBinrackToZoneRequest |  (optional)

    try:
        # UpdateWarehouseBinrackBinrackToZone
        api_response = api_instance.update_warehouse_binrack_binrack_to_zone(request=request)
        print("The response of WmsApi->update_warehouse_binrack_binrack_to_zone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WmsApi->update_warehouse_binrack_binrack_to_zone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**UpdateWarehouseBinrackBinrackToZoneRequest**](UpdateWarehouseBinrackBinrackToZoneRequest.md)|  | [optional] 

### Return type

[**UpdateWarehouseBinrackBinrackToZoneResponse**](UpdateWarehouseBinrackBinrackToZoneResponse.md)

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

# **update_warehouse_zone**
> UpdateWarehouseZoneResponse update_warehouse_zone(request=request)

UpdateWarehouseZone

 <b>Permissions Required: </b> GlobalPermissions.Inventory.WarehouseManagement.AdministrationNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.wms
from linnworks_api.generated.wms.models.update_warehouse_zone_request import UpdateWarehouseZoneRequest
from linnworks_api.generated.wms.models.update_warehouse_zone_response import UpdateWarehouseZoneResponse
from linnworks_api.generated.wms.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.wms.Configuration(
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
with linnworks_api.generated.wms.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.wms.WmsApi(api_client)
    request = linnworks_api.generated.wms.UpdateWarehouseZoneRequest() # UpdateWarehouseZoneRequest |  (optional)

    try:
        # UpdateWarehouseZone
        api_response = api_instance.update_warehouse_zone(request=request)
        print("The response of WmsApi->update_warehouse_zone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WmsApi->update_warehouse_zone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**UpdateWarehouseZoneRequest**](UpdateWarehouseZoneRequest.md)|  | [optional] 

### Return type

[**UpdateWarehouseZoneResponse**](UpdateWarehouseZoneResponse.md)

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

# **update_warehouse_zone_type**
> UpdateWarehouseZoneTypeResponse update_warehouse_zone_type(request=request)

UpdateWarehouseZoneType

 <b>Permissions Required: </b> GlobalPermissions.Inventory.WarehouseManagement.AdministrationNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.wms
from linnworks_api.generated.wms.models.update_warehouse_zone_type_request import UpdateWarehouseZoneTypeRequest
from linnworks_api.generated.wms.models.update_warehouse_zone_type_response import UpdateWarehouseZoneTypeResponse
from linnworks_api.generated.wms.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.wms.Configuration(
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
with linnworks_api.generated.wms.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.wms.WmsApi(api_client)
    request = linnworks_api.generated.wms.UpdateWarehouseZoneTypeRequest() # UpdateWarehouseZoneTypeRequest |  (optional)

    try:
        # UpdateWarehouseZoneType
        api_response = api_instance.update_warehouse_zone_type(request=request)
        print("The response of WmsApi->update_warehouse_zone_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WmsApi->update_warehouse_zone_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**UpdateWarehouseZoneTypeRequest**](UpdateWarehouseZoneTypeRequest.md)|  | [optional] 

### Return type

[**UpdateWarehouseZoneTypeResponse**](UpdateWarehouseZoneTypeResponse.md)

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

