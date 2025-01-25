# linnworks_api.generated.warehousetransfer_new.FbaShippingPlanApi

All URIs are relative to *https://eu-api.linnworks.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_shipping_plan_by_id**](FbaShippingPlanApi.md#get_shipping_plan_by_id) | **GET** /warehousetransfer/fbainbound/shippingplans/{id} | GetShippingPlanById
[**warehousetransfer_fbainbound_shippingplans_id_delete**](FbaShippingPlanApi.md#warehousetransfer_fbainbound_shippingplans_id_delete) | **DELETE** /warehousetransfer/fbainbound/shippingplans/{id} | DeleteShippingPlan
[**warehousetransfer_fbainbound_shippingplans_id_put**](FbaShippingPlanApi.md#warehousetransfer_fbainbound_shippingplans_id_put) | **PUT** /warehousetransfer/fbainbound/shippingplans/{id} | UpdateShippingPlan
[**warehousetransfer_fbainbound_shippingplans_post**](FbaShippingPlanApi.md#warehousetransfer_fbainbound_shippingplans_post) | **POST** /warehousetransfer/fbainbound/shippingplans | CreateShippingPlan
[**warehousetransfer_fbainbound_shippingplans_shipping_plan_id_from_location_put**](FbaShippingPlanApi.md#warehousetransfer_fbainbound_shippingplans_shipping_plan_id_from_location_put) | **PUT** /warehousetransfer/fbainbound/shippingplans/{shippingPlanId}/from-location | UpdateFromLocation
[**warehousetransfer_fbainbound_shippingplans_shipping_plan_id_packing_type_put**](FbaShippingPlanApi.md#warehousetransfer_fbainbound_shippingplans_shipping_plan_id_packing_type_put) | **PUT** /warehousetransfer/fbainbound/shippingplans/{shippingPlanId}/packing-type | UpdatePackingType
[**warehousetransfer_fbainbound_shippingplans_shipping_plan_id_sellercentralurl_get**](FbaShippingPlanApi.md#warehousetransfer_fbainbound_shippingplans_shipping_plan_id_sellercentralurl_get) | **GET** /warehousetransfer/fbainbound/shippingplans/{shippingPlanId}/sellercentralurl | GetSellerCentralUrl
[**warehousetransfer_fbainbound_shippingplans_shipping_plan_id_submit_put**](FbaShippingPlanApi.md#warehousetransfer_fbainbound_shippingplans_shipping_plan_id_submit_put) | **PUT** /warehousetransfer/fbainbound/shippingplans/{shippingPlanId}/submit | SubmitShippingPlan
[**warehousetransfer_fbainbound_shippingplans_shipping_plan_id_to_location_put**](FbaShippingPlanApi.md#warehousetransfer_fbainbound_shippingplans_shipping_plan_id_to_location_put) | **PUT** /warehousetransfer/fbainbound/shippingplans/{shippingPlanId}/to-location | UpdateToLocation
[**warehousetransfer_fbainbound_shippingplans_shipping_plan_id_topleveldomain_get**](FbaShippingPlanApi.md#warehousetransfer_fbainbound_shippingplans_shipping_plan_id_topleveldomain_get) | **GET** /warehousetransfer/fbainbound/shippingplans/{shippingPlanId}/topleveldomain | GetAmazonTopLevelDomain


# **get_shipping_plan_by_id**
> GetShippingPlanByIdResponse get_shipping_plan_by_id(id)

GetShippingPlanById

Used to get shipping plan with shipments and shipping items<br>Deprecated - please use v2 - [API Docs v2](https://apidocs.linnworks.net/v2/)

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.get_shipping_plan_by_id_response import GetShippingPlanByIdResponse
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
    api_instance = linnworks_api.generated.warehousetransfer_new.FbaShippingPlanApi(api_client)
    id = 56 # int | 

    try:
        # GetShippingPlanById
        api_response = api_instance.get_shipping_plan_by_id(id)
        print("The response of FbaShippingPlanApi->get_shipping_plan_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FbaShippingPlanApi->get_shipping_plan_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**GetShippingPlanByIdResponse**](GetShippingPlanByIdResponse.md)

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

# **warehousetransfer_fbainbound_shippingplans_id_delete**
> warehousetransfer_fbainbound_shippingplans_id_delete(id)

DeleteShippingPlan

Used to delete just shipping plan without related info<br>Deprecated - please use v2 - [API Docs v2](https://apidocs.linnworks.net/v2/)

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
    api_instance = linnworks_api.generated.warehousetransfer_new.FbaShippingPlanApi(api_client)
    id = 56 # int | 

    try:
        # DeleteShippingPlan
        api_instance.warehousetransfer_fbainbound_shippingplans_id_delete(id)
    except Exception as e:
        print("Exception when calling FbaShippingPlanApi->warehousetransfer_fbainbound_shippingplans_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

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

# **warehousetransfer_fbainbound_shippingplans_id_put**
> warehousetransfer_fbainbound_shippingplans_id_put(id, update_shipping_plan_request=update_shipping_plan_request)

UpdateShippingPlan

Used to update shipping plan<br>Deprecated - please use v2 - [API Docs v2](https://apidocs.linnworks.net/v2/)

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.update_shipping_plan_request import UpdateShippingPlanRequest
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
    api_instance = linnworks_api.generated.warehousetransfer_new.FbaShippingPlanApi(api_client)
    id = 56 # int | 
    update_shipping_plan_request = linnworks_api.generated.warehousetransfer_new.UpdateShippingPlanRequest() # UpdateShippingPlanRequest |  (optional)

    try:
        # UpdateShippingPlan
        api_instance.warehousetransfer_fbainbound_shippingplans_id_put(id, update_shipping_plan_request=update_shipping_plan_request)
    except Exception as e:
        print("Exception when calling FbaShippingPlanApi->warehousetransfer_fbainbound_shippingplans_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **update_shipping_plan_request** | [**UpdateShippingPlanRequest**](UpdateShippingPlanRequest.md)|  | [optional] 

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

# **warehousetransfer_fbainbound_shippingplans_post**
> warehousetransfer_fbainbound_shippingplans_post(create_shipping_plan_request=create_shipping_plan_request)

CreateShippingPlan

Used to create shipping plan with default shipment<br>Deprecated - please use v2 - [API Docs v2](https://apidocs.linnworks.net/v2/)

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.create_shipping_plan_request import CreateShippingPlanRequest
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
    api_instance = linnworks_api.generated.warehousetransfer_new.FbaShippingPlanApi(api_client)
    create_shipping_plan_request = linnworks_api.generated.warehousetransfer_new.CreateShippingPlanRequest() # CreateShippingPlanRequest |  (optional)

    try:
        # CreateShippingPlan
        api_instance.warehousetransfer_fbainbound_shippingplans_post(create_shipping_plan_request=create_shipping_plan_request)
    except Exception as e:
        print("Exception when calling FbaShippingPlanApi->warehousetransfer_fbainbound_shippingplans_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_shipping_plan_request** | [**CreateShippingPlanRequest**](CreateShippingPlanRequest.md)|  | [optional] 

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

# **warehousetransfer_fbainbound_shippingplans_shipping_plan_id_from_location_put**
> warehousetransfer_fbainbound_shippingplans_shipping_plan_id_from_location_put(shipping_plan_id, update_from_location_fba_request=update_from_location_fba_request)

UpdateFromLocation

Deprecated - please use v2 - [API Docs v2](https://apidocs.linnworks.net/v2/)

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.update_from_location_fba_request import UpdateFromLocationFbaRequest
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
    api_instance = linnworks_api.generated.warehousetransfer_new.FbaShippingPlanApi(api_client)
    shipping_plan_id = 56 # int | 
    update_from_location_fba_request = linnworks_api.generated.warehousetransfer_new.UpdateFromLocationFbaRequest() # UpdateFromLocationFbaRequest |  (optional)

    try:
        # UpdateFromLocation
        api_instance.warehousetransfer_fbainbound_shippingplans_shipping_plan_id_from_location_put(shipping_plan_id, update_from_location_fba_request=update_from_location_fba_request)
    except Exception as e:
        print("Exception when calling FbaShippingPlanApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_from_location_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_plan_id** | **int**|  | 
 **update_from_location_fba_request** | [**UpdateFromLocationFbaRequest**](UpdateFromLocationFbaRequest.md)|  | [optional] 

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

# **warehousetransfer_fbainbound_shippingplans_shipping_plan_id_packing_type_put**
> warehousetransfer_fbainbound_shippingplans_shipping_plan_id_packing_type_put(shipping_plan_id, update_packing_type_request=update_packing_type_request)

UpdatePackingType

Deprecated - please use v2 - [API Docs v2](https://apidocs.linnworks.net/v2/)

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.update_packing_type_request import UpdatePackingTypeRequest
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
    api_instance = linnworks_api.generated.warehousetransfer_new.FbaShippingPlanApi(api_client)
    shipping_plan_id = 56 # int | 
    update_packing_type_request = linnworks_api.generated.warehousetransfer_new.UpdatePackingTypeRequest() # UpdatePackingTypeRequest |  (optional)

    try:
        # UpdatePackingType
        api_instance.warehousetransfer_fbainbound_shippingplans_shipping_plan_id_packing_type_put(shipping_plan_id, update_packing_type_request=update_packing_type_request)
    except Exception as e:
        print("Exception when calling FbaShippingPlanApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_packing_type_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_plan_id** | **int**|  | 
 **update_packing_type_request** | [**UpdatePackingTypeRequest**](UpdatePackingTypeRequest.md)|  | [optional] 

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

# **warehousetransfer_fbainbound_shippingplans_shipping_plan_id_sellercentralurl_get**
> str warehousetransfer_fbainbound_shippingplans_shipping_plan_id_sellercentralurl_get(shipping_plan_id)

GetSellerCentralUrl

Used to get seller central url from shipping plan<br>Deprecated - please use v2 - [API Docs v2](https://apidocs.linnworks.net/v2/)

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
    api_instance = linnworks_api.generated.warehousetransfer_new.FbaShippingPlanApi(api_client)
    shipping_plan_id = 56 # int | 

    try:
        # GetSellerCentralUrl
        api_response = api_instance.warehousetransfer_fbainbound_shippingplans_shipping_plan_id_sellercentralurl_get(shipping_plan_id)
        print("The response of FbaShippingPlanApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_sellercentralurl_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FbaShippingPlanApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_sellercentralurl_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_plan_id** | **int**|  | 

### Return type

**str**

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

# **warehousetransfer_fbainbound_shippingplans_shipping_plan_id_submit_put**
> GetShippingPlanCardsResponse warehousetransfer_fbainbound_shippingplans_shipping_plan_id_submit_put(shipping_plan_id)

SubmitShippingPlan

Used to update shipping plan items (sellerSku and quantity)<br>Deprecated - please use v2 - [API Docs v2](https://apidocs.linnworks.net/v2/)

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.get_shipping_plan_cards_response import GetShippingPlanCardsResponse
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
    api_instance = linnworks_api.generated.warehousetransfer_new.FbaShippingPlanApi(api_client)
    shipping_plan_id = 56 # int | 

    try:
        # SubmitShippingPlan
        api_response = api_instance.warehousetransfer_fbainbound_shippingplans_shipping_plan_id_submit_put(shipping_plan_id)
        print("The response of FbaShippingPlanApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_submit_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FbaShippingPlanApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_submit_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_plan_id** | **int**|  | 

### Return type

[**GetShippingPlanCardsResponse**](GetShippingPlanCardsResponse.md)

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

# **warehousetransfer_fbainbound_shippingplans_shipping_plan_id_to_location_put**
> UpdateToLocationResponse warehousetransfer_fbainbound_shippingplans_shipping_plan_id_to_location_put(shipping_plan_id, update_to_location_fba_request=update_to_location_fba_request)

UpdateToLocation

Deprecated - please use v2 - [API Docs v2](https://apidocs.linnworks.net/v2/)

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.update_to_location_fba_request import UpdateToLocationFbaRequest
from linnworks_api.generated.warehousetransfer_new.models.update_to_location_response import UpdateToLocationResponse
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
    api_instance = linnworks_api.generated.warehousetransfer_new.FbaShippingPlanApi(api_client)
    shipping_plan_id = 56 # int | 
    update_to_location_fba_request = linnworks_api.generated.warehousetransfer_new.UpdateToLocationFbaRequest() # UpdateToLocationFbaRequest |  (optional)

    try:
        # UpdateToLocation
        api_response = api_instance.warehousetransfer_fbainbound_shippingplans_shipping_plan_id_to_location_put(shipping_plan_id, update_to_location_fba_request=update_to_location_fba_request)
        print("The response of FbaShippingPlanApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_to_location_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FbaShippingPlanApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_to_location_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_plan_id** | **int**|  | 
 **update_to_location_fba_request** | [**UpdateToLocationFbaRequest**](UpdateToLocationFbaRequest.md)|  | [optional] 

### Return type

[**UpdateToLocationResponse**](UpdateToLocationResponse.md)

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

# **warehousetransfer_fbainbound_shippingplans_shipping_plan_id_topleveldomain_get**
> str warehousetransfer_fbainbound_shippingplans_shipping_plan_id_topleveldomain_get(shipping_plan_id)

GetAmazonTopLevelDomain

Used to get amazon top level domain from shipping plan<br>Deprecated - please use v2 - [API Docs v2](https://apidocs.linnworks.net/v2/)

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
    api_instance = linnworks_api.generated.warehousetransfer_new.FbaShippingPlanApi(api_client)
    shipping_plan_id = 56 # int | 

    try:
        # GetAmazonTopLevelDomain
        api_response = api_instance.warehousetransfer_fbainbound_shippingplans_shipping_plan_id_topleveldomain_get(shipping_plan_id)
        print("The response of FbaShippingPlanApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_topleveldomain_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FbaShippingPlanApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_topleveldomain_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_plan_id** | **int**|  | 

### Return type

**str**

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

