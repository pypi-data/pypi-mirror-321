# linnworks_api.generated.warehousetransfer_new.FbaShipmentBoxItemApi

All URIs are relative to *https://eu-api.linnworks.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxitems_delete**](FbaShipmentBoxItemApi.md#warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxitems_delete) | **DELETE** /warehousetransfer/fbainbound/shippingplans/{shippingPlanId}/shipments/{shipmentId}/boxitems | Delete
[**warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxitems_put**](FbaShipmentBoxItemApi.md#warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxitems_put) | **PUT** /warehousetransfer/fbainbound/shippingplans/{shippingPlanId}/shipments/{shipmentId}/boxitems | AddUpdateShipmentBoxItems
[**warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxitems_withboxandpallet_get**](FbaShipmentBoxItemApi.md#warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxitems_withboxandpallet_get) | **GET** /warehousetransfer/fbainbound/shippingplans/{shippingPlanId}/shipments/{shipmentId}/boxitems/withboxandpallet | GetShipmentItemsWithBoxAndPallet


# **warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxitems_delete**
> int warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxitems_delete(shipment_id, shipping_plan_id, shipment_box_item_ids=shipment_box_item_ids)

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
    api_instance = linnworks_api.generated.warehousetransfer_new.FbaShipmentBoxItemApi(api_client)
    shipment_id = 56 # int | 
    shipping_plan_id = 56 # int | 
    shipment_box_item_ids = [56] # List[int] |  (optional)

    try:
        # Delete
        api_response = api_instance.warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxitems_delete(shipment_id, shipping_plan_id, shipment_box_item_ids=shipment_box_item_ids)
        print("The response of FbaShipmentBoxItemApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxitems_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FbaShipmentBoxItemApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxitems_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **int**|  | 
 **shipping_plan_id** | **int**|  | 
 **shipment_box_item_ids** | [**List[int]**](int.md)|  | [optional] 

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

# **warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxitems_put**
> bool warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxitems_put(shipping_plan_id, shipment_id, add_update_shipment_box_item_request=add_update_shipment_box_item_request)

AddUpdateShipmentBoxItems

Deprecated - please use v2 - [API Docs v2](https://apidocs.linnworks.net/v2/)

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.add_update_shipment_box_item_request import AddUpdateShipmentBoxItemRequest
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
    api_instance = linnworks_api.generated.warehousetransfer_new.FbaShipmentBoxItemApi(api_client)
    shipping_plan_id = 56 # int | 
    shipment_id = 56 # int | 
    add_update_shipment_box_item_request = [linnworks_api.generated.warehousetransfer_new.AddUpdateShipmentBoxItemRequest()] # List[AddUpdateShipmentBoxItemRequest] |  (optional)

    try:
        # AddUpdateShipmentBoxItems
        api_response = api_instance.warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxitems_put(shipping_plan_id, shipment_id, add_update_shipment_box_item_request=add_update_shipment_box_item_request)
        print("The response of FbaShipmentBoxItemApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxitems_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FbaShipmentBoxItemApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxitems_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_plan_id** | **int**|  | 
 **shipment_id** | **int**|  | 
 **add_update_shipment_box_item_request** | [**List[AddUpdateShipmentBoxItemRequest]**](AddUpdateShipmentBoxItemRequest.md)|  | [optional] 

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

# **warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxitems_withboxandpallet_get**
> GetShipmentItemsWithBoxAndPalletResponse warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxitems_withboxandpallet_get(shipping_plan_id, shipment_id)

GetShipmentItemsWithBoxAndPallet

Deprecated - please use v2 - [API Docs v2](https://apidocs.linnworks.net/v2/)

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.get_shipment_items_with_box_and_pallet_response import GetShipmentItemsWithBoxAndPalletResponse
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
    api_instance = linnworks_api.generated.warehousetransfer_new.FbaShipmentBoxItemApi(api_client)
    shipping_plan_id = 56 # int | 
    shipment_id = 56 # int | 

    try:
        # GetShipmentItemsWithBoxAndPallet
        api_response = api_instance.warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxitems_withboxandpallet_get(shipping_plan_id, shipment_id)
        print("The response of FbaShipmentBoxItemApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxitems_withboxandpallet_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FbaShipmentBoxItemApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipment_id_boxitems_withboxandpallet_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_plan_id** | **int**|  | 
 **shipment_id** | **int**|  | 

### Return type

[**GetShipmentItemsWithBoxAndPalletResponse**](GetShipmentItemsWithBoxAndPalletResponse.md)

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

