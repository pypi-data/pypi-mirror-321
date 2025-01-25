# linnworks_api.generated.shippingservice.ShippingServiceApi

All URIs are relative to *https://eu-ext.linnworks.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_order_shipping_label**](ShippingServiceApi.md#cancel_order_shipping_label) | **POST** /api/ShippingService/CancelOrderShippingLabel | CancelOrderShippingLabel
[**get_consignments_by_manifest**](ShippingServiceApi.md#get_consignments_by_manifest) | **GET** /api/ShippingService/GetConsignmentsByManifest | GetConsignmentsByManifest
[**get_filed_manifests_by_vendor**](ShippingServiceApi.md#get_filed_manifests_by_vendor) | **GET** /api/ShippingService/GetFiledManifestsByVendor | GetFiledManifestsByVendor
[**get_integrations**](ShippingServiceApi.md#get_integrations) | **GET** /api/ShippingService/GetIntegrations | GetIntegrations
[**post_shipment_upload**](ShippingServiceApi.md#post_shipment_upload) | **POST** /api/ShippingService/PostShipmentUpload | PostShipmentUpload


# **cancel_order_shipping_label**
> CancelOrderShippingLabelResponse cancel_order_shipping_label(shipping_service_cancel_order_shipping_label_request)

CancelOrderShippingLabel

Cancels the shipping label for an order <b>Permissions Required: </b> GlobalPermissions.ShippingService.ShippingLabelNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.shippingservice
from linnworks_api.generated.shippingservice.models.cancel_order_shipping_label_response import CancelOrderShippingLabelResponse
from linnworks_api.generated.shippingservice.models.shipping_service_cancel_order_shipping_label_request import ShippingServiceCancelOrderShippingLabelRequest
from linnworks_api.generated.shippingservice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.shippingservice.Configuration(
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
with linnworks_api.generated.shippingservice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.shippingservice.ShippingServiceApi(api_client)
    shipping_service_cancel_order_shipping_label_request = linnworks_api.generated.shippingservice.ShippingServiceCancelOrderShippingLabelRequest() # ShippingServiceCancelOrderShippingLabelRequest | 

    try:
        # CancelOrderShippingLabel
        api_response = api_instance.cancel_order_shipping_label(shipping_service_cancel_order_shipping_label_request)
        print("The response of ShippingServiceApi->cancel_order_shipping_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingServiceApi->cancel_order_shipping_label: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_service_cancel_order_shipping_label_request** | [**ShippingServiceCancelOrderShippingLabelRequest**](ShippingServiceCancelOrderShippingLabelRequest.md)|  | 

### Return type

[**CancelOrderShippingLabelResponse**](CancelOrderShippingLabelResponse.md)

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

# **get_consignments_by_manifest**
> GenericPagedResultConsignment get_consignments_by_manifest(vendor=vendor, account_id=account_id, pk_manifest_id=pk_manifest_id, external_manifest_id=external_manifest_id, manifest_date=manifest_date)

GetConsignmentsByManifest

Get paged list of consignments for a specific vendor, account id and manifest id. Use /ShippingService/GetFiledManifestsByVendor for input arguments. <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>10</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.shippingservice
from linnworks_api.generated.shippingservice.models.generic_paged_result_consignment import GenericPagedResultConsignment
from linnworks_api.generated.shippingservice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.shippingservice.Configuration(
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
with linnworks_api.generated.shippingservice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.shippingservice.ShippingServiceApi(api_client)
    vendor = 'vendor_example' # str | Vendor name (optional)
    account_id = 'account_id_example' # str | Account id (optional)
    pk_manifest_id = 56 # int | Manifest id (optional)
    external_manifest_id = 'external_manifest_id_example' # str | External manifest id. If is null, all consignments for this account will be returned (optional)
    manifest_date = '2013-10-20T19:20:30+01:00' # datetime | The date at which the manifest was filed. Leave empty. (optional)

    try:
        # GetConsignmentsByManifest
        api_response = api_instance.get_consignments_by_manifest(vendor=vendor, account_id=account_id, pk_manifest_id=pk_manifest_id, external_manifest_id=external_manifest_id, manifest_date=manifest_date)
        print("The response of ShippingServiceApi->get_consignments_by_manifest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingServiceApi->get_consignments_by_manifest: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor** | **str**| Vendor name | [optional] 
 **account_id** | **str**| Account id | [optional] 
 **pk_manifest_id** | **int**| Manifest id | [optional] 
 **external_manifest_id** | **str**| External manifest id. If is null, all consignments for this account will be returned | [optional] 
 **manifest_date** | **datetime**| The date at which the manifest was filed. Leave empty. | [optional] 

### Return type

[**GenericPagedResultConsignment**](GenericPagedResultConsignment.md)

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

# **get_filed_manifests_by_vendor**
> GenericPagedResultFiledManifest get_filed_manifests_by_vendor(vendor=vendor, vendor_friendly_name=vendor_friendly_name, var_from=var_from, to=to, page_number=page_number, entries_per_page=entries_per_page)

GetFiledManifestsByVendor

Gets a paged list of filed manifest by vendor between two dates. Use /ShippingService/GetIntegrations to get all vendors and friendly names <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>10</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.shippingservice
from linnworks_api.generated.shippingservice.models.generic_paged_result_filed_manifest import GenericPagedResultFiledManifest
from linnworks_api.generated.shippingservice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.shippingservice.Configuration(
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
with linnworks_api.generated.shippingservice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.shippingservice.ShippingServiceApi(api_client)
    vendor = 'vendor_example' # str | Vendor name (optional)
    vendor_friendly_name = 'vendor_friendly_name_example' # str | Vendor friendly name (optional)
    var_from = '2013-10-20T19:20:30+01:00' # datetime | From date (optional)
    to = '2013-10-20T19:20:30+01:00' # datetime | To date (optional)
    page_number = 56 # int | Page number (optional)
    entries_per_page = 56 # int | Entries per page (optional)

    try:
        # GetFiledManifestsByVendor
        api_response = api_instance.get_filed_manifests_by_vendor(vendor=vendor, vendor_friendly_name=vendor_friendly_name, var_from=var_from, to=to, page_number=page_number, entries_per_page=entries_per_page)
        print("The response of ShippingServiceApi->get_filed_manifests_by_vendor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingServiceApi->get_filed_manifests_by_vendor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor** | **str**| Vendor name | [optional] 
 **vendor_friendly_name** | **str**| Vendor friendly name | [optional] 
 **var_from** | **datetime**| From date | [optional] 
 **to** | **datetime**| To date | [optional] 
 **page_number** | **int**| Page number | [optional] 
 **entries_per_page** | **int**| Entries per page | [optional] 

### Return type

[**GenericPagedResultFiledManifest**](GenericPagedResultFiledManifest.md)

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

# **get_integrations**
> List[SystemShippingAPIConfig] get_integrations()

GetIntegrations

Gets all configured vendor integrations <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>1</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.shippingservice
from linnworks_api.generated.shippingservice.models.system_shipping_api_config import SystemShippingAPIConfig
from linnworks_api.generated.shippingservice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.shippingservice.Configuration(
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
with linnworks_api.generated.shippingservice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.shippingservice.ShippingServiceApi(api_client)

    try:
        # GetIntegrations
        api_response = api_instance.get_integrations()
        print("The response of ShippingServiceApi->get_integrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingServiceApi->get_integrations: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[SystemShippingAPIConfig]**](SystemShippingAPIConfig.md)

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

# **post_shipment_upload**
> post_shipment_upload(request=request)

PostShipmentUpload

 <b>Permissions Required: </b> GlobalPermissions.ShippingService.PostShipmentUploadNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.shippingservice
from linnworks_api.generated.shippingservice.models.post_shipment_upload_request import PostShipmentUploadRequest
from linnworks_api.generated.shippingservice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.shippingservice.Configuration(
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
with linnworks_api.generated.shippingservice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.shippingservice.ShippingServiceApi(api_client)
    request = linnworks_api.generated.shippingservice.PostShipmentUploadRequest() # PostShipmentUploadRequest |  (optional)

    try:
        # PostShipmentUpload
        api_instance.post_shipment_upload(request=request)
    except Exception as e:
        print("Exception when calling ShippingServiceApi->post_shipment_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**PostShipmentUploadRequest**](PostShipmentUploadRequest.md)|  | [optional] 

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

