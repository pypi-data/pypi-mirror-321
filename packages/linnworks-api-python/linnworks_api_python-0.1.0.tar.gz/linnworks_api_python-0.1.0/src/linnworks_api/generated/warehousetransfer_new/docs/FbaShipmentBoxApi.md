# linnworks_api.generated.warehousetransfer_new.FbaShipmentBoxApi

All URIs are relative to *https://eu-api.linnworks.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxes_get**](FbaShipmentBoxApi.md#warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxes_get) | **GET** /warehousetransfer/fbainbound/shippingplans/{shippingPlanId}/shipments/{shipmentId}/boxes | Get
[**warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxes_pallets_put**](FbaShipmentBoxApi.md#warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxes_pallets_put) | **PUT** /warehousetransfer/fbainbound/shippingplans/{shippingPlanId}/shipments/{shipmentId}/boxes/pallets | UpdateShipmentBoxPallets
[**warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxes_post**](FbaShipmentBoxApi.md#warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxes_post) | **POST** /warehousetransfer/fbainbound/shippingplans/{shippingPlanId}/shipments/{shipmentId}/boxes | Add
[**warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxes_put**](FbaShipmentBoxApi.md#warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxes_put) | **PUT** /warehousetransfer/fbainbound/shippingplans/{shippingPlanId}/shipments/{shipmentId}/boxes | Update
[**warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxes_shipment_box_id_delete**](FbaShipmentBoxApi.md#warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxes_shipment_box_id_delete) | **DELETE** /warehousetransfer/fbainbound/shippingplans/{shippingPlanId}/shipments/{shipmentId}/boxes/{shipmentBoxId} | Delete


# **warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxes_get**
> GetShipmentBoxesResponse warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxes_get(shipment_id, shipping_plan_id)

Get

Deprecated - please use v2 - [API Docs v2](https://apidocs.linnworks.net/v2/)

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.get_shipment_boxes_response import GetShipmentBoxesResponse
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
    api_instance = linnworks_api.generated.warehousetransfer_new.FbaShipmentBoxApi(api_client)
    shipment_id = 56 # int | 
    shipping_plan_id = 'shipping_plan_id_example' # str | 

    try:
        # Get
        api_response = api_instance.warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxes_get(shipment_id, shipping_plan_id)
        print("The response of FbaShipmentBoxApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FbaShipmentBoxApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **int**|  | 
 **shipping_plan_id** | **str**|  | 

### Return type

[**GetShipmentBoxesResponse**](GetShipmentBoxesResponse.md)

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

# **warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxes_pallets_put**
> int warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxes_pallets_put(shipping_plan_id, shipment_id, update_shipment_box_pallets_request=update_shipment_box_pallets_request)

UpdateShipmentBoxPallets

Deprecated - please use v2 - [API Docs v2](https://apidocs.linnworks.net/v2/)

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.update_shipment_box_pallets_request import UpdateShipmentBoxPalletsRequest
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
    api_instance = linnworks_api.generated.warehousetransfer_new.FbaShipmentBoxApi(api_client)
    shipping_plan_id = 'shipping_plan_id_example' # str | 
    shipment_id = 'shipment_id_example' # str | 
    update_shipment_box_pallets_request = linnworks_api.generated.warehousetransfer_new.UpdateShipmentBoxPalletsRequest() # UpdateShipmentBoxPalletsRequest |  (optional)

    try:
        # UpdateShipmentBoxPallets
        api_response = api_instance.warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxes_pallets_put(shipping_plan_id, shipment_id, update_shipment_box_pallets_request=update_shipment_box_pallets_request)
        print("The response of FbaShipmentBoxApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxes_pallets_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FbaShipmentBoxApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxes_pallets_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_plan_id** | **str**|  | 
 **shipment_id** | **str**|  | 
 **update_shipment_box_pallets_request** | [**UpdateShipmentBoxPalletsRequest**](UpdateShipmentBoxPalletsRequest.md)|  | [optional] 

### Return type

**int**

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

# **warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxes_post**
> List[AddShipmentBoxesResponse] warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxes_post(shipment_id, shipping_plan_id, add_shipment_boxes_request=add_shipment_boxes_request)

Add

Deprecated - please use v2 - [API Docs v2](https://apidocs.linnworks.net/v2/)

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.add_shipment_boxes_request import AddShipmentBoxesRequest
from linnworks_api.generated.warehousetransfer_new.models.add_shipment_boxes_response import AddShipmentBoxesResponse
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
    api_instance = linnworks_api.generated.warehousetransfer_new.FbaShipmentBoxApi(api_client)
    shipment_id = 56 # int | 
    shipping_plan_id = 56 # int | 
    add_shipment_boxes_request = linnworks_api.generated.warehousetransfer_new.AddShipmentBoxesRequest() # AddShipmentBoxesRequest |  (optional)

    try:
        # Add
        api_response = api_instance.warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxes_post(shipment_id, shipping_plan_id, add_shipment_boxes_request=add_shipment_boxes_request)
        print("The response of FbaShipmentBoxApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FbaShipmentBoxApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **int**|  | 
 **shipping_plan_id** | **int**|  | 
 **add_shipment_boxes_request** | [**AddShipmentBoxesRequest**](AddShipmentBoxesRequest.md)|  | [optional] 

### Return type

[**List[AddShipmentBoxesResponse]**](AddShipmentBoxesResponse.md)

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

# **warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxes_put**
> bool warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxes_put(shipment_id, shipping_plan_id, update_shipment_box_request=update_shipment_box_request)

Update

Deprecated - please use v2 - [API Docs v2](https://apidocs.linnworks.net/v2/)

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.update_shipment_box_request import UpdateShipmentBoxRequest
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
    api_instance = linnworks_api.generated.warehousetransfer_new.FbaShipmentBoxApi(api_client)
    shipment_id = 56 # int | 
    shipping_plan_id = 56 # int | 
    update_shipment_box_request = linnworks_api.generated.warehousetransfer_new.UpdateShipmentBoxRequest() # UpdateShipmentBoxRequest |  (optional)

    try:
        # Update
        api_response = api_instance.warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxes_put(shipment_id, shipping_plan_id, update_shipment_box_request=update_shipment_box_request)
        print("The response of FbaShipmentBoxApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxes_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FbaShipmentBoxApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxes_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **int**|  | 
 **shipping_plan_id** | **int**|  | 
 **update_shipment_box_request** | [**UpdateShipmentBoxRequest**](UpdateShipmentBoxRequest.md)|  | [optional] 

### Return type

**bool**

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

# **warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxes_shipment_box_id_delete**
> int warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxes_shipment_box_id_delete(shipment_id, shipping_plan_id, shipment_box_id)

Delete

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
    api_instance = linnworks_api.generated.warehousetransfer_new.FbaShipmentBoxApi(api_client)
    shipment_id = 56 # int | 
    shipping_plan_id = 56 # int | 
    shipment_box_id = 56 # int | 

    try:
        # Delete
        api_response = api_instance.warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxes_shipment_box_id_delete(shipment_id, shipping_plan_id, shipment_box_id)
        print("The response of FbaShipmentBoxApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxes_shipment_box_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FbaShipmentBoxApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxes_shipment_box_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **int**|  | 
 **shipping_plan_id** | **int**|  | 
 **shipment_box_id** | **int**|  | 

### Return type

**int**

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

