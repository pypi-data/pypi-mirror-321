# linnworks_api.generated.auth.AuthApi

All URIs are relative to *https://api.linnworks.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorize_by_application**](AuthApi.md#authorize_by_application) | **POST** /api/Auth/AuthorizeByApplication | AuthorizeByApplication
[**get_application_profile_by_secret_key**](AuthApi.md#get_application_profile_by_secret_key) | **POST** /api/Auth/GetApplicationProfileBySecretKey | GetApplicationProfileBySecretKey


# **authorize_by_application**
> BaseSession authorize_by_application(request=request)

AuthorizeByApplication

Generates a sesssion and provide Authorization Token and server in response. <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example


```python
import linnworks_api.generated.auth
from linnworks_api.generated.auth.models.authorize_by_application_request import AuthorizeByApplicationRequest
from linnworks_api.generated.auth.models.base_session import BaseSession
from linnworks_api.generated.auth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.auth.Configuration(
    host = "https://api.linnworks.net"
)


# Enter a context with an instance of the API client
with linnworks_api.generated.auth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.auth.AuthApi(api_client)
    request = linnworks_api.generated.auth.AuthorizeByApplicationRequest() # AuthorizeByApplicationRequest |  (optional)

    try:
        # AuthorizeByApplication
        api_response = api_instance.authorize_by_application(request=request)
        print("The response of AuthApi->authorize_by_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->authorize_by_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**AuthorizeByApplicationRequest**](AuthorizeByApplicationRequest.md)|  | [optional] 

### Return type

[**BaseSession**](BaseSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_profile_by_secret_key**
> ApplicationProfileResponse get_application_profile_by_secret_key(auth_get_application_profile_by_secret_key_request)

GetApplicationProfileBySecretKey

Returns current application subscription profile information for a given application for a specific user.   You can use this method to get the current application subscription after AuthorizedByApplication returned a session.   The session will contain Id, this is the UserId you need to supply in the call.  If there are no current subscriptions for the application for the user. The method will return null (nothing) <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example


```python
import linnworks_api.generated.auth
from linnworks_api.generated.auth.models.application_profile_response import ApplicationProfileResponse
from linnworks_api.generated.auth.models.auth_get_application_profile_by_secret_key_request import AuthGetApplicationProfileBySecretKeyRequest
from linnworks_api.generated.auth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.auth.Configuration(
    host = "https://api.linnworks.net"
)


# Enter a context with an instance of the API client
with linnworks_api.generated.auth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.auth.AuthApi(api_client)
    auth_get_application_profile_by_secret_key_request = linnworks_api.generated.auth.AuthGetApplicationProfileBySecretKeyRequest() # AuthGetApplicationProfileBySecretKeyRequest | 

    try:
        # GetApplicationProfileBySecretKey
        api_response = api_instance.get_application_profile_by_secret_key(auth_get_application_profile_by_secret_key_request)
        print("The response of AuthApi->get_application_profile_by_secret_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->get_application_profile_by_secret_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_get_application_profile_by_secret_key_request** | [**AuthGetApplicationProfileBySecretKeyRequest**](AuthGetApplicationProfileBySecretKeyRequest.md)|  | 

### Return type

[**ApplicationProfileResponse**](ApplicationProfileResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

