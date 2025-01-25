# linnworks_api.generated.printservice.PrintServiceApi

All URIs are relative to *https://eu-ext.linnworks.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_pd_ffrom_job_force_template**](PrintServiceApi.md#create_pd_ffrom_job_force_template) | **POST** /api/PrintService/CreatePDFfromJobForceTemplate | CreatePDFfromJobForceTemplate
[**create_pd_ffrom_job_force_template_stock_in**](PrintServiceApi.md#create_pd_ffrom_job_force_template_stock_in) | **POST** /api/PrintService/CreatePDFfromJobForceTemplateStockIn | CreatePDFfromJobForceTemplateStockIn
[**create_pd_ffrom_job_force_template_with_quantities**](PrintServiceApi.md#create_pd_ffrom_job_force_template_with_quantities) | **POST** /api/PrintService/CreatePDFfromJobForceTemplateWithQuantities | CreatePDFfromJobForceTemplateWithQuantities
[**create_return_shipping_labels_pdf**](PrintServiceApi.md#create_return_shipping_labels_pdf) | **POST** /api/PrintService/CreateReturnShippingLabelsPDF | CreateReturnShippingLabelsPDF
[**create_return_shipping_labels_pdf_with_skus**](PrintServiceApi.md#create_return_shipping_labels_pdf_with_skus) | **POST** /api/PrintService/CreateReturnShippingLabelsPDFWithSKUs | CreateReturnShippingLabelsPDFWithSKUs
[**get_template_list**](PrintServiceApi.md#get_template_list) | **GET** /api/PrintService/GetTemplateList | GetTemplateList
[**get_users_for_printer_config**](PrintServiceApi.md#get_users_for_printer_config) | **GET** /api/PrintService/GetUsersForPrinterConfig | GetUsersForPrinterConfig
[**print_template_preview**](PrintServiceApi.md#print_template_preview) | **POST** /api/PrintService/PrintTemplatePreview | PrintTemplatePreview
[**v_p_get_printers**](PrintServiceApi.md#v_p_get_printers) | **GET** /api/PrintService/VP_GetPrinters | VP_GetPrinters


# **create_pd_ffrom_job_force_template**
> CreatePDFResult create_pd_ffrom_job_force_template(print_service_create_pd_ffrom_job_force_template_request)

CreatePDFfromJobForceTemplate

Creates a PDF file from a print job request <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>250</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.printservice
from linnworks_api.generated.printservice.models.create_pdf_result import CreatePDFResult
from linnworks_api.generated.printservice.models.print_service_create_pd_ffrom_job_force_template_request import PrintServiceCreatePDFfromJobForceTemplateRequest
from linnworks_api.generated.printservice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.printservice.Configuration(
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
with linnworks_api.generated.printservice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.printservice.PrintServiceApi(api_client)
    print_service_create_pd_ffrom_job_force_template_request = linnworks_api.generated.printservice.PrintServiceCreatePDFfromJobForceTemplateRequest() # PrintServiceCreatePDFfromJobForceTemplateRequest | 

    try:
        # CreatePDFfromJobForceTemplate
        api_response = api_instance.create_pd_ffrom_job_force_template(print_service_create_pd_ffrom_job_force_template_request)
        print("The response of PrintServiceApi->create_pd_ffrom_job_force_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrintServiceApi->create_pd_ffrom_job_force_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **print_service_create_pd_ffrom_job_force_template_request** | [**PrintServiceCreatePDFfromJobForceTemplateRequest**](PrintServiceCreatePDFfromJobForceTemplateRequest.md)|  | 

### Return type

[**CreatePDFResult**](CreatePDFResult.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_pd_ffrom_job_force_template_stock_in**
> CreatePDFResult create_pd_ffrom_job_force_template_stock_in(print_service_create_pd_ffrom_job_force_template_stock_in_request)

CreatePDFfromJobForceTemplateStockIn

Creates a PDF file from a print job request <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.printservice
from linnworks_api.generated.printservice.models.create_pdf_result import CreatePDFResult
from linnworks_api.generated.printservice.models.print_service_create_pd_ffrom_job_force_template_stock_in_request import PrintServiceCreatePDFfromJobForceTemplateStockInRequest
from linnworks_api.generated.printservice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.printservice.Configuration(
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
with linnworks_api.generated.printservice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.printservice.PrintServiceApi(api_client)
    print_service_create_pd_ffrom_job_force_template_stock_in_request = linnworks_api.generated.printservice.PrintServiceCreatePDFfromJobForceTemplateStockInRequest() # PrintServiceCreatePDFfromJobForceTemplateStockInRequest | 

    try:
        # CreatePDFfromJobForceTemplateStockIn
        api_response = api_instance.create_pd_ffrom_job_force_template_stock_in(print_service_create_pd_ffrom_job_force_template_stock_in_request)
        print("The response of PrintServiceApi->create_pd_ffrom_job_force_template_stock_in:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrintServiceApi->create_pd_ffrom_job_force_template_stock_in: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **print_service_create_pd_ffrom_job_force_template_stock_in_request** | [**PrintServiceCreatePDFfromJobForceTemplateStockInRequest**](PrintServiceCreatePDFfromJobForceTemplateStockInRequest.md)|  | 

### Return type

[**CreatePDFResult**](CreatePDFResult.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_pd_ffrom_job_force_template_with_quantities**
> CreatePDFResult create_pd_ffrom_job_force_template_with_quantities(print_service_create_pd_ffrom_job_force_template_with_quantities_request)

CreatePDFfromJobForceTemplateWithQuantities

Creates a PDF file with Stock Item labels from a print job request <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.printservice
from linnworks_api.generated.printservice.models.create_pdf_result import CreatePDFResult
from linnworks_api.generated.printservice.models.print_service_create_pd_ffrom_job_force_template_with_quantities_request import PrintServiceCreatePDFfromJobForceTemplateWithQuantitiesRequest
from linnworks_api.generated.printservice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.printservice.Configuration(
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
with linnworks_api.generated.printservice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.printservice.PrintServiceApi(api_client)
    print_service_create_pd_ffrom_job_force_template_with_quantities_request = linnworks_api.generated.printservice.PrintServiceCreatePDFfromJobForceTemplateWithQuantitiesRequest() # PrintServiceCreatePDFfromJobForceTemplateWithQuantitiesRequest | 

    try:
        # CreatePDFfromJobForceTemplateWithQuantities
        api_response = api_instance.create_pd_ffrom_job_force_template_with_quantities(print_service_create_pd_ffrom_job_force_template_with_quantities_request)
        print("The response of PrintServiceApi->create_pd_ffrom_job_force_template_with_quantities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrintServiceApi->create_pd_ffrom_job_force_template_with_quantities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **print_service_create_pd_ffrom_job_force_template_with_quantities_request** | [**PrintServiceCreatePDFfromJobForceTemplateWithQuantitiesRequest**](PrintServiceCreatePDFfromJobForceTemplateWithQuantitiesRequest.md)|  | 

### Return type

[**CreatePDFResult**](CreatePDFResult.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_return_shipping_labels_pdf**
> CreatePDFResult create_return_shipping_labels_pdf(print_service_create_return_shipping_labels_pdf_request)

CreateReturnShippingLabelsPDF

Creates a PDF file of return shipping labels for a single order <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.printservice
from linnworks_api.generated.printservice.models.create_pdf_result import CreatePDFResult
from linnworks_api.generated.printservice.models.print_service_create_return_shipping_labels_pdf_request import PrintServiceCreateReturnShippingLabelsPDFRequest
from linnworks_api.generated.printservice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.printservice.Configuration(
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
with linnworks_api.generated.printservice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.printservice.PrintServiceApi(api_client)
    print_service_create_return_shipping_labels_pdf_request = linnworks_api.generated.printservice.PrintServiceCreateReturnShippingLabelsPDFRequest() # PrintServiceCreateReturnShippingLabelsPDFRequest | 

    try:
        # CreateReturnShippingLabelsPDF
        api_response = api_instance.create_return_shipping_labels_pdf(print_service_create_return_shipping_labels_pdf_request)
        print("The response of PrintServiceApi->create_return_shipping_labels_pdf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrintServiceApi->create_return_shipping_labels_pdf: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **print_service_create_return_shipping_labels_pdf_request** | [**PrintServiceCreateReturnShippingLabelsPDFRequest**](PrintServiceCreateReturnShippingLabelsPDFRequest.md)|  | 

### Return type

[**CreatePDFResult**](CreatePDFResult.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_return_shipping_labels_pdf_with_skus**
> CreatePDFResult create_return_shipping_labels_pdf_with_skus(print_service_create_return_shipping_labels_pdf_with_skus_request)

CreateReturnShippingLabelsPDFWithSKUs

Creates a PDF file of return shipping labels for a single order <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.printservice
from linnworks_api.generated.printservice.models.create_pdf_result import CreatePDFResult
from linnworks_api.generated.printservice.models.print_service_create_return_shipping_labels_pdf_with_skus_request import PrintServiceCreateReturnShippingLabelsPDFWithSKUsRequest
from linnworks_api.generated.printservice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.printservice.Configuration(
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
with linnworks_api.generated.printservice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.printservice.PrintServiceApi(api_client)
    print_service_create_return_shipping_labels_pdf_with_skus_request = linnworks_api.generated.printservice.PrintServiceCreateReturnShippingLabelsPDFWithSKUsRequest() # PrintServiceCreateReturnShippingLabelsPDFWithSKUsRequest | 

    try:
        # CreateReturnShippingLabelsPDFWithSKUs
        api_response = api_instance.create_return_shipping_labels_pdf_with_skus(print_service_create_return_shipping_labels_pdf_with_skus_request)
        print("The response of PrintServiceApi->create_return_shipping_labels_pdf_with_skus:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrintServiceApi->create_return_shipping_labels_pdf_with_skus: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **print_service_create_return_shipping_labels_pdf_with_skus_request** | [**PrintServiceCreateReturnShippingLabelsPDFWithSKUsRequest**](PrintServiceCreateReturnShippingLabelsPDFWithSKUsRequest.md)|  | 

### Return type

[**CreatePDFResult**](CreatePDFResult.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_list**
> List[TemplateHeader] get_template_list(template_type=template_type)

GetTemplateList

Get list of templates for a specific type <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.printservice
from linnworks_api.generated.printservice.models.template_header import TemplateHeader
from linnworks_api.generated.printservice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.printservice.Configuration(
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
with linnworks_api.generated.printservice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.printservice.PrintServiceApi(api_client)
    template_type = 'template_type_example' # str | The template type to load (e.g. Warehouse Transfer). Empty body will return them all (optional)

    try:
        # GetTemplateList
        api_response = api_instance.get_template_list(template_type=template_type)
        print("The response of PrintServiceApi->get_template_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrintServiceApi->get_template_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_type** | **str**| The template type to load (e.g. Warehouse Transfer). Empty body will return them all | [optional] 

### Return type

[**List[TemplateHeader]**](TemplateHeader.md)

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

# **get_users_for_printer_config**
> List[PermissionsUser] get_users_for_printer_config()

GetUsersForPrinterConfig

Gets a list of users for printer configuration. Only super admin can get the full list. Non super admins can only get their own user <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.printservice
from linnworks_api.generated.printservice.models.permissions_user import PermissionsUser
from linnworks_api.generated.printservice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.printservice.Configuration(
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
with linnworks_api.generated.printservice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.printservice.PrintServiceApi(api_client)

    try:
        # GetUsersForPrinterConfig
        api_response = api_instance.get_users_for_printer_config()
        print("The response of PrintServiceApi->get_users_for_printer_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrintServiceApi->get_users_for_printer_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[PermissionsUser]**](PermissionsUser.md)

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

# **print_template_preview**
> CreatePDFResult print_template_preview(print_service_print_template_preview_request)

PrintTemplatePreview

Generate a PDF preview of a specific template <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.printservice
from linnworks_api.generated.printservice.models.create_pdf_result import CreatePDFResult
from linnworks_api.generated.printservice.models.print_service_print_template_preview_request import PrintServicePrintTemplatePreviewRequest
from linnworks_api.generated.printservice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.printservice.Configuration(
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
with linnworks_api.generated.printservice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.printservice.PrintServiceApi(api_client)
    print_service_print_template_preview_request = linnworks_api.generated.printservice.PrintServicePrintTemplatePreviewRequest() # PrintServicePrintTemplatePreviewRequest | 

    try:
        # PrintTemplatePreview
        api_response = api_instance.print_template_preview(print_service_print_template_preview_request)
        print("The response of PrintServiceApi->print_template_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrintServiceApi->print_template_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **print_service_print_template_preview_request** | [**PrintServicePrintTemplatePreviewRequest**](PrintServicePrintTemplatePreviewRequest.md)|  | 

### Return type

[**CreatePDFResult**](CreatePDFResult.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v_p_get_printers**
> List[VirtualPrinter] v_p_get_printers()

VP_GetPrinters

Gets list of virtual printers. <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>250</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.printservice
from linnworks_api.generated.printservice.models.virtual_printer import VirtualPrinter
from linnworks_api.generated.printservice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.printservice.Configuration(
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
with linnworks_api.generated.printservice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.printservice.PrintServiceApi(api_client)

    try:
        # VP_GetPrinters
        api_response = api_instance.v_p_get_printers()
        print("The response of PrintServiceApi->v_p_get_printers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrintServiceApi->v_p_get_printers: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[VirtualPrinter]**](VirtualPrinter.md)

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

