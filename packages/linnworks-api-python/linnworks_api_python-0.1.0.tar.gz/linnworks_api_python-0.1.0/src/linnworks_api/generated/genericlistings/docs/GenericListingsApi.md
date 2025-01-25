# linnworks_api.generated.genericlistings.GenericListingsApi

All URIs are relative to *https://eu-ext.linnworks.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_configurator**](GenericListingsApi.md#create_configurator) | **POST** /api/GenericListings/CreateConfigurator | CreateConfigurator
[**create_templates**](GenericListingsApi.md#create_templates) | **POST** /api/GenericListings/CreateTemplates | CreateTemplates
[**delete_configurators**](GenericListingsApi.md#delete_configurators) | **POST** /api/GenericListings/DeleteConfigurators | DeleteConfigurators
[**get_configurator_data**](GenericListingsApi.md#get_configurator_data) | **POST** /api/GenericListings/GetConfiguratorData | GetConfiguratorData
[**get_configurator_description**](GenericListingsApi.md#get_configurator_description) | **POST** /api/GenericListings/GetConfiguratorDescription | GetConfiguratorDescription
[**get_configurators_info_paged**](GenericListingsApi.md#get_configurators_info_paged) | **POST** /api/GenericListings/GetConfiguratorsInfoPaged | GetConfiguratorsInfoPaged
[**open_templates_by_inventory**](GenericListingsApi.md#open_templates_by_inventory) | **POST** /api/GenericListings/OpenTemplatesByInventory | OpenTemplatesByInventory
[**process_templates**](GenericListingsApi.md#process_templates) | **POST** /api/GenericListings/ProcessTemplates | ProcessTemplates
[**save_configurator_data**](GenericListingsApi.md#save_configurator_data) | **POST** /api/GenericListings/SaveConfiguratorData | SaveConfiguratorData
[**save_configurator_description**](GenericListingsApi.md#save_configurator_description) | **POST** /api/GenericListings/SaveConfiguratorDescription | SaveConfiguratorDescription
[**save_configurator_fields**](GenericListingsApi.md#save_configurator_fields) | **POST** /api/GenericListings/SaveConfiguratorFields | SaveConfiguratorFields
[**save_template_fields**](GenericListingsApi.md#save_template_fields) | **POST** /api/GenericListings/SaveTemplateFields | SaveTemplateFields


# **create_configurator**
> CreateConfiguratorResponse create_configurator(generic_listings_create_configurator_request)

CreateConfigurator

Use this call to create a configurator. The configurator setup will be dependant on the channel that you want to create it for.    More information on configurators can be found in the [Linnworks general documentation](https://docs.linnworks.com/articles/#!documentation/configurators) <b>Permissions Required: </b> GlobalPermissions.Settings.ListingConfigurators.EditListingConfiguratorsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.genericlistings
from linnworks_api.generated.genericlistings.models.create_configurator_response import CreateConfiguratorResponse
from linnworks_api.generated.genericlistings.models.generic_listings_create_configurator_request import GenericListingsCreateConfiguratorRequest
from linnworks_api.generated.genericlistings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.genericlistings.Configuration(
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
with linnworks_api.generated.genericlistings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.genericlistings.GenericListingsApi(api_client)
    generic_listings_create_configurator_request = linnworks_api.generated.genericlistings.GenericListingsCreateConfiguratorRequest() # GenericListingsCreateConfiguratorRequest | 

    try:
        # CreateConfigurator
        api_response = api_instance.create_configurator(generic_listings_create_configurator_request)
        print("The response of GenericListingsApi->create_configurator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenericListingsApi->create_configurator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generic_listings_create_configurator_request** | [**GenericListingsCreateConfiguratorRequest**](GenericListingsCreateConfiguratorRequest.md)|  | 

### Return type

[**CreateConfiguratorResponse**](CreateConfiguratorResponse.md)

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

# **create_templates**
> CreateTemplatesResponse create_templates(generic_listings_create_templates_request)

CreateTemplates

Use this call to create a generic template based on the inventory item details and the configurator details. This template will contain the full details of the item that will be listed on the channel. <b>Permissions Required: </b> GlobalPermissions.Settings.ListingConfigurators.GetListingConfiguratorsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.genericlistings
from linnworks_api.generated.genericlistings.models.create_templates_response import CreateTemplatesResponse
from linnworks_api.generated.genericlistings.models.generic_listings_create_templates_request import GenericListingsCreateTemplatesRequest
from linnworks_api.generated.genericlistings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.genericlistings.Configuration(
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
with linnworks_api.generated.genericlistings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.genericlistings.GenericListingsApi(api_client)
    generic_listings_create_templates_request = linnworks_api.generated.genericlistings.GenericListingsCreateTemplatesRequest() # GenericListingsCreateTemplatesRequest | 

    try:
        # CreateTemplates
        api_response = api_instance.create_templates(generic_listings_create_templates_request)
        print("The response of GenericListingsApi->create_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenericListingsApi->create_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generic_listings_create_templates_request** | [**GenericListingsCreateTemplatesRequest**](GenericListingsCreateTemplatesRequest.md)|  | 

### Return type

[**CreateTemplatesResponse**](CreateTemplatesResponse.md)

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

# **delete_configurators**
> DeleteConfiguratorsResponse delete_configurators(generic_listings_delete_configurators_request)

DeleteConfigurators

Use this call to delete a configurator.    More information on configurators can be found in the [Linnworks general documentation](https://docs.linnworks.com/articles/#!documentation/configurators) <b>Permissions Required: </b> GlobalPermissions.Settings.ListingConfigurators.EditListingConfiguratorsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.genericlistings
from linnworks_api.generated.genericlistings.models.delete_configurators_response import DeleteConfiguratorsResponse
from linnworks_api.generated.genericlistings.models.generic_listings_delete_configurators_request import GenericListingsDeleteConfiguratorsRequest
from linnworks_api.generated.genericlistings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.genericlistings.Configuration(
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
with linnworks_api.generated.genericlistings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.genericlistings.GenericListingsApi(api_client)
    generic_listings_delete_configurators_request = linnworks_api.generated.genericlistings.GenericListingsDeleteConfiguratorsRequest() # GenericListingsDeleteConfiguratorsRequest | 

    try:
        # DeleteConfigurators
        api_response = api_instance.delete_configurators(generic_listings_delete_configurators_request)
        print("The response of GenericListingsApi->delete_configurators:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenericListingsApi->delete_configurators: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generic_listings_delete_configurators_request** | [**GenericListingsDeleteConfiguratorsRequest**](GenericListingsDeleteConfiguratorsRequest.md)|  | 

### Return type

[**DeleteConfiguratorsResponse**](DeleteConfiguratorsResponse.md)

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

# **get_configurator_data**
> GetConfiguratorDataResponse get_configurator_data(generic_listings_get_configurator_data_request)

GetConfiguratorData

Use this call to get the existing Generic Listing Tool configurators data.    More information on configurators can be found in the [Linnworks general documentation](https://docs.linnworks.com/articles/#!documentation/configurators) <b>Permissions Required: </b> GlobalPermissions.Settings.ListingConfigurators.GetListingConfiguratorsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.genericlistings
from linnworks_api.generated.genericlistings.models.generic_listings_get_configurator_data_request import GenericListingsGetConfiguratorDataRequest
from linnworks_api.generated.genericlistings.models.get_configurator_data_response import GetConfiguratorDataResponse
from linnworks_api.generated.genericlistings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.genericlistings.Configuration(
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
with linnworks_api.generated.genericlistings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.genericlistings.GenericListingsApi(api_client)
    generic_listings_get_configurator_data_request = linnworks_api.generated.genericlistings.GenericListingsGetConfiguratorDataRequest() # GenericListingsGetConfiguratorDataRequest | 

    try:
        # GetConfiguratorData
        api_response = api_instance.get_configurator_data(generic_listings_get_configurator_data_request)
        print("The response of GenericListingsApi->get_configurator_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenericListingsApi->get_configurator_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generic_listings_get_configurator_data_request** | [**GenericListingsGetConfiguratorDataRequest**](GenericListingsGetConfiguratorDataRequest.md)|  | 

### Return type

[**GetConfiguratorDataResponse**](GetConfiguratorDataResponse.md)

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

# **get_configurator_description**
> GetConfiguratorDescriptionResponse get_configurator_description(generic_listings_get_configurator_description_request)

GetConfiguratorDescription

Use this call to get the existing Generic Listing Tool configurators description.    More information on configurators can be found in the [Linnworks general documentation](https://docs.linnworks.com/articles/#!documentation/configurators) <b>Permissions Required: </b> GlobalPermissions.Settings.ListingConfigurators.GetListingConfiguratorsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.genericlistings
from linnworks_api.generated.genericlistings.models.generic_listings_get_configurator_description_request import GenericListingsGetConfiguratorDescriptionRequest
from linnworks_api.generated.genericlistings.models.get_configurator_description_response import GetConfiguratorDescriptionResponse
from linnworks_api.generated.genericlistings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.genericlistings.Configuration(
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
with linnworks_api.generated.genericlistings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.genericlistings.GenericListingsApi(api_client)
    generic_listings_get_configurator_description_request = linnworks_api.generated.genericlistings.GenericListingsGetConfiguratorDescriptionRequest() # GenericListingsGetConfiguratorDescriptionRequest | 

    try:
        # GetConfiguratorDescription
        api_response = api_instance.get_configurator_description(generic_listings_get_configurator_description_request)
        print("The response of GenericListingsApi->get_configurator_description:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenericListingsApi->get_configurator_description: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generic_listings_get_configurator_description_request** | [**GenericListingsGetConfiguratorDescriptionRequest**](GenericListingsGetConfiguratorDescriptionRequest.md)|  | 

### Return type

[**GetConfiguratorDescriptionResponse**](GetConfiguratorDescriptionResponse.md)

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

# **get_configurators_info_paged**
> GetConfiguratorsInfoResponse get_configurators_info_paged(generic_listings_get_configurators_info_paged_request)

GetConfiguratorsInfoPaged

Use this call to get the existing Generic Listing Tool configurators.    More information on configurators can be found in the [Linnworks general documentation](https://docs.linnworks.com/articles/#!documentation/configurators) <b>Permissions Required: </b> GlobalPermissions.Settings.ListingConfigurators.GetListingConfiguratorsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.genericlistings
from linnworks_api.generated.genericlistings.models.generic_listings_get_configurators_info_paged_request import GenericListingsGetConfiguratorsInfoPagedRequest
from linnworks_api.generated.genericlistings.models.get_configurators_info_response import GetConfiguratorsInfoResponse
from linnworks_api.generated.genericlistings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.genericlistings.Configuration(
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
with linnworks_api.generated.genericlistings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.genericlistings.GenericListingsApi(api_client)
    generic_listings_get_configurators_info_paged_request = linnworks_api.generated.genericlistings.GenericListingsGetConfiguratorsInfoPagedRequest() # GenericListingsGetConfiguratorsInfoPagedRequest | 

    try:
        # GetConfiguratorsInfoPaged
        api_response = api_instance.get_configurators_info_paged(generic_listings_get_configurators_info_paged_request)
        print("The response of GenericListingsApi->get_configurators_info_paged:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenericListingsApi->get_configurators_info_paged: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generic_listings_get_configurators_info_paged_request** | [**GenericListingsGetConfiguratorsInfoPagedRequest**](GenericListingsGetConfiguratorsInfoPagedRequest.md)|  | 

### Return type

[**GetConfiguratorsInfoResponse**](GetConfiguratorsInfoResponse.md)

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

# **open_templates_by_inventory**
> OpenTemplatesByInventoryResponse open_templates_by_inventory(generic_listings_open_templates_by_inventory_request)

OpenTemplatesByInventory

Use this call to get template details for Generic Listings using Stock Item IDs. <b>Permissions Required: </b> GlobalPermissions.Settings.ListingConfigurators.GetListingConfiguratorsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.genericlistings
from linnworks_api.generated.genericlistings.models.generic_listings_open_templates_by_inventory_request import GenericListingsOpenTemplatesByInventoryRequest
from linnworks_api.generated.genericlistings.models.open_templates_by_inventory_response import OpenTemplatesByInventoryResponse
from linnworks_api.generated.genericlistings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.genericlistings.Configuration(
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
with linnworks_api.generated.genericlistings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.genericlistings.GenericListingsApi(api_client)
    generic_listings_open_templates_by_inventory_request = linnworks_api.generated.genericlistings.GenericListingsOpenTemplatesByInventoryRequest() # GenericListingsOpenTemplatesByInventoryRequest | 

    try:
        # OpenTemplatesByInventory
        api_response = api_instance.open_templates_by_inventory(generic_listings_open_templates_by_inventory_request)
        print("The response of GenericListingsApi->open_templates_by_inventory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenericListingsApi->open_templates_by_inventory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generic_listings_open_templates_by_inventory_request** | [**GenericListingsOpenTemplatesByInventoryRequest**](GenericListingsOpenTemplatesByInventoryRequest.md)|  | 

### Return type

[**OpenTemplatesByInventoryResponse**](OpenTemplatesByInventoryResponse.md)

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

# **process_templates**
> object process_templates(generic_listings_process_templates_request)

ProcessTemplates

Use this call to push a template that you have created to a channel. This endpoint can also be used to update, relist, delete a template from a channel. <b>Permissions Required: </b> GlobalPermissions.Settings.ListingConfigurators.GetListingConfiguratorsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.genericlistings
from linnworks_api.generated.genericlistings.models.generic_listings_process_templates_request import GenericListingsProcessTemplatesRequest
from linnworks_api.generated.genericlistings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.genericlistings.Configuration(
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
with linnworks_api.generated.genericlistings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.genericlistings.GenericListingsApi(api_client)
    generic_listings_process_templates_request = linnworks_api.generated.genericlistings.GenericListingsProcessTemplatesRequest() # GenericListingsProcessTemplatesRequest | 

    try:
        # ProcessTemplates
        api_response = api_instance.process_templates(generic_listings_process_templates_request)
        print("The response of GenericListingsApi->process_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenericListingsApi->process_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generic_listings_process_templates_request** | [**GenericListingsProcessTemplatesRequest**](GenericListingsProcessTemplatesRequest.md)|  | 

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

# **save_configurator_data**
> SaveConfiguratorDataResponse save_configurator_data(generic_listings_save_configurator_data_request)

SaveConfiguratorData

Use this call to update a configurators data (attributes of the configurator).    More information on configurators can be found in the [Linnworks general documentation](https://docs.linnworks.com/articles/#!documentation/configurators) <b>Permissions Required: </b> GlobalPermissions.Settings.ListingConfigurators.EditListingConfiguratorsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.genericlistings
from linnworks_api.generated.genericlistings.models.generic_listings_save_configurator_data_request import GenericListingsSaveConfiguratorDataRequest
from linnworks_api.generated.genericlistings.models.save_configurator_data_response import SaveConfiguratorDataResponse
from linnworks_api.generated.genericlistings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.genericlistings.Configuration(
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
with linnworks_api.generated.genericlistings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.genericlistings.GenericListingsApi(api_client)
    generic_listings_save_configurator_data_request = linnworks_api.generated.genericlistings.GenericListingsSaveConfiguratorDataRequest() # GenericListingsSaveConfiguratorDataRequest | 

    try:
        # SaveConfiguratorData
        api_response = api_instance.save_configurator_data(generic_listings_save_configurator_data_request)
        print("The response of GenericListingsApi->save_configurator_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenericListingsApi->save_configurator_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generic_listings_save_configurator_data_request** | [**GenericListingsSaveConfiguratorDataRequest**](GenericListingsSaveConfiguratorDataRequest.md)|  | 

### Return type

[**SaveConfiguratorDataResponse**](SaveConfiguratorDataResponse.md)

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

# **save_configurator_description**
> SaveConfiguratorDescriptionResponse save_configurator_description(generic_listings_save_configurator_description_request)

SaveConfiguratorDescription

Use this call to update a configurators description.    More information on configurators can be found in the [Linnworks general documentation](https://docs.linnworks.com/articles/#!documentation/configurators) <b>Permissions Required: </b> GlobalPermissions.Settings.ListingConfigurators.GetListingConfiguratorsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.genericlistings
from linnworks_api.generated.genericlistings.models.generic_listings_save_configurator_description_request import GenericListingsSaveConfiguratorDescriptionRequest
from linnworks_api.generated.genericlistings.models.save_configurator_description_response import SaveConfiguratorDescriptionResponse
from linnworks_api.generated.genericlistings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.genericlistings.Configuration(
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
with linnworks_api.generated.genericlistings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.genericlistings.GenericListingsApi(api_client)
    generic_listings_save_configurator_description_request = linnworks_api.generated.genericlistings.GenericListingsSaveConfiguratorDescriptionRequest() # GenericListingsSaveConfiguratorDescriptionRequest | 

    try:
        # SaveConfiguratorDescription
        api_response = api_instance.save_configurator_description(generic_listings_save_configurator_description_request)
        print("The response of GenericListingsApi->save_configurator_description:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenericListingsApi->save_configurator_description: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generic_listings_save_configurator_description_request** | [**GenericListingsSaveConfiguratorDescriptionRequest**](GenericListingsSaveConfiguratorDescriptionRequest.md)|  | 

### Return type

[**SaveConfiguratorDescriptionResponse**](SaveConfiguratorDescriptionResponse.md)

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

# **save_configurator_fields**
> object save_configurator_fields(generic_listings_save_configurator_fields_request)

SaveConfiguratorFields

Use this call to update a configurators fields.    More information on configurators can be found in the [Linnworks general documentation](https://docs.linnworks.com/articles/#!documentation/configurators) <b>Permissions Required: </b> GlobalPermissions.Settings.ListingConfigurators.EditListingConfiguratorsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.genericlistings
from linnworks_api.generated.genericlistings.models.generic_listings_save_configurator_fields_request import GenericListingsSaveConfiguratorFieldsRequest
from linnworks_api.generated.genericlistings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.genericlistings.Configuration(
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
with linnworks_api.generated.genericlistings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.genericlistings.GenericListingsApi(api_client)
    generic_listings_save_configurator_fields_request = linnworks_api.generated.genericlistings.GenericListingsSaveConfiguratorFieldsRequest() # GenericListingsSaveConfiguratorFieldsRequest | 

    try:
        # SaveConfiguratorFields
        api_response = api_instance.save_configurator_fields(generic_listings_save_configurator_fields_request)
        print("The response of GenericListingsApi->save_configurator_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenericListingsApi->save_configurator_fields: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generic_listings_save_configurator_fields_request** | [**GenericListingsSaveConfiguratorFieldsRequest**](GenericListingsSaveConfiguratorFieldsRequest.md)|  | 

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

# **save_template_fields**
> object save_template_fields(generic_listings_save_template_fields_request)

SaveTemplateFields

Use this call to manipulate the fields on a template. This can be used to modify a generic template created using the CreateTemplate endpoint. <b>Permissions Required: </b> GlobalPermissions.Settings.ListingConfigurators.GetListingConfiguratorsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.genericlistings
from linnworks_api.generated.genericlistings.models.generic_listings_save_template_fields_request import GenericListingsSaveTemplateFieldsRequest
from linnworks_api.generated.genericlistings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.genericlistings.Configuration(
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
with linnworks_api.generated.genericlistings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.genericlistings.GenericListingsApi(api_client)
    generic_listings_save_template_fields_request = linnworks_api.generated.genericlistings.GenericListingsSaveTemplateFieldsRequest() # GenericListingsSaveTemplateFieldsRequest | 

    try:
        # SaveTemplateFields
        api_response = api_instance.save_template_fields(generic_listings_save_template_fields_request)
        print("The response of GenericListingsApi->save_template_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenericListingsApi->save_template_fields: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generic_listings_save_template_fields_request** | [**GenericListingsSaveTemplateFieldsRequest**](GenericListingsSaveTemplateFieldsRequest.md)|  | 

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

