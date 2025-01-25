# linnworks_api.generated.macro.MacroApi

All URIs are relative to *https://eu-ext.linnworks.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_installed_macros**](MacroApi.md#get_installed_macros) | **GET** /api/Macro/GetInstalledMacros | GetInstalledMacros
[**get_macro_configurations**](MacroApi.md#get_macro_configurations) | **GET** /api/Macro/GetMacroConfigurations | GetMacroConfigurations


# **get_installed_macros**
> GetInstalledMacrosResponse get_installed_macros()

GetInstalledMacros

Get a list of all macros and their related applications as installed on the users system <b>Permissions Required: </b> GlobalPermissions.Applications.MacroConfigurationNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.macro
from linnworks_api.generated.macro.models.get_installed_macros_response import GetInstalledMacrosResponse
from linnworks_api.generated.macro.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.macro.Configuration(
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
with linnworks_api.generated.macro.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.macro.MacroApi(api_client)

    try:
        # GetInstalledMacros
        api_response = api_instance.get_installed_macros()
        print("The response of MacroApi->get_installed_macros:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MacroApi->get_installed_macros: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetInstalledMacrosResponse**](GetInstalledMacrosResponse.md)

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

# **get_macro_configurations**
> List[MacroRegister] get_macro_configurations()

GetMacroConfigurations

Get all the macro configurations for the user account <b>Permissions Required: </b> GlobalPermissions.Applications.MacroConfigurationNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.macro
from linnworks_api.generated.macro.models.macro_register import MacroRegister
from linnworks_api.generated.macro.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.macro.Configuration(
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
with linnworks_api.generated.macro.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.macro.MacroApi(api_client)

    try:
        # GetMacroConfigurations
        api_response = api_instance.get_macro_configurations()
        print("The response of MacroApi->get_macro_configurations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MacroApi->get_macro_configurations: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[MacroRegister]**](MacroRegister.md)

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

