# linnworks_api.generated.warehousetransfer_v2.ShipmentsApi

All URIs are relative to *https://eu-api.linnworks.net/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_get**](ShipmentsApi.md#warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_get) | **GET** /warehousetransfer/fba-inbound/shipping-plans/{shippingPlanId}/shipments | GetShipmentsByShippingPlanId
[**warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_shipment_id_bill_of_lading_get**](ShipmentsApi.md#warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_shipment_id_bill_of_lading_get) | **GET** /warehousetransfer/fba-inbound/shipping-plans/{shippingPlanId}/shipments/{shipmentId}/bill-of-lading | GetBillOfLading
[**warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_shipment_id_get**](ShipmentsApi.md#warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_shipment_id_get) | **GET** /warehousetransfer/fba-inbound/shipping-plans/{shippingPlanId}/shipments/{shipmentId} | GetShipmentById
[**warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_shipment_id_labels_get**](ShipmentsApi.md#warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_shipment_id_labels_get) | **GET** /warehousetransfer/fba-inbound/shipping-plans/{shippingPlanId}/shipments/{shipmentId}/labels | GetLabelByShipmentId


# **warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_get**
> List[ShipmentResponse] warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_get(shipping_plan_id)

GetShipmentsByShippingPlanId

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_v2
from linnworks_api.generated.warehousetransfer_v2.models.shipment_response import ShipmentResponse
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
    api_instance = linnworks_api.generated.warehousetransfer_v2.ShipmentsApi(api_client)
    shipping_plan_id = 56 # int | 

    try:
        # GetShipmentsByShippingPlanId
        api_response = api_instance.warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_get(shipping_plan_id)
        print("The response of ShipmentsApi->warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentsApi->warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_get: %s\n" % e)
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
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Server Error |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_shipment_id_bill_of_lading_get**
> GetBillOfLadingByShipmentIdResponse warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_shipment_id_bill_of_lading_get(shipment_id, shipping_plan_id)

GetBillOfLading

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_v2
from linnworks_api.generated.warehousetransfer_v2.models.get_bill_of_lading_by_shipment_id_response import GetBillOfLadingByShipmentIdResponse
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
    api_instance = linnworks_api.generated.warehousetransfer_v2.ShipmentsApi(api_client)
    shipment_id = 56 # int | 
    shipping_plan_id = 'shipping_plan_id_example' # str | 

    try:
        # GetBillOfLading
        api_response = api_instance.warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_shipment_id_bill_of_lading_get(shipment_id, shipping_plan_id)
        print("The response of ShipmentsApi->warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_shipment_id_bill_of_lading_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentsApi->warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_shipment_id_bill_of_lading_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **int**|  | 
 **shipping_plan_id** | **str**|  | 

### Return type

[**GetBillOfLadingByShipmentIdResponse**](GetBillOfLadingByShipmentIdResponse.md)

### Authorization

[Linnworks](../README.md#Linnworks)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Server Error |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_shipment_id_get**
> ShipmentModel warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_shipment_id_get(shipment_id, shipping_plan_id)

GetShipmentById

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_v2
from linnworks_api.generated.warehousetransfer_v2.models.shipment_model import ShipmentModel
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
    api_instance = linnworks_api.generated.warehousetransfer_v2.ShipmentsApi(api_client)
    shipment_id = 56 # int | 
    shipping_plan_id = 'shipping_plan_id_example' # str | 

    try:
        # GetShipmentById
        api_response = api_instance.warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_shipment_id_get(shipment_id, shipping_plan_id)
        print("The response of ShipmentsApi->warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_shipment_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentsApi->warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_shipment_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **int**|  | 
 **shipping_plan_id** | **str**|  | 

### Return type

[**ShipmentModel**](ShipmentModel.md)

### Authorization

[Linnworks](../README.md#Linnworks)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Server Error |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_shipment_id_labels_get**
> GetLabelByShipmentIdResponse warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_shipment_id_labels_get(shipment_id, shipping_plan_id, page_type=page_type, label_type=label_type)

GetLabelByShipmentId

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_v2
from linnworks_api.generated.warehousetransfer_v2.models.amazon_label_type import AmazonLabelType
from linnworks_api.generated.warehousetransfer_v2.models.amazon_page_type import AmazonPageType
from linnworks_api.generated.warehousetransfer_v2.models.get_label_by_shipment_id_response import GetLabelByShipmentIdResponse
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
    api_instance = linnworks_api.generated.warehousetransfer_v2.ShipmentsApi(api_client)
    shipment_id = 56 # int | 
    shipping_plan_id = 'shipping_plan_id_example' # str | 
    page_type = linnworks_api.generated.warehousetransfer_v2.AmazonPageType() # AmazonPageType |  (optional)
    label_type = linnworks_api.generated.warehousetransfer_v2.AmazonLabelType() # AmazonLabelType |  (optional)

    try:
        # GetLabelByShipmentId
        api_response = api_instance.warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_shipment_id_labels_get(shipment_id, shipping_plan_id, page_type=page_type, label_type=label_type)
        print("The response of ShipmentsApi->warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_shipment_id_labels_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentsApi->warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_shipment_id_labels_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **int**|  | 
 **shipping_plan_id** | **str**|  | 
 **page_type** | [**AmazonPageType**](.md)|  | [optional] 
 **label_type** | [**AmazonLabelType**](.md)|  | [optional] 

### Return type

[**GetLabelByShipmentIdResponse**](GetLabelByShipmentIdResponse.md)

### Authorization

[Linnworks](../README.md#Linnworks)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Server Error |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

