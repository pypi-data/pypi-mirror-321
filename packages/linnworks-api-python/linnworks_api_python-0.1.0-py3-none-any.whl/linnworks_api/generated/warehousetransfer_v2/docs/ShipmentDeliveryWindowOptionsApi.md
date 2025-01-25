# linnworks_api.generated.warehousetransfer_v2.ShipmentDeliveryWindowOptionsApi

All URIs are relative to *https://eu-api.linnworks.net/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_shipment_id_delivery_window_options_delivery_window_option_id_confirm_post**](ShipmentDeliveryWindowOptionsApi.md#warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_shipment_id_delivery_window_options_delivery_window_option_id_confirm_post) | **POST** /warehousetransfer/fba-inbound/shipping-plans/{shippingPlanId}/shipments/{shipmentId}/delivery-window-options/{deliveryWindowOptionId}/confirm | ConfirmDeliveryWindowOptions
[**warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_shipment_id_delivery_window_options_generate_post**](ShipmentDeliveryWindowOptionsApi.md#warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_shipment_id_delivery_window_options_generate_post) | **POST** /warehousetransfer/fba-inbound/shipping-plans/{shippingPlanId}/shipments/{shipmentId}/delivery-window-options/generate | GenerateDeliveryWindowOptions
[**warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_shipment_id_delivery_window_options_get**](ShipmentDeliveryWindowOptionsApi.md#warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_shipment_id_delivery_window_options_get) | **GET** /warehousetransfer/fba-inbound/shipping-plans/{shippingPlanId}/shipments/{shipmentId}/delivery-window-options | ListDeliveryWindowOptions


# **warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_shipment_id_delivery_window_options_delivery_window_option_id_confirm_post**
> OperationModel warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_shipment_id_delivery_window_options_delivery_window_option_id_confirm_post(shipping_plan_id, shipment_id, delivery_window_option_id)

ConfirmDeliveryWindowOptions

Confirms the delivery window option for chosen shipment within an inbound plan

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
    api_instance = linnworks_api.generated.warehousetransfer_v2.ShipmentDeliveryWindowOptionsApi(api_client)
    shipping_plan_id = 56 # int | 
    shipment_id = 56 # int | 
    delivery_window_option_id = 'delivery_window_option_id_example' # str | 

    try:
        # ConfirmDeliveryWindowOptions
        api_response = api_instance.warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_shipment_id_delivery_window_options_delivery_window_option_id_confirm_post(shipping_plan_id, shipment_id, delivery_window_option_id)
        print("The response of ShipmentDeliveryWindowOptionsApi->warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_shipment_id_delivery_window_options_delivery_window_option_id_confirm_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentDeliveryWindowOptionsApi->warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_shipment_id_delivery_window_options_delivery_window_option_id_confirm_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_plan_id** | **int**|  | 
 **shipment_id** | **int**|  | 
 **delivery_window_option_id** | **str**|  | 

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
**204** | Success |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_shipment_id_delivery_window_options_generate_post**
> OperationModel warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_shipment_id_delivery_window_options_generate_post(shipping_plan_id, shipment_id)

GenerateDeliveryWindowOptions

Generates available delivery window options for a given shipment

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
    api_instance = linnworks_api.generated.warehousetransfer_v2.ShipmentDeliveryWindowOptionsApi(api_client)
    shipping_plan_id = 56 # int | 
    shipment_id = 56 # int | 

    try:
        # GenerateDeliveryWindowOptions
        api_response = api_instance.warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_shipment_id_delivery_window_options_generate_post(shipping_plan_id, shipment_id)
        print("The response of ShipmentDeliveryWindowOptionsApi->warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_shipment_id_delivery_window_options_generate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentDeliveryWindowOptionsApi->warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_shipment_id_delivery_window_options_generate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_plan_id** | **int**|  | 
 **shipment_id** | **int**|  | 

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
**204** | Success |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_shipment_id_delivery_window_options_get**
> List[ListDeliveryWindowOptionResponse] warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_shipment_id_delivery_window_options_get(shipping_plan_id, shipment_id)

ListDeliveryWindowOptions

Retrieves all delivery window options for a shipment

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_v2
from linnworks_api.generated.warehousetransfer_v2.models.list_delivery_window_option_response import ListDeliveryWindowOptionResponse
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
    api_instance = linnworks_api.generated.warehousetransfer_v2.ShipmentDeliveryWindowOptionsApi(api_client)
    shipping_plan_id = 56 # int | 
    shipment_id = 56 # int | 

    try:
        # ListDeliveryWindowOptions
        api_response = api_instance.warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_shipment_id_delivery_window_options_get(shipping_plan_id, shipment_id)
        print("The response of ShipmentDeliveryWindowOptionsApi->warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_shipment_id_delivery_window_options_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentDeliveryWindowOptionsApi->warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_shipment_id_delivery_window_options_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_plan_id** | **int**|  | 
 **shipment_id** | **int**|  | 

### Return type

[**List[ListDeliveryWindowOptionResponse]**](ListDeliveryWindowOptionResponse.md)

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

