# linnworks_api.generated.email.EmailApi

All URIs are relative to *https://eu-ext.linnworks.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_adhoc_email**](EmailApi.md#generate_adhoc_email) | **POST** /api/Email/GenerateAdhocEmail | GenerateAdhocEmail
[**generate_free_text_email**](EmailApi.md#generate_free_text_email) | **POST** /api/Email/GenerateFreeTextEmail | GenerateFreeTextEmail
[**get_email_template**](EmailApi.md#get_email_template) | **GET** /api/Email/GetEmailTemplate | GetEmailTemplate
[**get_email_templates**](EmailApi.md#get_email_templates) | **GET** /api/Email/GetEmailTemplates | GetEmailTemplates


# **generate_adhoc_email**
> GenerateAdhocEmailResponse generate_adhoc_email(email_generate_adhoc_email_request)

GenerateAdhocEmail

Generate a custom email <b>Permissions Required: </b> GlobalPermissions.Email.SendEmails.SendAdhocEmailsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.email
from linnworks_api.generated.email.models.email_generate_adhoc_email_request import EmailGenerateAdhocEmailRequest
from linnworks_api.generated.email.models.generate_adhoc_email_response import GenerateAdhocEmailResponse
from linnworks_api.generated.email.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.email.Configuration(
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
with linnworks_api.generated.email.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.email.EmailApi(api_client)
    email_generate_adhoc_email_request = linnworks_api.generated.email.EmailGenerateAdhocEmailRequest() # EmailGenerateAdhocEmailRequest | 

    try:
        # GenerateAdhocEmail
        api_response = api_instance.generate_adhoc_email(email_generate_adhoc_email_request)
        print("The response of EmailApi->generate_adhoc_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->generate_adhoc_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_generate_adhoc_email_request** | [**EmailGenerateAdhocEmailRequest**](EmailGenerateAdhocEmailRequest.md)|  | 

### Return type

[**GenerateAdhocEmailResponse**](GenerateAdhocEmailResponse.md)

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

# **generate_free_text_email**
> GenerateFreeTextEmailResponse generate_free_text_email(email_generate_free_text_email_request)

GenerateFreeTextEmail

Generate a custom email <b>Permissions Required: </b> GlobalPermissions.Email.SendEmails.SendFreeTextEmailsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.email
from linnworks_api.generated.email.models.email_generate_free_text_email_request import EmailGenerateFreeTextEmailRequest
from linnworks_api.generated.email.models.generate_free_text_email_response import GenerateFreeTextEmailResponse
from linnworks_api.generated.email.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.email.Configuration(
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
with linnworks_api.generated.email.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.email.EmailApi(api_client)
    email_generate_free_text_email_request = linnworks_api.generated.email.EmailGenerateFreeTextEmailRequest() # EmailGenerateFreeTextEmailRequest | 

    try:
        # GenerateFreeTextEmail
        api_response = api_instance.generate_free_text_email(email_generate_free_text_email_request)
        print("The response of EmailApi->generate_free_text_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->generate_free_text_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_generate_free_text_email_request** | [**EmailGenerateFreeTextEmailRequest**](EmailGenerateFreeTextEmailRequest.md)|  | 

### Return type

[**GenerateFreeTextEmailResponse**](GenerateFreeTextEmailResponse.md)

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

# **get_email_template**
> EmailTemplate get_email_template(pk_email_template_row_id=pk_email_template_row_id)

GetEmailTemplate

Get the full data of a specific email template <b>Permissions Required: </b> GlobalPermissions.Email.Templates.GetEmailTemplateNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.email
from linnworks_api.generated.email.models.email_template import EmailTemplate
from linnworks_api.generated.email.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.email.Configuration(
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
with linnworks_api.generated.email.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.email.EmailApi(api_client)
    pk_email_template_row_id = 56 # int | Id of the email template to retrieve (optional)

    try:
        # GetEmailTemplate
        api_response = api_instance.get_email_template(pk_email_template_row_id=pk_email_template_row_id)
        print("The response of EmailApi->get_email_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->get_email_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pk_email_template_row_id** | **int**| Id of the email template to retrieve | [optional] 

### Return type

[**EmailTemplate**](EmailTemplate.md)

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

# **get_email_templates**
> List[EmailTemplateHeader] get_email_templates()

GetEmailTemplates

Get the whole list of email header templates <b>Permissions Required: </b> GlobalPermissions.Email.Templates.GetEmailTemplatesNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.email
from linnworks_api.generated.email.models.email_template_header import EmailTemplateHeader
from linnworks_api.generated.email.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.email.Configuration(
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
with linnworks_api.generated.email.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.email.EmailApi(api_client)

    try:
        # GetEmailTemplates
        api_response = api_instance.get_email_templates()
        print("The response of EmailApi->get_email_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->get_email_templates: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[EmailTemplateHeader]**](EmailTemplateHeader.md)

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

