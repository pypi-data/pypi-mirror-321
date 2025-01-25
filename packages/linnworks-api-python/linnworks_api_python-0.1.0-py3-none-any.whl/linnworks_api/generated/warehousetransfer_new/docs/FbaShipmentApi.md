# linnworks_api.generated.warehousetransfer_new.FbaShipmentApi

All URIs are relative to *https://eu-api.linnworks.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_shipment_by_id**](FbaShipmentApi.md#get_shipment_by_id) | **GET** /warehousetransfer/fbainbound/shippingplans/{shippingPlanId}/shipments/{shipmentId} | GetShipmentById
[**warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_approve_post**](FbaShipmentApi.md#warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_approve_post) | **POST** /warehousetransfer/fbainbound/shippingplans/{shippingPlanId}/shipments/approve | ApproveAllShipments
[**warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_get**](FbaShipmentApi.md#warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_get) | **GET** /warehousetransfer/fbainbound/shippingplans/{shippingPlanId}/shipments | GetShipmentsByShippingPlanId
[**warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_amazon_shipment_items_delete**](FbaShipmentApi.md#warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_amazon_shipment_items_delete) | **DELETE** /warehousetransfer/fbainbound/shippingplans/{shippingPlanId}/shipments/{shipmentId}/amazon-shipment-items | DeleteAmazonShipmentItem
[**warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_approve_post**](FbaShipmentApi.md#warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_approve_post) | **POST** /warehousetransfer/fbainbound/shippingplans/{shippingPlanId}/shipments/{shipmentId}/approve | ApproveShipment
[**warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_inbound_put**](FbaShipmentApi.md#warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_inbound_put) | **PUT** /warehousetransfer/fbainbound/shippingplans/{shippingPlanId}/shipments/{shipmentId}/inbound | UpdateInboundShipment
[**warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_name_put**](FbaShipmentApi.md#warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_name_put) | **PUT** /warehousetransfer/fbainbound/shippingplans/{shippingPlanId}/shipments/{shipmentId}/name | UpdateShipmentName
[**warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_put**](FbaShipmentApi.md#warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_put) | **PUT** /warehousetransfer/fbainbound/shippingplans/{shippingPlanId}/shipments/{shipmentId} | UpdateShipment
[**warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_ship_post**](FbaShipmentApi.md#warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_ship_post) | **POST** /warehousetransfer/fbainbound/shippingplans/{shippingPlanId}/shipments/{shipmentId}/ship | ShipShipment
[**warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_void_delete**](FbaShipmentApi.md#warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_void_delete) | **DELETE** /warehousetransfer/fbainbound/shippingplans/{shippingPlanId}/shipments/{shipmentId}/void | VoidShipment
[**warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_withshipmentitems_get**](FbaShipmentApi.md#warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_withshipmentitems_get) | **GET** /warehousetransfer/fbainbound/shippingplans/{shippingPlanId}/shipments/withshipmentitems | GetShipmentsWithItemsByShippingPlanId


# **get_shipment_by_id**
> ShipmentResponse get_shipment_by_id(shipment_id, shipping_plan_id)

GetShipmentById

Used to get shipment by id<br>Deprecated - please use v2 - [API Docs v2](https://apidocs.linnworks.net/v2/)

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.shipment_response import ShipmentResponse
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
    api_instance = linnworks_api.generated.warehousetransfer_new.FbaShipmentApi(api_client)
    shipment_id = 56 # int | 
    shipping_plan_id = 'shipping_plan_id_example' # str | 

    try:
        # GetShipmentById
        api_response = api_instance.get_shipment_by_id(shipment_id, shipping_plan_id)
        print("The response of FbaShipmentApi->get_shipment_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FbaShipmentApi->get_shipment_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **int**|  | 
 **shipping_plan_id** | **str**|  | 

### Return type

[**ShipmentResponse**](ShipmentResponse.md)

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

# **warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_approve_post**
> List[ApproveShipmentResponse] warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_approve_post(shipping_plan_id)

ApproveAllShipments

Approves all shipments<br>Deprecated - please use v2 - [API Docs v2](https://apidocs.linnworks.net/v2/)

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.approve_shipment_response import ApproveShipmentResponse
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
    api_instance = linnworks_api.generated.warehousetransfer_new.FbaShipmentApi(api_client)
    shipping_plan_id = 56 # int | 

    try:
        # ApproveAllShipments
        api_response = api_instance.warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_approve_post(shipping_plan_id)
        print("The response of FbaShipmentApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_approve_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FbaShipmentApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_approve_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_plan_id** | **int**|  | 

### Return type

[**List[ApproveShipmentResponse]**](ApproveShipmentResponse.md)

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

# **warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_get**
> List[ShipmentResponse] warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_get(shipping_plan_id)

GetShipmentsByShippingPlanId

Deprecated - please use v2 - [API Docs v2](https://apidocs.linnworks.net/v2/)

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.shipment_response import ShipmentResponse
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
    api_instance = linnworks_api.generated.warehousetransfer_new.FbaShipmentApi(api_client)
    shipping_plan_id = 56 # int | 

    try:
        # GetShipmentsByShippingPlanId
        api_response = api_instance.warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_get(shipping_plan_id)
        print("The response of FbaShipmentApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FbaShipmentApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_plan_id** | **int**|  | 

### Return type

[**List[ShipmentResponse]**](ShipmentResponse.md)

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

# **warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_amazon_shipment_items_delete**
> warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_amazon_shipment_items_delete(shipping_plan_id, shipment_id, shipment_item_id=shipment_item_id)

DeleteAmazonShipmentItem

Used to delete shipment items in batch on amazon and in db<br>Deprecated - please use v2 - [API Docs v2](https://apidocs.linnworks.net/v2/)

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
    api_instance = linnworks_api.generated.warehousetransfer_new.FbaShipmentApi(api_client)
    shipping_plan_id = 56 # int | 
    shipment_id = 56 # int | 
    shipment_item_id = [56] # List[int] |  (optional)

    try:
        # DeleteAmazonShipmentItem
        api_instance.warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_amazon_shipment_items_delete(shipping_plan_id, shipment_id, shipment_item_id=shipment_item_id)
    except Exception as e:
        print("Exception when calling FbaShipmentApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_amazon_shipment_items_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_plan_id** | **int**|  | 
 **shipment_id** | **int**|  | 
 **shipment_item_id** | [**List[int]**](int.md)|  | [optional] 

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

# **warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_approve_post**
> ApproveShipmentResponse warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_approve_post(shipping_plan_id, shipment_id)

ApproveShipment

Used to approve shipment<br>Deprecated - please use v2 - [API Docs v2](https://apidocs.linnworks.net/v2/)

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.approve_shipment_response import ApproveShipmentResponse
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
    api_instance = linnworks_api.generated.warehousetransfer_new.FbaShipmentApi(api_client)
    shipping_plan_id = 56 # int | 
    shipment_id = 56 # int | 

    try:
        # ApproveShipment
        api_response = api_instance.warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_approve_post(shipping_plan_id, shipment_id)
        print("The response of FbaShipmentApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_approve_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FbaShipmentApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_approve_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_plan_id** | **int**|  | 
 **shipment_id** | **int**|  | 

### Return type

[**ApproveShipmentResponse**](ApproveShipmentResponse.md)

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

# **warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_inbound_put**
> warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_inbound_put(shipping_plan_id, shipment_id)

UpdateInboundShipment

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
    api_instance = linnworks_api.generated.warehousetransfer_new.FbaShipmentApi(api_client)
    shipping_plan_id = 56 # int | 
    shipment_id = 56 # int | 

    try:
        # UpdateInboundShipment
        api_instance.warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_inbound_put(shipping_plan_id, shipment_id)
    except Exception as e:
        print("Exception when calling FbaShipmentApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_inbound_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_plan_id** | **int**|  | 
 **shipment_id** | **int**|  | 

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

# **warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_name_put**
> warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_name_put(shipping_plan_id, shipment_id, update_shipment_name_request=update_shipment_name_request)

UpdateShipmentName

Deprecated - please use v2 - [API Docs v2](https://apidocs.linnworks.net/v2/)

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.update_shipment_name_request import UpdateShipmentNameRequest
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
    api_instance = linnworks_api.generated.warehousetransfer_new.FbaShipmentApi(api_client)
    shipping_plan_id = 56 # int | 
    shipment_id = 56 # int | 
    update_shipment_name_request = linnworks_api.generated.warehousetransfer_new.UpdateShipmentNameRequest() # UpdateShipmentNameRequest |  (optional)

    try:
        # UpdateShipmentName
        api_instance.warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_name_put(shipping_plan_id, shipment_id, update_shipment_name_request=update_shipment_name_request)
    except Exception as e:
        print("Exception when calling FbaShipmentApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_name_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_plan_id** | **int**|  | 
 **shipment_id** | **int**|  | 
 **update_shipment_name_request** | [**UpdateShipmentNameRequest**](UpdateShipmentNameRequest.md)|  | [optional] 

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

# **warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_put**
> warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_put(shipping_plan_id, shipment_id, update_shipment_request=update_shipment_request)

UpdateShipment

Used to update shipment<br>Deprecated - please use v2 - [API Docs v2](https://apidocs.linnworks.net/v2/)

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.update_shipment_request import UpdateShipmentRequest
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
    api_instance = linnworks_api.generated.warehousetransfer_new.FbaShipmentApi(api_client)
    shipping_plan_id = 56 # int | 
    shipment_id = 56 # int | 
    update_shipment_request = linnworks_api.generated.warehousetransfer_new.UpdateShipmentRequest() # UpdateShipmentRequest |  (optional)

    try:
        # UpdateShipment
        api_instance.warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_put(shipping_plan_id, shipment_id, update_shipment_request=update_shipment_request)
    except Exception as e:
        print("Exception when calling FbaShipmentApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_plan_id** | **int**|  | 
 **shipment_id** | **int**|  | 
 **update_shipment_request** | [**UpdateShipmentRequest**](UpdateShipmentRequest.md)|  | [optional] 

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

# **warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_ship_post**
> warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_ship_post(shipping_plan_id, shipment_id)

ShipShipment

Used to mark as shipped<br>Deprecated - please use v2 - [API Docs v2](https://apidocs.linnworks.net/v2/)

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
    api_instance = linnworks_api.generated.warehousetransfer_new.FbaShipmentApi(api_client)
    shipping_plan_id = 56 # int | 
    shipment_id = 56 # int | 

    try:
        # ShipShipment
        api_instance.warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_ship_post(shipping_plan_id, shipment_id)
    except Exception as e:
        print("Exception when calling FbaShipmentApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_ship_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_plan_id** | **int**|  | 
 **shipment_id** | **int**|  | 

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

# **warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_void_delete**
> warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_void_delete(shipment_id, shipping_plan_id)

VoidShipment

Used to void shipment<br>Deprecated - please use v2 - [API Docs v2](https://apidocs.linnworks.net/v2/)

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
    api_instance = linnworks_api.generated.warehousetransfer_new.FbaShipmentApi(api_client)
    shipment_id = 56 # int | 
    shipping_plan_id = 'shipping_plan_id_example' # str | 

    try:
        # VoidShipment
        api_instance.warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_void_delete(shipment_id, shipping_plan_id)
    except Exception as e:
        print("Exception when calling FbaShipmentApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_void_delete: %s\n" % e)
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

# **warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_withshipmentitems_get**
> List[ShipmentResponse] warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_withshipmentitems_get(shipping_plan_id)

GetShipmentsWithItemsByShippingPlanId

this method is used to get shipments for a specific shipping plan<br>Deprecated - please use v2 - [API Docs v2](https://apidocs.linnworks.net/v2/)

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.shipment_response import ShipmentResponse
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
    api_instance = linnworks_api.generated.warehousetransfer_new.FbaShipmentApi(api_client)
    shipping_plan_id = 56 # int | 

    try:
        # GetShipmentsWithItemsByShippingPlanId
        api_response = api_instance.warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_withshipmentitems_get(shipping_plan_id)
        print("The response of FbaShipmentApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_withshipmentitems_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FbaShipmentApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_withshipmentitems_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_plan_id** | **int**|  | 

### Return type

[**List[ShipmentResponse]**](ShipmentResponse.md)

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

