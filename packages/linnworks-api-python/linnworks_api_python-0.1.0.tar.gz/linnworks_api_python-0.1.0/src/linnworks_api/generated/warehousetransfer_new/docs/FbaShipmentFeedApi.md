# linnworks_api.generated.warehousetransfer_new.FbaShipmentFeedApi

All URIs are relative to *https://eu-api.linnworks.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_feeds_error_message_get**](FbaShipmentFeedApi.md#warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_feeds_error_message_get) | **GET** /warehousetransfer/fbainbound/shippingplans/{shippingPlanId}/shipments/{shipmentId}/feeds/error-message | GetCartonInformationFeedError
[**warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_feeds_put**](FbaShipmentFeedApi.md#warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_feeds_put) | **PUT** /warehousetransfer/fbainbound/shippingplans/{shippingPlanId}/shipments/{shipmentId}/feeds | SubmitCartonInformationFeed


# **warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_feeds_error_message_get**
> GetCartonInformationFeedErrorResponse warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_feeds_error_message_get(shipment_id, shipping_plan_id)

GetCartonInformationFeedError

Deprecated - please use v2 - [API Docs v2](https://apidocs.linnworks.net/v2/)

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.get_carton_information_feed_error_response import GetCartonInformationFeedErrorResponse
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
    api_instance = linnworks_api.generated.warehousetransfer_new.FbaShipmentFeedApi(api_client)
    shipment_id = 56 # int | 
    shipping_plan_id = 'shipping_plan_id_example' # str | 

    try:
        # GetCartonInformationFeedError
        api_response = api_instance.warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_feeds_error_message_get(shipment_id, shipping_plan_id)
        print("The response of FbaShipmentFeedApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_feeds_error_message_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FbaShipmentFeedApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_feeds_error_message_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **int**|  | 
 **shipping_plan_id** | **str**|  | 

### Return type

[**GetCartonInformationFeedErrorResponse**](GetCartonInformationFeedErrorResponse.md)

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

# **warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_feeds_put**
> warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_feeds_put(shipping_plan_id, shipment_id)

SubmitCartonInformationFeed

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
    api_instance = linnworks_api.generated.warehousetransfer_new.FbaShipmentFeedApi(api_client)
    shipping_plan_id = 56 # int | 
    shipment_id = 56 # int | 

    try:
        # SubmitCartonInformationFeed
        api_instance.warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_feeds_put(shipping_plan_id, shipment_id)
    except Exception as e:
        print("Exception when calling FbaShipmentFeedApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_feeds_put: %s\n" % e)
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

