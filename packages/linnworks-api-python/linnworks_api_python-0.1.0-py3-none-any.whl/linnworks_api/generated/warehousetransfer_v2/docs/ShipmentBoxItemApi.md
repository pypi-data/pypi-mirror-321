# linnworks_api.generated.warehousetransfer_v2.ShipmentBoxItemApi

All URIs are relative to *https://eu-api.linnworks.net/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_box_items_delete**](ShipmentBoxItemApi.md#warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_box_items_delete) | **DELETE** /warehousetransfer/fba-inbound/shipping-plans/{shippingPlanId}/box-items | DeleteShipmentBoxItems
[**warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_box_items_packing_groups_packing_group_id_get**](ShipmentBoxItemApi.md#warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_box_items_packing_groups_packing_group_id_get) | **GET** /warehousetransfer/fba-inbound/shipping-plans/{shippingPlanId}/box-items/packing-groups/{packingGroupId} | GetShipmentBoxItems
[**warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_box_items_post**](ShipmentBoxItemApi.md#warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_box_items_post) | **POST** /warehousetransfer/fba-inbound/shipping-plans/{shippingPlanId}/box-items | AddShipmentBoxItems
[**warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_box_items_put**](ShipmentBoxItemApi.md#warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_box_items_put) | **PUT** /warehousetransfer/fba-inbound/shipping-plans/{shippingPlanId}/box-items | UpdateShipmentBoxItems


# **warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_box_items_delete**
> warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_box_items_delete(shipping_plan_id, shipment_box_item_ids)

DeleteShipmentBoxItems

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
    api_instance = linnworks_api.generated.warehousetransfer_v2.ShipmentBoxItemApi(api_client)
    shipping_plan_id = 56 # int | 
    shipment_box_item_ids = [56] # List[int] | 

    try:
        # DeleteShipmentBoxItems
        api_instance.warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_box_items_delete(shipping_plan_id, shipment_box_item_ids)
    except Exception as e:
        print("Exception when calling ShipmentBoxItemApi->warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_box_items_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_plan_id** | **int**|  | 
 **shipment_box_item_ids** | [**List[int]**](int.md)|  | 

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

# **warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_box_items_packing_groups_packing_group_id_get**
> GetShipmentBoxItemsResponse warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_box_items_packing_groups_packing_group_id_get(shipping_plan_id, packing_group_id)

GetShipmentBoxItems

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_v2
from linnworks_api.generated.warehousetransfer_v2.models.get_shipment_box_items_response import GetShipmentBoxItemsResponse
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
    api_instance = linnworks_api.generated.warehousetransfer_v2.ShipmentBoxItemApi(api_client)
    shipping_plan_id = 56 # int | 
    packing_group_id = 56 # int | 

    try:
        # GetShipmentBoxItems
        api_response = api_instance.warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_box_items_packing_groups_packing_group_id_get(shipping_plan_id, packing_group_id)
        print("The response of ShipmentBoxItemApi->warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_box_items_packing_groups_packing_group_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentBoxItemApi->warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_box_items_packing_groups_packing_group_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_plan_id** | **int**|  | 
 **packing_group_id** | **int**|  | 

### Return type

[**GetShipmentBoxItemsResponse**](GetShipmentBoxItemsResponse.md)

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

# **warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_box_items_post**
> List[ShipmentBoxItemModel] warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_box_items_post(shipping_plan_id, add_shipment_box_item_model)

AddShipmentBoxItems

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_v2
from linnworks_api.generated.warehousetransfer_v2.models.add_shipment_box_item_model import AddShipmentBoxItemModel
from linnworks_api.generated.warehousetransfer_v2.models.shipment_box_item_model import ShipmentBoxItemModel
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
    api_instance = linnworks_api.generated.warehousetransfer_v2.ShipmentBoxItemApi(api_client)
    shipping_plan_id = 56 # int | 
    add_shipment_box_item_model = [linnworks_api.generated.warehousetransfer_v2.AddShipmentBoxItemModel()] # List[AddShipmentBoxItemModel] | 

    try:
        # AddShipmentBoxItems
        api_response = api_instance.warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_box_items_post(shipping_plan_id, add_shipment_box_item_model)
        print("The response of ShipmentBoxItemApi->warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_box_items_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentBoxItemApi->warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_box_items_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_plan_id** | **int**|  | 
 **add_shipment_box_item_model** | [**List[AddShipmentBoxItemModel]**](AddShipmentBoxItemModel.md)|  | 

### Return type

[**List[ShipmentBoxItemModel]**](ShipmentBoxItemModel.md)

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

# **warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_box_items_put**
> List[ShipmentBoxItemModel] warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_box_items_put(shipping_plan_id, update_shipment_box_item_model)

UpdateShipmentBoxItems

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_v2
from linnworks_api.generated.warehousetransfer_v2.models.shipment_box_item_model import ShipmentBoxItemModel
from linnworks_api.generated.warehousetransfer_v2.models.update_shipment_box_item_model import UpdateShipmentBoxItemModel
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
    api_instance = linnworks_api.generated.warehousetransfer_v2.ShipmentBoxItemApi(api_client)
    shipping_plan_id = 56 # int | 
    update_shipment_box_item_model = [linnworks_api.generated.warehousetransfer_v2.UpdateShipmentBoxItemModel()] # List[UpdateShipmentBoxItemModel] | 

    try:
        # UpdateShipmentBoxItems
        api_response = api_instance.warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_box_items_put(shipping_plan_id, update_shipment_box_item_model)
        print("The response of ShipmentBoxItemApi->warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_box_items_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentBoxItemApi->warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_box_items_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_plan_id** | **int**|  | 
 **update_shipment_box_item_model** | [**List[UpdateShipmentBoxItemModel]**](UpdateShipmentBoxItemModel.md)|  | 

### Return type

[**List[ShipmentBoxItemModel]**](ShipmentBoxItemModel.md)

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

