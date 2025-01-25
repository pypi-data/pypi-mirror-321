# linnworks_api.generated.warehousetransfer_v2.ShipmentBoxApi

All URIs are relative to *https://eu-api.linnworks.net/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_boxes_get**](ShipmentBoxApi.md#warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_boxes_get) | **GET** /warehousetransfer/fba-inbound/shipping-plans/{shippingPlanId}/boxes | GetShipmentBoxes
[**warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_boxes_post**](ShipmentBoxApi.md#warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_boxes_post) | **POST** /warehousetransfer/fba-inbound/shipping-plans/{shippingPlanId}/boxes | AddShipmentBoxes
[**warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_boxes_put**](ShipmentBoxApi.md#warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_boxes_put) | **PUT** /warehousetransfer/fba-inbound/shipping-plans/{shippingPlanId}/boxes | UpdateShipmentBoxes
[**warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_boxes_shipment_box_id_delete**](ShipmentBoxApi.md#warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_boxes_shipment_box_id_delete) | **DELETE** /warehousetransfer/fba-inbound/shipping-plans/{shippingPlanId}/boxes/{shipmentBoxId} | DeleteShipmentBoxes


# **warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_boxes_get**
> List[ShipmentBoxModel] warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_boxes_get(shipping_plan_id)

GetShipmentBoxes

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_v2
from linnworks_api.generated.warehousetransfer_v2.models.shipment_box_model import ShipmentBoxModel
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
    api_instance = linnworks_api.generated.warehousetransfer_v2.ShipmentBoxApi(api_client)
    shipping_plan_id = 56 # int | 

    try:
        # GetShipmentBoxes
        api_response = api_instance.warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_boxes_get(shipping_plan_id)
        print("The response of ShipmentBoxApi->warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_boxes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentBoxApi->warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_boxes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_plan_id** | **int**|  | 

### Return type

[**List[ShipmentBoxModel]**](ShipmentBoxModel.md)

### Authorization

[Linnworks](../README.md#Linnworks)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_boxes_post**
> List[ShipmentBoxModel] warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_boxes_post(shipping_plan_id, add_shipment_box_model)

AddShipmentBoxes

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_v2
from linnworks_api.generated.warehousetransfer_v2.models.add_shipment_box_model import AddShipmentBoxModel
from linnworks_api.generated.warehousetransfer_v2.models.shipment_box_model import ShipmentBoxModel
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
    api_instance = linnworks_api.generated.warehousetransfer_v2.ShipmentBoxApi(api_client)
    shipping_plan_id = 56 # int | 
    add_shipment_box_model = [linnworks_api.generated.warehousetransfer_v2.AddShipmentBoxModel()] # List[AddShipmentBoxModel] | 

    try:
        # AddShipmentBoxes
        api_response = api_instance.warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_boxes_post(shipping_plan_id, add_shipment_box_model)
        print("The response of ShipmentBoxApi->warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_boxes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentBoxApi->warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_boxes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_plan_id** | **int**|  | 
 **add_shipment_box_model** | [**List[AddShipmentBoxModel]**](AddShipmentBoxModel.md)|  | 

### Return type

[**List[ShipmentBoxModel]**](ShipmentBoxModel.md)

### Authorization

[Linnworks](../README.md#Linnworks)

### HTTP request headers

 - **Content-Type**: application/json-patch+json; x-api-version=2.0, application/json; x-api-version=2.0, text/json; x-api-version=2.0, application/*+json; x-api-version=2.0
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_boxes_put**
> List[ShipmentBoxModel] warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_boxes_put(shipping_plan_id, update_shipment_box_model)

UpdateShipmentBoxes

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_v2
from linnworks_api.generated.warehousetransfer_v2.models.shipment_box_model import ShipmentBoxModel
from linnworks_api.generated.warehousetransfer_v2.models.update_shipment_box_model import UpdateShipmentBoxModel
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
    api_instance = linnworks_api.generated.warehousetransfer_v2.ShipmentBoxApi(api_client)
    shipping_plan_id = 56 # int | 
    update_shipment_box_model = [linnworks_api.generated.warehousetransfer_v2.UpdateShipmentBoxModel()] # List[UpdateShipmentBoxModel] | 

    try:
        # UpdateShipmentBoxes
        api_response = api_instance.warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_boxes_put(shipping_plan_id, update_shipment_box_model)
        print("The response of ShipmentBoxApi->warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_boxes_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentBoxApi->warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_boxes_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_plan_id** | **int**|  | 
 **update_shipment_box_model** | [**List[UpdateShipmentBoxModel]**](UpdateShipmentBoxModel.md)|  | 

### Return type

[**List[ShipmentBoxModel]**](ShipmentBoxModel.md)

### Authorization

[Linnworks](../README.md#Linnworks)

### HTTP request headers

 - **Content-Type**: application/json-patch+json; x-api-version=2.0, application/json; x-api-version=2.0, text/json; x-api-version=2.0, application/*+json; x-api-version=2.0
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_boxes_shipment_box_id_delete**
> warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_boxes_shipment_box_id_delete(shipping_plan_id, shipment_box_id)

DeleteShipmentBoxes

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
    api_instance = linnworks_api.generated.warehousetransfer_v2.ShipmentBoxApi(api_client)
    shipping_plan_id = 56 # int | 
    shipment_box_id = 56 # int | 

    try:
        # DeleteShipmentBoxes
        api_instance.warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_boxes_shipment_box_id_delete(shipping_plan_id, shipment_box_id)
    except Exception as e:
        print("Exception when calling ShipmentBoxApi->warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_boxes_shipment_box_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_plan_id** | **int**|  | 
 **shipment_box_id** | **int**|  | 

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
**404** | Not Found |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**204** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

