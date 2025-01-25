# linnworks_api.generated.warehousetransfer_v2.ShippingPlanApi

All URIs are relative to *https://eu-api.linnworks.net/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_fba_shipping_plan_by_id**](ShippingPlanApi.md#get_fba_shipping_plan_by_id) | **GET** /warehousetransfer/fba-inbound/shipping-plans/{shippingPlanId} | GetFbaShippingPlanById
[**warehousetransfer_fba_inbound_shipping_plans_post**](ShippingPlanApi.md#warehousetransfer_fba_inbound_shipping_plans_post) | **POST** /warehousetransfer/fba-inbound/shipping-plans | CreateShippingPlan
[**warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_delete**](ShippingPlanApi.md#warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_delete) | **DELETE** /warehousetransfer/fba-inbound/shipping-plans/{shippingPlanId} | DeleteShippingPlan
[**warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_packing_information_post**](ShippingPlanApi.md#warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_packing_information_post) | **POST** /warehousetransfer/fba-inbound/shipping-plans/{shippingPlanId}/packing-information | SetPackingInformation
[**warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_put**](ShippingPlanApi.md#warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_put) | **PUT** /warehousetransfer/fba-inbound/shipping-plans/{shippingPlanId} | UpdateShippingPlan
[**warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_submit_put**](ShippingPlanApi.md#warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_submit_put) | **PUT** /warehousetransfer/fba-inbound/shipping-plans/{shippingPlanId}/submit | SubmitShippingPlan


# **get_fba_shipping_plan_by_id**
> GetShippingPlanByIdResponse get_fba_shipping_plan_by_id(shipping_plan_id)

GetFbaShippingPlanById

Used to get shipping plan with shipments and shipping items

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_v2
from linnworks_api.generated.warehousetransfer_v2.models.get_shipping_plan_by_id_response import GetShippingPlanByIdResponse
from linnworks_api.generated.warehousetransfer_v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-api.linnworks.net/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.warehousetransfer_v2.Configuration(
    host = "https://eu-api.linnworks.net/v2"
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
with linnworks_api.generated.warehousetransfer_v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.warehousetransfer_v2.ShippingPlanApi(api_client)
    shipping_plan_id = 56 # int | 

    try:
        # GetFbaShippingPlanById
        api_response = api_instance.get_fba_shipping_plan_by_id(shipping_plan_id)
        print("The response of ShippingPlanApi->get_fba_shipping_plan_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingPlanApi->get_fba_shipping_plan_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_plan_id** | **int**|  | 

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
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehousetransfer_fba_inbound_shipping_plans_post**
> warehousetransfer_fba_inbound_shipping_plans_post(create_shippping_plan_request)

CreateShippingPlan

Used to create shipping plan with default shipment

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_v2
from linnworks_api.generated.warehousetransfer_v2.models.create_shippping_plan_request import CreateShipppingPlanRequest
from linnworks_api.generated.warehousetransfer_v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-api.linnworks.net/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.warehousetransfer_v2.Configuration(
    host = "https://eu-api.linnworks.net/v2"
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
with linnworks_api.generated.warehousetransfer_v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.warehousetransfer_v2.ShippingPlanApi(api_client)
    create_shippping_plan_request = linnworks_api.generated.warehousetransfer_v2.CreateShipppingPlanRequest() # CreateShipppingPlanRequest | 

    try:
        # CreateShippingPlan
        api_instance.warehousetransfer_fba_inbound_shipping_plans_post(create_shippping_plan_request)
    except Exception as e:
        print("Exception when calling ShippingPlanApi->warehousetransfer_fba_inbound_shipping_plans_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_shippping_plan_request** | [**CreateShipppingPlanRequest**](CreateShipppingPlanRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[Linnworks](../README.md#Linnworks)

### HTTP request headers

 - **Content-Type**: application/json-patch+json; x-api-version=2.0, application/json; x-api-version=2.0, text/json; x-api-version=2.0, application/*+json; x-api-version=2.0
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**201** | Success |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_delete**
> warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_delete(shipping_plan_id)

DeleteShippingPlan

Used to delete just shipping plan without related info

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_v2
from linnworks_api.generated.warehousetransfer_v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-api.linnworks.net/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.warehousetransfer_v2.Configuration(
    host = "https://eu-api.linnworks.net/v2"
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
with linnworks_api.generated.warehousetransfer_v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.warehousetransfer_v2.ShippingPlanApi(api_client)
    shipping_plan_id = 56 # int | 

    try:
        # DeleteShippingPlan
        api_instance.warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_delete(shipping_plan_id)
    except Exception as e:
        print("Exception when calling ShippingPlanApi->warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_plan_id** | **int**|  | 

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
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**204** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_packing_information_post**
> OperationModel warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_packing_information_post(shipping_plan_id)

SetPackingInformation

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_v2
from linnworks_api.generated.warehousetransfer_v2.models.operation_model import OperationModel
from linnworks_api.generated.warehousetransfer_v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-api.linnworks.net/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.warehousetransfer_v2.Configuration(
    host = "https://eu-api.linnworks.net/v2"
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
with linnworks_api.generated.warehousetransfer_v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.warehousetransfer_v2.ShippingPlanApi(api_client)
    shipping_plan_id = 56 # int | 

    try:
        # SetPackingInformation
        api_response = api_instance.warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_packing_information_post(shipping_plan_id)
        print("The response of ShippingPlanApi->warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_packing_information_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingPlanApi->warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_packing_information_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_plan_id** | **int**|  | 

### Return type

[**OperationModel**](OperationModel.md)

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
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_put**
> GetShippingPlanCardsResponse warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_put(shipping_plan_id, update_shipping_plan_request_input)

UpdateShippingPlan

Used to update shipping plan

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_v2
from linnworks_api.generated.warehousetransfer_v2.models.get_shipping_plan_cards_response import GetShippingPlanCardsResponse
from linnworks_api.generated.warehousetransfer_v2.models.update_shipping_plan_request_input import UpdateShippingPlanRequestInput
from linnworks_api.generated.warehousetransfer_v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-api.linnworks.net/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.warehousetransfer_v2.Configuration(
    host = "https://eu-api.linnworks.net/v2"
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
with linnworks_api.generated.warehousetransfer_v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.warehousetransfer_v2.ShippingPlanApi(api_client)
    shipping_plan_id = 56 # int | 
    update_shipping_plan_request_input = linnworks_api.generated.warehousetransfer_v2.UpdateShippingPlanRequestInput() # UpdateShippingPlanRequestInput | 

    try:
        # UpdateShippingPlan
        api_response = api_instance.warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_put(shipping_plan_id, update_shipping_plan_request_input)
        print("The response of ShippingPlanApi->warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingPlanApi->warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_plan_id** | **int**|  | 
 **update_shipping_plan_request_input** | [**UpdateShippingPlanRequestInput**](UpdateShippingPlanRequestInput.md)|  | 

### Return type

[**GetShippingPlanCardsResponse**](GetShippingPlanCardsResponse.md)

### Authorization

[Linnworks](../README.md#Linnworks)

### HTTP request headers

 - **Content-Type**: application/json-patch+json; x-api-version=2.0, application/json; x-api-version=2.0, text/json; x-api-version=2.0, application/*+json; x-api-version=2.0
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**201** | Success |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_submit_put**
> GetShippingPlanCardsResponse warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_submit_put(shipping_plan_id)

SubmitShippingPlan

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_v2
from linnworks_api.generated.warehousetransfer_v2.models.get_shipping_plan_cards_response import GetShippingPlanCardsResponse
from linnworks_api.generated.warehousetransfer_v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-api.linnworks.net/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.warehousetransfer_v2.Configuration(
    host = "https://eu-api.linnworks.net/v2"
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
with linnworks_api.generated.warehousetransfer_v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.warehousetransfer_v2.ShippingPlanApi(api_client)
    shipping_plan_id = 56 # int | 

    try:
        # SubmitShippingPlan
        api_response = api_instance.warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_submit_put(shipping_plan_id)
        print("The response of ShippingPlanApi->warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_submit_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingPlanApi->warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_submit_put: %s\n" % e)
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
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

