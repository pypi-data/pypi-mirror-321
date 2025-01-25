# linnworks_api.generated.warehousetransfer_new.ImportApi

All URIs are relative to *https://eu-api.linnworks.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**warehousetransfer_import_importshipmentitems_shipping_plan_id_post**](ImportApi.md#warehousetransfer_import_importshipmentitems_shipping_plan_id_post) | **POST** /warehousetransfer/Import/importshipmentitems/{shippingPlanId} | ImportCsv
[**warehousetransfer_import_importstockrequestitems_transfer_id_post**](ImportApi.md#warehousetransfer_import_importstockrequestitems_transfer_id_post) | **POST** /warehousetransfer/Import/importstockrequestitems/{transferId} | ImportCsv
[**warehousetransfer_import_importstocktransferitems_transfer_id_post**](ImportApi.md#warehousetransfer_import_importstocktransferitems_transfer_id_post) | **POST** /warehousetransfer/Import/importstocktransferitems/{transferId} | ImportCsv
[**warehousetransfer_import_upload_import_type_post**](ImportApi.md#warehousetransfer_import_upload_import_type_post) | **POST** /warehousetransfer/Import/upload/{importType} | UploadCsv


# **warehousetransfer_import_importshipmentitems_shipping_plan_id_post**
> ImportProductsToShipmentResponse warehousetransfer_import_importshipmentitems_shipping_plan_id_post(shipping_plan_id, import_products_to_shipment_request=import_products_to_shipment_request)

ImportCsv

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.import_products_to_shipment_request import ImportProductsToShipmentRequest
from linnworks_api.generated.warehousetransfer_new.models.import_products_to_shipment_response import ImportProductsToShipmentResponse
from linnworks_api.generated.warehousetransfer_new.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-api.linnworks.net/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.warehousetransfer_new.Configuration(
    host = "https://eu-api.linnworks.net/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Linnworks
configuration.api_key['Linnworks'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Linnworks'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.warehousetransfer_new.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.warehousetransfer_new.ImportApi(api_client)
    shipping_plan_id = 'shipping_plan_id_example' # str | 
    import_products_to_shipment_request = linnworks_api.generated.warehousetransfer_new.ImportProductsToShipmentRequest() # ImportProductsToShipmentRequest |  (optional)

    try:
        # ImportCsv
        api_response = api_instance.warehousetransfer_import_importshipmentitems_shipping_plan_id_post(shipping_plan_id, import_products_to_shipment_request=import_products_to_shipment_request)
        print("The response of ImportApi->warehousetransfer_import_importshipmentitems_shipping_plan_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->warehousetransfer_import_importshipmentitems_shipping_plan_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_plan_id** | **str**|  | 
 **import_products_to_shipment_request** | [**ImportProductsToShipmentRequest**](ImportProductsToShipmentRequest.md)|  | [optional] 

### Return type

[**ImportProductsToShipmentResponse**](ImportProductsToShipmentResponse.md)

### Authorization

[Linnworks](../README.md#Linnworks)

### HTTP request headers

 - **Content-Type**: application/json-patch+json; x-api-version=1.0, application/json; x-api-version=1.0, text/json; x-api-version=1.0, application/*+json; x-api-version=1.0
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**201** | Success |  -  |
**204** | Success |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehousetransfer_import_importstockrequestitems_transfer_id_post**
> ImportProductsToStockRequestResponse warehousetransfer_import_importstockrequestitems_transfer_id_post(transfer_id, import_products_to_stock_request_request=import_products_to_stock_request_request)

ImportCsv

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.import_products_to_stock_request_request import ImportProductsToStockRequestRequest
from linnworks_api.generated.warehousetransfer_new.models.import_products_to_stock_request_response import ImportProductsToStockRequestResponse
from linnworks_api.generated.warehousetransfer_new.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-api.linnworks.net/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.warehousetransfer_new.Configuration(
    host = "https://eu-api.linnworks.net/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Linnworks
configuration.api_key['Linnworks'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Linnworks'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.warehousetransfer_new.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.warehousetransfer_new.ImportApi(api_client)
    transfer_id = 'transfer_id_example' # str | 
    import_products_to_stock_request_request = linnworks_api.generated.warehousetransfer_new.ImportProductsToStockRequestRequest() # ImportProductsToStockRequestRequest |  (optional)

    try:
        # ImportCsv
        api_response = api_instance.warehousetransfer_import_importstockrequestitems_transfer_id_post(transfer_id, import_products_to_stock_request_request=import_products_to_stock_request_request)
        print("The response of ImportApi->warehousetransfer_import_importstockrequestitems_transfer_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->warehousetransfer_import_importstockrequestitems_transfer_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_id** | **str**|  | 
 **import_products_to_stock_request_request** | [**ImportProductsToStockRequestRequest**](ImportProductsToStockRequestRequest.md)|  | [optional] 

### Return type

[**ImportProductsToStockRequestResponse**](ImportProductsToStockRequestResponse.md)

### Authorization

[Linnworks](../README.md#Linnworks)

### HTTP request headers

 - **Content-Type**: application/json-patch+json; x-api-version=1.0, application/json; x-api-version=1.0, text/json; x-api-version=1.0, application/*+json; x-api-version=1.0
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**201** | Success |  -  |
**204** | Success |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehousetransfer_import_importstocktransferitems_transfer_id_post**
> ImportProductsToStockTransferResponse warehousetransfer_import_importstocktransferitems_transfer_id_post(transfer_id, import_products_to_stock_transfer_request=import_products_to_stock_transfer_request)

ImportCsv

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.import_products_to_stock_transfer_request import ImportProductsToStockTransferRequest
from linnworks_api.generated.warehousetransfer_new.models.import_products_to_stock_transfer_response import ImportProductsToStockTransferResponse
from linnworks_api.generated.warehousetransfer_new.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-api.linnworks.net/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.warehousetransfer_new.Configuration(
    host = "https://eu-api.linnworks.net/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Linnworks
configuration.api_key['Linnworks'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Linnworks'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.warehousetransfer_new.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.warehousetransfer_new.ImportApi(api_client)
    transfer_id = 'transfer_id_example' # str | 
    import_products_to_stock_transfer_request = linnworks_api.generated.warehousetransfer_new.ImportProductsToStockTransferRequest() # ImportProductsToStockTransferRequest |  (optional)

    try:
        # ImportCsv
        api_response = api_instance.warehousetransfer_import_importstocktransferitems_transfer_id_post(transfer_id, import_products_to_stock_transfer_request=import_products_to_stock_transfer_request)
        print("The response of ImportApi->warehousetransfer_import_importstocktransferitems_transfer_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->warehousetransfer_import_importstocktransferitems_transfer_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_id** | **str**|  | 
 **import_products_to_stock_transfer_request** | [**ImportProductsToStockTransferRequest**](ImportProductsToStockTransferRequest.md)|  | [optional] 

### Return type

[**ImportProductsToStockTransferResponse**](ImportProductsToStockTransferResponse.md)

### Authorization

[Linnworks](../README.md#Linnworks)

### HTTP request headers

 - **Content-Type**: application/json-patch+json; x-api-version=1.0, application/json; x-api-version=1.0, text/json; x-api-version=1.0, application/*+json; x-api-version=1.0
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**201** | Success |  -  |
**204** | Success |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehousetransfer_import_upload_import_type_post**
> UploadCsvResponse warehousetransfer_import_upload_import_type_post(import_type)

UploadCsv

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.import_type import ImportType
from linnworks_api.generated.warehousetransfer_new.models.upload_csv_response import UploadCsvResponse
from linnworks_api.generated.warehousetransfer_new.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-api.linnworks.net/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.warehousetransfer_new.Configuration(
    host = "https://eu-api.linnworks.net/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Linnworks
configuration.api_key['Linnworks'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Linnworks'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.warehousetransfer_new.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.warehousetransfer_new.ImportApi(api_client)
    import_type = linnworks_api.generated.warehousetransfer_new.ImportType() # ImportType | 

    try:
        # UploadCsv
        api_response = api_instance.warehousetransfer_import_upload_import_type_post(import_type)
        print("The response of ImportApi->warehousetransfer_import_upload_import_type_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->warehousetransfer_import_upload_import_type_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_type** | [**ImportType**](.md)|  | 

### Return type

[**UploadCsvResponse**](UploadCsvResponse.md)

### Authorization

[Linnworks](../README.md#Linnworks)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**201** | Success |  -  |
**204** | Success |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

