# linnworks_api.generated.warehousetransfer_new.FbaShipmentTransportApi

All URIs are relative to *https://eu-api.linnworks.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_transport_billoflading_get**](FbaShipmentTransportApi.md#warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_transport_billoflading_get) | **GET** /warehousetransfer/fbainbound/shippingplans/{shippingPlanId}/shipments/{shipmentId}/transport/billoflading | GetBillOfLading
[**warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_transport_confirm_put**](FbaShipmentTransportApi.md#warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_transport_confirm_put) | **PUT** /warehousetransfer/fbainbound/shippingplans/{shippingPlanId}/shipments/{shipmentId}/transport/confirm | ConfirmTransportRequest
[**warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_transport_estimate_put**](FbaShipmentTransportApi.md#warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_transport_estimate_put) | **PUT** /warehousetransfer/fbainbound/shippingplans/{shippingPlanId}/shipments/{shipmentId}/transport/estimate | EstimateTransportContent
[**warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_transport_palletlabels_page_type_get**](FbaShipmentTransportApi.md#warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_transport_palletlabels_page_type_get) | **GET** /warehousetransfer/fbainbound/shippingplans/{shippingPlanId}/shipments/{shipmentId}/transport/palletlabels/{pageType} | GetPalletLabelsRequest
[**warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_transport_put**](FbaShipmentTransportApi.md#warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_transport_put) | **PUT** /warehousetransfer/fbainbound/shippingplans/{shippingPlanId}/shipments/{shipmentId}/transport | SubmitTransportContent
[**warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_transport_uniquepackagelabels_page_type_get**](FbaShipmentTransportApi.md#warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_transport_uniquepackagelabels_page_type_get) | **GET** /warehousetransfer/fbainbound/shippingplans/{shippingPlanId}/shipments/{shipmentId}/transport/uniquepackagelabels/{pageType} | GetUniquePackageLabels
[**warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_transport_void_put**](FbaShipmentTransportApi.md#warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_transport_void_put) | **PUT** /warehousetransfer/fbainbound/shippingplans/{shippingPlanId}/shipments/{shipmentId}/transport/void | VoidTransportRequest


# **warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_transport_billoflading_get**
> AmazonTransportDocumentResponseModel warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_transport_billoflading_get(shipment_id, shipping_plan_id)

GetBillOfLading

Deprecated - please use v2 - [API Docs v2](https://apidocs.linnworks.net/v2/)

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.amazon_transport_document_response_model import AmazonTransportDocumentResponseModel
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
    api_instance = linnworks_api.generated.warehousetransfer_new.FbaShipmentTransportApi(api_client)
    shipment_id = 56 # int | 
    shipping_plan_id = 'shipping_plan_id_example' # str | 

    try:
        # GetBillOfLading
        api_response = api_instance.warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_transport_billoflading_get(shipment_id, shipping_plan_id)
        print("The response of FbaShipmentTransportApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_transport_billoflading_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FbaShipmentTransportApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_transport_billoflading_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **int**|  | 
 **shipping_plan_id** | **str**|  | 

### Return type

[**AmazonTransportDocumentResponseModel**](AmazonTransportDocumentResponseModel.md)

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

# **warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_transport_confirm_put**
> warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_transport_confirm_put(shipment_id, shipping_plan_id)

ConfirmTransportRequest

Deprecated - please use v2 - [API Docs v2](https://apidocs.linnworks.net/v2/)

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
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
    api_instance = linnworks_api.generated.warehousetransfer_new.FbaShipmentTransportApi(api_client)
    shipment_id = 56 # int | 
    shipping_plan_id = 'shipping_plan_id_example' # str | 

    try:
        # ConfirmTransportRequest
        api_instance.warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_transport_confirm_put(shipment_id, shipping_plan_id)
    except Exception as e:
        print("Exception when calling FbaShipmentTransportApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_transport_confirm_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **int**|  | 
 **shipping_plan_id** | **str**|  | 

### Return type

void (empty response body)

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

# **warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_transport_estimate_put**
> warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_transport_estimate_put(shipment_id, shipping_plan_id)

EstimateTransportContent

Deprecated - please use v2 - [API Docs v2](https://apidocs.linnworks.net/v2/)

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
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
    api_instance = linnworks_api.generated.warehousetransfer_new.FbaShipmentTransportApi(api_client)
    shipment_id = 56 # int | 
    shipping_plan_id = 'shipping_plan_id_example' # str | 

    try:
        # EstimateTransportContent
        api_instance.warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_transport_estimate_put(shipment_id, shipping_plan_id)
    except Exception as e:
        print("Exception when calling FbaShipmentTransportApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_transport_estimate_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **int**|  | 
 **shipping_plan_id** | **str**|  | 

### Return type

void (empty response body)

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

# **warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_transport_palletlabels_page_type_get**
> AmazonTransportDocumentResponseModel warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_transport_palletlabels_page_type_get(shipment_id, page_type, shipping_plan_id)

GetPalletLabelsRequest

Deprecated - please use v2 - [API Docs v2](https://apidocs.linnworks.net/v2/)

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.amazon_page_type import AmazonPageType
from linnworks_api.generated.warehousetransfer_new.models.amazon_transport_document_response_model import AmazonTransportDocumentResponseModel
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
    api_instance = linnworks_api.generated.warehousetransfer_new.FbaShipmentTransportApi(api_client)
    shipment_id = 56 # int | 
    page_type = linnworks_api.generated.warehousetransfer_new.AmazonPageType() # AmazonPageType | 
    shipping_plan_id = 'shipping_plan_id_example' # str | 

    try:
        # GetPalletLabelsRequest
        api_response = api_instance.warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_transport_palletlabels_page_type_get(shipment_id, page_type, shipping_plan_id)
        print("The response of FbaShipmentTransportApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_transport_palletlabels_page_type_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FbaShipmentTransportApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_transport_palletlabels_page_type_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **int**|  | 
 **page_type** | [**AmazonPageType**](.md)|  | 
 **shipping_plan_id** | **str**|  | 

### Return type

[**AmazonTransportDocumentResponseModel**](AmazonTransportDocumentResponseModel.md)

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

# **warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_transport_put**
> warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_transport_put(shipment_id, shipping_plan_id, save_transport_content_request=save_transport_content_request)

SubmitTransportContent

Deprecated - please use v2 - [API Docs v2](https://apidocs.linnworks.net/v2/)

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.save_transport_content_request import SaveTransportContentRequest
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
    api_instance = linnworks_api.generated.warehousetransfer_new.FbaShipmentTransportApi(api_client)
    shipment_id = 56 # int | 
    shipping_plan_id = 'shipping_plan_id_example' # str | 
    save_transport_content_request = linnworks_api.generated.warehousetransfer_new.SaveTransportContentRequest() # SaveTransportContentRequest |  (optional)

    try:
        # SubmitTransportContent
        api_instance.warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_transport_put(shipment_id, shipping_plan_id, save_transport_content_request=save_transport_content_request)
    except Exception as e:
        print("Exception when calling FbaShipmentTransportApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_transport_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **int**|  | 
 **shipping_plan_id** | **str**|  | 
 **save_transport_content_request** | [**SaveTransportContentRequest**](SaveTransportContentRequest.md)|  | [optional] 

### Return type

void (empty response body)

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

# **warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_transport_uniquepackagelabels_page_type_get**
> AmazonTransportDocumentResponseModel warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_transport_uniquepackagelabels_page_type_get(shipment_id, page_type, shipping_plan_id)

GetUniquePackageLabels

Deprecated - please use v2 - [API Docs v2](https://apidocs.linnworks.net/v2/)

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.amazon_page_type import AmazonPageType
from linnworks_api.generated.warehousetransfer_new.models.amazon_transport_document_response_model import AmazonTransportDocumentResponseModel
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
    api_instance = linnworks_api.generated.warehousetransfer_new.FbaShipmentTransportApi(api_client)
    shipment_id = 56 # int | 
    page_type = linnworks_api.generated.warehousetransfer_new.AmazonPageType() # AmazonPageType | 
    shipping_plan_id = 'shipping_plan_id_example' # str | 

    try:
        # GetUniquePackageLabels
        api_response = api_instance.warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_transport_uniquepackagelabels_page_type_get(shipment_id, page_type, shipping_plan_id)
        print("The response of FbaShipmentTransportApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_transport_uniquepackagelabels_page_type_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FbaShipmentTransportApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_transport_uniquepackagelabels_page_type_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **int**|  | 
 **page_type** | [**AmazonPageType**](.md)|  | 
 **shipping_plan_id** | **str**|  | 

### Return type

[**AmazonTransportDocumentResponseModel**](AmazonTransportDocumentResponseModel.md)

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

# **warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_transport_void_put**
> warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_transport_void_put(shipment_id, shipping_plan_id)

VoidTransportRequest

Deprecated - please use v2 - [API Docs v2](https://apidocs.linnworks.net/v2/)

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
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
    api_instance = linnworks_api.generated.warehousetransfer_new.FbaShipmentTransportApi(api_client)
    shipment_id = 56 # int | 
    shipping_plan_id = 'shipping_plan_id_example' # str | 

    try:
        # VoidTransportRequest
        api_instance.warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_transport_void_put(shipment_id, shipping_plan_id)
    except Exception as e:
        print("Exception when calling FbaShipmentTransportApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_transport_void_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **int**|  | 
 **shipping_plan_id** | **str**|  | 

### Return type

void (empty response body)

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

