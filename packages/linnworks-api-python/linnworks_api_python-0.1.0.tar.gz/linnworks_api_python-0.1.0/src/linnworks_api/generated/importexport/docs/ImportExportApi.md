# linnworks_api.generated.importexport.ImportExportApi

All URIs are relative to *https://eu-ext.linnworks.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_export**](ImportExportApi.md#delete_export) | **POST** /api/ImportExport/DeleteExport | DeleteExport
[**delete_import**](ImportExportApi.md#delete_import) | **POST** /api/ImportExport/DeleteImport | DeleteImport
[**enable_export**](ImportExportApi.md#enable_export) | **POST** /api/ImportExport/EnableExport | EnableExport
[**enable_import**](ImportExportApi.md#enable_import) | **POST** /api/ImportExport/EnableImport | EnableImport
[**get_export**](ImportExportApi.md#get_export) | **GET** /api/ImportExport/GetExport | GetExport
[**get_export_list**](ImportExportApi.md#get_export_list) | **GET** /api/ImportExport/GetExportList | GetExportList
[**get_fullfilment_center_settings**](ImportExportApi.md#get_fullfilment_center_settings) | **GET** /api/ImportExport/GetFullfilmentCenterSettings | GetFullfilmentCenterSettings
[**get_import**](ImportExportApi.md#get_import) | **GET** /api/ImportExport/GetImport | GetImport
[**get_import_list**](ImportExportApi.md#get_import_list) | **GET** /api/ImportExport/GetImportList | GetImportList
[**run_now_export**](ImportExportApi.md#run_now_export) | **POST** /api/ImportExport/RunNowExport | RunNowExport
[**run_now_import**](ImportExportApi.md#run_now_import) | **POST** /api/ImportExport/RunNowImport | RunNowImport


# **delete_export**
> delete_export(import_export_delete_export_request)

DeleteExport

Delete an export configuration <b>Permissions Required: </b> GlobalPermissions.Settings.ImportExport.ExportNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.importexport
from linnworks_api.generated.importexport.models.import_export_delete_export_request import ImportExportDeleteExportRequest
from linnworks_api.generated.importexport.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.importexport.Configuration(
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
with linnworks_api.generated.importexport.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.importexport.ImportExportApi(api_client)
    import_export_delete_export_request = linnworks_api.generated.importexport.ImportExportDeleteExportRequest() # ImportExportDeleteExportRequest | 

    try:
        # DeleteExport
        api_instance.delete_export(import_export_delete_export_request)
    except Exception as e:
        print("Exception when calling ImportExportApi->delete_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_export_delete_export_request** | [**ImportExportDeleteExportRequest**](ImportExportDeleteExportRequest.md)|  | 

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

# **delete_import**
> delete_import(import_export_delete_import_request)

DeleteImport

Delete an import configuration <b>Permissions Required: </b> GlobalPermissions.Settings.ImportExport.ImportNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.importexport
from linnworks_api.generated.importexport.models.import_export_delete_import_request import ImportExportDeleteImportRequest
from linnworks_api.generated.importexport.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.importexport.Configuration(
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
with linnworks_api.generated.importexport.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.importexport.ImportExportApi(api_client)
    import_export_delete_import_request = linnworks_api.generated.importexport.ImportExportDeleteImportRequest() # ImportExportDeleteImportRequest | 

    try:
        # DeleteImport
        api_instance.delete_import(import_export_delete_import_request)
    except Exception as e:
        print("Exception when calling ImportExportApi->delete_import: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_export_delete_import_request** | [**ImportExportDeleteImportRequest**](ImportExportDeleteImportRequest.md)|  | 

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

# **enable_export**
> ExportRegister enable_export(import_export_enable_export_request)

EnableExport

Enable/disable a specific export <b>Permissions Required: </b> GlobalPermissions.Settings.ImportExport.ExportNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.importexport
from linnworks_api.generated.importexport.models.export_register import ExportRegister
from linnworks_api.generated.importexport.models.import_export_enable_export_request import ImportExportEnableExportRequest
from linnworks_api.generated.importexport.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.importexport.Configuration(
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
with linnworks_api.generated.importexport.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.importexport.ImportExportApi(api_client)
    import_export_enable_export_request = linnworks_api.generated.importexport.ImportExportEnableExportRequest() # ImportExportEnableExportRequest | 

    try:
        # EnableExport
        api_response = api_instance.enable_export(import_export_enable_export_request)
        print("The response of ImportExportApi->enable_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportExportApi->enable_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_export_enable_export_request** | [**ImportExportEnableExportRequest**](ImportExportEnableExportRequest.md)|  | 

### Return type

[**ExportRegister**](ExportRegister.md)

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

# **enable_import**
> ImportRegister enable_import(import_export_enable_import_request)

EnableImport

Enable/disable a specific import <b>Permissions Required: </b> GlobalPermissions.Settings.ImportExport.ImportNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.importexport
from linnworks_api.generated.importexport.models.import_export_enable_import_request import ImportExportEnableImportRequest
from linnworks_api.generated.importexport.models.import_register import ImportRegister
from linnworks_api.generated.importexport.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.importexport.Configuration(
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
with linnworks_api.generated.importexport.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.importexport.ImportExportApi(api_client)
    import_export_enable_import_request = linnworks_api.generated.importexport.ImportExportEnableImportRequest() # ImportExportEnableImportRequest | 

    try:
        # EnableImport
        api_response = api_instance.enable_import(import_export_enable_import_request)
        print("The response of ImportExportApi->enable_import:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportExportApi->enable_import: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_export_enable_import_request** | [**ImportExportEnableImportRequest**](ImportExportEnableImportRequest.md)|  | 

### Return type

[**ImportRegister**](ImportRegister.md)

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

# **get_export**
> Export get_export(id=id)

GetExport

Get an export configuration <b>Permissions Required: </b> GlobalPermissions.Settings.ImportExport.ExportNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.importexport
from linnworks_api.generated.importexport.models.export import Export
from linnworks_api.generated.importexport.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.importexport.Configuration(
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
with linnworks_api.generated.importexport.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.importexport.ImportExportApi(api_client)
    id = 56 # int | Id of the export to get (optional)

    try:
        # GetExport
        api_response = api_instance.get_export(id=id)
        print("The response of ImportExportApi->get_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportExportApi->get_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of the export to get | [optional] 

### Return type

[**Export**](Export.md)

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

# **get_export_list**
> GetExportListResponse get_export_list()

GetExportList

Get all existing exports <b>Permissions Required: </b> GlobalPermissions.Settings.ImportExport.ExportNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.importexport
from linnworks_api.generated.importexport.models.get_export_list_response import GetExportListResponse
from linnworks_api.generated.importexport.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.importexport.Configuration(
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
with linnworks_api.generated.importexport.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.importexport.ImportExportApi(api_client)

    try:
        # GetExportList
        api_response = api_instance.get_export_list()
        print("The response of ImportExportApi->get_export_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportExportApi->get_export_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetExportListResponse**](GetExportListResponse.md)

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

# **get_fullfilment_center_settings**
> FulfilmentCenterImportExportSettings get_fullfilment_center_settings(fk_stock_location_id=fk_stock_location_id)

GetFullfilmentCenterSettings

Gets fulfillment center settings <b>Permissions Required: </b> GlobalPermissions.Settings.ImportExportNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.importexport
from linnworks_api.generated.importexport.models.fulfilment_center_import_export_settings import FulfilmentCenterImportExportSettings
from linnworks_api.generated.importexport.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.importexport.Configuration(
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
with linnworks_api.generated.importexport.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.importexport.ImportExportApi(api_client)
    fk_stock_location_id = 'fk_stock_location_id_example' # str | Stock location id (optional)

    try:
        # GetFullfilmentCenterSettings
        api_response = api_instance.get_fullfilment_center_settings(fk_stock_location_id=fk_stock_location_id)
        print("The response of ImportExportApi->get_fullfilment_center_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportExportApi->get_fullfilment_center_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fk_stock_location_id** | **str**| Stock location id | [optional] 

### Return type

[**FulfilmentCenterImportExportSettings**](FulfilmentCenterImportExportSettings.md)

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

# **get_import**
> ModelImport get_import(id=id)

GetImport

Get an import configuration <b>Permissions Required: </b> GlobalPermissions.Settings.ImportExport.ImportNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.importexport
from linnworks_api.generated.importexport.models.model_import import ModelImport
from linnworks_api.generated.importexport.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.importexport.Configuration(
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
with linnworks_api.generated.importexport.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.importexport.ImportExportApi(api_client)
    id = 56 # int | Id of the import to get (optional)

    try:
        # GetImport
        api_response = api_instance.get_import(id=id)
        print("The response of ImportExportApi->get_import:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportExportApi->get_import: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of the import to get | [optional] 

### Return type

[**ModelImport**](ModelImport.md)

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

# **get_import_list**
> GetImportListResponse get_import_list()

GetImportList

Get all existing imports <b>Permissions Required: </b> GlobalPermissions.Settings.ImportExport.ImportNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.importexport
from linnworks_api.generated.importexport.models.get_import_list_response import GetImportListResponse
from linnworks_api.generated.importexport.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.importexport.Configuration(
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
with linnworks_api.generated.importexport.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.importexport.ImportExportApi(api_client)

    try:
        # GetImportList
        api_response = api_instance.get_import_list()
        print("The response of ImportExportApi->get_import_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportExportApi->get_import_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetImportListResponse**](GetImportListResponse.md)

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

# **run_now_export**
> run_now_export(import_export_run_now_export_request)

RunNowExport

Put the specific export immediately in the queue <b>Permissions Required: </b> GlobalPermissions.Settings.ImportExport.ExportNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.importexport
from linnworks_api.generated.importexport.models.import_export_run_now_export_request import ImportExportRunNowExportRequest
from linnworks_api.generated.importexport.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.importexport.Configuration(
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
with linnworks_api.generated.importexport.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.importexport.ImportExportApi(api_client)
    import_export_run_now_export_request = linnworks_api.generated.importexport.ImportExportRunNowExportRequest() # ImportExportRunNowExportRequest | 

    try:
        # RunNowExport
        api_instance.run_now_export(import_export_run_now_export_request)
    except Exception as e:
        print("Exception when calling ImportExportApi->run_now_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_export_run_now_export_request** | [**ImportExportRunNowExportRequest**](ImportExportRunNowExportRequest.md)|  | 

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

# **run_now_import**
> run_now_import(import_export_run_now_import_request)

RunNowImport

Put the specific import immediately in the queue <b>Permissions Required: </b> GlobalPermissions.Settings.ImportExport.ImportNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.importexport
from linnworks_api.generated.importexport.models.import_export_run_now_import_request import ImportExportRunNowImportRequest
from linnworks_api.generated.importexport.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.importexport.Configuration(
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
with linnworks_api.generated.importexport.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.importexport.ImportExportApi(api_client)
    import_export_run_now_import_request = linnworks_api.generated.importexport.ImportExportRunNowImportRequest() # ImportExportRunNowImportRequest | 

    try:
        # RunNowImport
        api_instance.run_now_import(import_export_run_now_import_request)
    except Exception as e:
        print("Exception when calling ImportExportApi->run_now_import: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_export_run_now_import_request** | [**ImportExportRunNowImportRequest**](ImportExportRunNowImportRequest.md)|  | 

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

