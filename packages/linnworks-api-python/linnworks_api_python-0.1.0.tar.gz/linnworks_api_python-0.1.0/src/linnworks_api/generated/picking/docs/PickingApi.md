# linnworks_api.generated.picking.PickingApi

All URIs are relative to *https://eu-ext.linnworks.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_allocatable_to_pickwave**](PickingApi.md#check_allocatable_to_pickwave) | **POST** /api/Picking/CheckAllocatableToPickwave | CheckAllocatableToPickwave
[**delete_orders_from_picking_waves**](PickingApi.md#delete_orders_from_picking_waves) | **POST** /api/Picking/DeleteOrdersFromPickingWaves | DeleteOrdersFromPickingWaves
[**generate_picking_wave**](PickingApi.md#generate_picking_wave) | **POST** /api/Picking/GeneratePickingWave | GeneratePickingWave
[**get_all_picking_wave_headers**](PickingApi.md#get_all_picking_wave_headers) | **GET** /api/Picking/GetAllPickingWaveHeaders | GetAllPickingWaveHeaders
[**get_all_picking_waves**](PickingApi.md#get_all_picking_waves) | **GET** /api/Picking/GetAllPickingWaves | GetAllPickingWaves
[**get_item_binracks**](PickingApi.md#get_item_binracks) | **GET** /api/Picking/GetItemBinracks | GetItemBinracks
[**get_my_picking_wave_headers**](PickingApi.md#get_my_picking_wave_headers) | **GET** /api/Picking/GetMyPickingWaveHeaders | GetMyPickingWaveHeaders
[**get_my_picking_waves**](PickingApi.md#get_my_picking_waves) | **GET** /api/Picking/GetMyPickingWaves | GetMyPickingWaves
[**get_picking_wave**](PickingApi.md#get_picking_wave) | **GET** /api/Picking/GetPickingWave | GetPickingWave
[**get_pickwave_users_with_summary**](PickingApi.md#get_pickwave_users_with_summary) | **GET** /api/Picking/GetPickwaveUsersWithSummary | GetPickwaveUsersWithSummary
[**update_picked_item_delta**](PickingApi.md#update_picked_item_delta) | **POST** /api/Picking/UpdatePickedItemDelta | UpdatePickedItemDelta
[**update_picking_wave_header**](PickingApi.md#update_picking_wave_header) | **POST** /api/Picking/UpdatePickingWaveHeader | UpdatePickingWaveHeader
[**update_picking_wave_item**](PickingApi.md#update_picking_wave_item) | **POST** /api/Picking/UpdatePickingWaveItem | UpdatePickingWaveItem
[**update_picking_wave_item_with_new_binrack**](PickingApi.md#update_picking_wave_item_with_new_binrack) | **POST** /api/Picking/UpdatePickingWaveItemWithNewBinrack | UpdatePickingWaveItemWithNewBinrack


# **check_allocatable_to_pickwave**
> CheckAllocatableToPickwaveResponse check_allocatable_to_pickwave(picking_check_allocatable_to_pickwave_request)

CheckAllocatableToPickwave

Check a list of Linnworks order ids to see if they can be added to a pickwave <b>Permissions Required: </b> GlobalPermissions.OrderBook.OpenOrders.PickingWaves.GeneratePickingWavesNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.picking
from linnworks_api.generated.picking.models.check_allocatable_to_pickwave_response import CheckAllocatableToPickwaveResponse
from linnworks_api.generated.picking.models.picking_check_allocatable_to_pickwave_request import PickingCheckAllocatableToPickwaveRequest
from linnworks_api.generated.picking.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.picking.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.picking.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.picking.PickingApi(api_client)
    picking_check_allocatable_to_pickwave_request = linnworks_api.generated.picking.PickingCheckAllocatableToPickwaveRequest() # PickingCheckAllocatableToPickwaveRequest | 

    try:
        # CheckAllocatableToPickwave
        api_response = api_instance.check_allocatable_to_pickwave(picking_check_allocatable_to_pickwave_request)
        print("The response of PickingApi->check_allocatable_to_pickwave:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PickingApi->check_allocatable_to_pickwave: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **picking_check_allocatable_to_pickwave_request** | [**PickingCheckAllocatableToPickwaveRequest**](PickingCheckAllocatableToPickwaveRequest.md)|  | 

### Return type

[**CheckAllocatableToPickwaveResponse**](CheckAllocatableToPickwaveResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_orders_from_picking_waves**
> DeleteOrdersFromPickingWavesResponse delete_orders_from_picking_waves(picking_delete_orders_from_picking_waves_request)

DeleteOrdersFromPickingWaves

Delete one or more orders from a pickwave <b>Permissions Required: </b> GlobalPermissions.OrderBook.OpenOrders.PickingWaves.DeletePickingWavesNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.picking
from linnworks_api.generated.picking.models.delete_orders_from_picking_waves_response import DeleteOrdersFromPickingWavesResponse
from linnworks_api.generated.picking.models.picking_delete_orders_from_picking_waves_request import PickingDeleteOrdersFromPickingWavesRequest
from linnworks_api.generated.picking.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.picking.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.picking.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.picking.PickingApi(api_client)
    picking_delete_orders_from_picking_waves_request = linnworks_api.generated.picking.PickingDeleteOrdersFromPickingWavesRequest() # PickingDeleteOrdersFromPickingWavesRequest | 

    try:
        # DeleteOrdersFromPickingWaves
        api_response = api_instance.delete_orders_from_picking_waves(picking_delete_orders_from_picking_waves_request)
        print("The response of PickingApi->delete_orders_from_picking_waves:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PickingApi->delete_orders_from_picking_waves: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **picking_delete_orders_from_picking_waves_request** | [**PickingDeleteOrdersFromPickingWavesRequest**](PickingDeleteOrdersFromPickingWavesRequest.md)|  | 

### Return type

[**DeleteOrdersFromPickingWavesResponse**](DeleteOrdersFromPickingWavesResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_picking_wave**
> GeneratePickingWaveResponse generate_picking_wave(request=request)

GeneratePickingWave

Generate a new pickwave <b>Permissions Required: </b> GlobalPermissions.OrderBook.OpenOrders.PickingWaves.GeneratePickingWavesNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.picking
from linnworks_api.generated.picking.models.generate_picking_wave_response import GeneratePickingWaveResponse
from linnworks_api.generated.picking.models.picking_wave_generate import PickingWaveGenerate
from linnworks_api.generated.picking.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.picking.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.picking.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.picking.PickingApi(api_client)
    request = linnworks_api.generated.picking.PickingWaveGenerate() # PickingWaveGenerate |  (optional)

    try:
        # GeneratePickingWave
        api_response = api_instance.generate_picking_wave(request=request)
        print("The response of PickingApi->generate_picking_wave:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PickingApi->generate_picking_wave: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**PickingWaveGenerate**](PickingWaveGenerate.md)|  | [optional] 

### Return type

[**GeneratePickingWaveResponse**](GeneratePickingWaveResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_picking_wave_headers**
> GetPickingWaveHeadersResponse get_all_picking_wave_headers(state=state, location_id=location_id, detail_level=detail_level)

GetAllPickingWaveHeaders

Get a list of all pickwaves <b>Permissions Required: </b> GlobalPermissions.OrderBook.OpenOrders.PickingWaves.AllPickingWavesNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.picking
from linnworks_api.generated.picking.models.get_picking_wave_headers_response import GetPickingWaveHeadersResponse
from linnworks_api.generated.picking.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.picking.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.picking.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.picking.PickingApi(api_client)
    state = 'state_example' # str | Pickwave state (optional), if not supplied then all states. (optional)
    location_id = 'location_id_example' # str | Location id for waves (optional)
    detail_level = 'detail_level_example' # str | Detail level, if not supplied then all is assumed (optional)

    try:
        # GetAllPickingWaveHeaders
        api_response = api_instance.get_all_picking_wave_headers(state=state, location_id=location_id, detail_level=detail_level)
        print("The response of PickingApi->get_all_picking_wave_headers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PickingApi->get_all_picking_wave_headers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**| Pickwave state (optional), if not supplied then all states. | [optional] 
 **location_id** | **str**| Location id for waves | [optional] 
 **detail_level** | **str**| Detail level, if not supplied then all is assumed | [optional] 

### Return type

[**GetPickingWaveHeadersResponse**](GetPickingWaveHeadersResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_picking_waves**
> GetPickingWavesResponse get_all_picking_waves(state=state, location_id=location_id, detail_level=detail_level)

GetAllPickingWaves

Get a list of all pickwaves <b>Permissions Required: </b> GlobalPermissions.OrderBook.OpenOrders.PickingWaves.AllPickingWavesNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.picking
from linnworks_api.generated.picking.models.get_picking_waves_response import GetPickingWavesResponse
from linnworks_api.generated.picking.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.picking.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.picking.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.picking.PickingApi(api_client)
    state = 'state_example' # str | Pickwave state (optional), if not supplied then all states. (optional)
    location_id = 'location_id_example' # str | Location id for waves (optional)
    detail_level = 'detail_level_example' # str | Detail level, if not supplied then all is assumed (optional)

    try:
        # GetAllPickingWaves
        api_response = api_instance.get_all_picking_waves(state=state, location_id=location_id, detail_level=detail_level)
        print("The response of PickingApi->get_all_picking_waves:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PickingApi->get_all_picking_waves: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**| Pickwave state (optional), if not supplied then all states. | [optional] 
 **location_id** | **str**| Location id for waves | [optional] 
 **detail_level** | **str**| Detail level, if not supplied then all is assumed | [optional] 

### Return type

[**GetPickingWavesResponse**](GetPickingWavesResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_binracks**
> GetItemBinracksResponse get_item_binracks(stock_item_id=stock_item_id, stock_location_id=stock_location_id, current_bin_rack_suggestion=current_bin_rack_suggestion, include_non_pick_locations=include_non_pick_locations)

GetItemBinracks

Returns a list of places that the requested item can be found, other than the location already suggested. <b>Permissions Required: </b> GlobalPermissions.OrderBook.OpenOrders.PickingWavesNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.picking
from linnworks_api.generated.picking.models.get_item_binracks_response import GetItemBinracksResponse
from linnworks_api.generated.picking.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.picking.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.picking.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.picking.PickingApi(api_client)
    stock_item_id = 'stock_item_id_example' # str | Stock item Id (optional)
    stock_location_id = 'stock_location_id_example' # str | Linnworks stock location Id (optional)
    current_bin_rack_suggestion = 'current_bin_rack_suggestion_example' # str | The name of the location that is currently set to pick from (optional)
    include_non_pick_locations = True # bool | If true, the response will also contain binracks that cannot be selected to pick from (optional)

    try:
        # GetItemBinracks
        api_response = api_instance.get_item_binracks(stock_item_id=stock_item_id, stock_location_id=stock_location_id, current_bin_rack_suggestion=current_bin_rack_suggestion, include_non_pick_locations=include_non_pick_locations)
        print("The response of PickingApi->get_item_binracks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PickingApi->get_item_binracks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_item_id** | **str**| Stock item Id | [optional] 
 **stock_location_id** | **str**| Linnworks stock location Id | [optional] 
 **current_bin_rack_suggestion** | **str**| The name of the location that is currently set to pick from | [optional] 
 **include_non_pick_locations** | **bool**| If true, the response will also contain binracks that cannot be selected to pick from | [optional] 

### Return type

[**GetItemBinracksResponse**](GetItemBinracksResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_picking_wave_headers**
> GetPickingWaveHeadersResponse get_my_picking_wave_headers(state=state, location_id=location_id, detail_level=detail_level)

GetMyPickingWaveHeaders

Get a list of list of pickwaves for the current user <b>Permissions Required: </b> GlobalPermissions.OrderBook.OpenOrders.PickingWavesNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.picking
from linnworks_api.generated.picking.models.get_picking_wave_headers_response import GetPickingWaveHeadersResponse
from linnworks_api.generated.picking.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.picking.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.picking.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.picking.PickingApi(api_client)
    state = 'state_example' # str | Pickwave state (optional), if not supplied then all states. (optional)
    location_id = 'location_id_example' # str | Location id for waves (optional)
    detail_level = 'detail_level_example' # str | Detail level, if not supplied then all is assumed (optional)

    try:
        # GetMyPickingWaveHeaders
        api_response = api_instance.get_my_picking_wave_headers(state=state, location_id=location_id, detail_level=detail_level)
        print("The response of PickingApi->get_my_picking_wave_headers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PickingApi->get_my_picking_wave_headers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**| Pickwave state (optional), if not supplied then all states. | [optional] 
 **location_id** | **str**| Location id for waves | [optional] 
 **detail_level** | **str**| Detail level, if not supplied then all is assumed | [optional] 

### Return type

[**GetPickingWaveHeadersResponse**](GetPickingWaveHeadersResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_picking_waves**
> GetPickingWavesResponse get_my_picking_waves(state=state, location_id=location_id, detail_level=detail_level)

GetMyPickingWaves

Get a list of list of pickwaves for the current user <b>Permissions Required: </b> GlobalPermissions.OrderBook.OpenOrders.PickingWavesNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.picking
from linnworks_api.generated.picking.models.get_picking_waves_response import GetPickingWavesResponse
from linnworks_api.generated.picking.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.picking.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.picking.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.picking.PickingApi(api_client)
    state = 'state_example' # str | Pickwave state (optional), if not supplied then all states. (optional)
    location_id = 'location_id_example' # str | Location id for waves (optional)
    detail_level = 'detail_level_example' # str | Detail level, if not supplied then all is assumed (optional)

    try:
        # GetMyPickingWaves
        api_response = api_instance.get_my_picking_waves(state=state, location_id=location_id, detail_level=detail_level)
        print("The response of PickingApi->get_my_picking_waves:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PickingApi->get_my_picking_waves: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**| Pickwave state (optional), if not supplied then all states. | [optional] 
 **location_id** | **str**| Location id for waves | [optional] 
 **detail_level** | **str**| Detail level, if not supplied then all is assumed | [optional] 

### Return type

[**GetPickingWavesResponse**](GetPickingWavesResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_picking_wave**
> GetPickingWavesResponse get_picking_wave(picking_wave_id=picking_wave_id)

GetPickingWave

Get a specific pickwave by id <b>Permissions Required: </b> GlobalPermissions.OrderBook.OpenOrders.PickingWavesNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.picking
from linnworks_api.generated.picking.models.get_picking_waves_response import GetPickingWavesResponse
from linnworks_api.generated.picking.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.picking.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.picking.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.picking.PickingApi(api_client)
    picking_wave_id = 56 # int | Pickwave id (optional)

    try:
        # GetPickingWave
        api_response = api_instance.get_picking_wave(picking_wave_id=picking_wave_id)
        print("The response of PickingApi->get_picking_wave:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PickingApi->get_picking_wave: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **picking_wave_id** | **int**| Pickwave id | [optional] 

### Return type

[**GetPickingWavesResponse**](GetPickingWavesResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pickwave_users_with_summary**
> GetPickwaveUsersWithSummaryResponse get_pickwave_users_with_summary(state=state, location_id=location_id, detail_level=detail_level)

GetPickwaveUsersWithSummary

Returns a list of pickwaves as well as dummy entries for users who have permissions to complete pickwaves, but don't currently have any assigned. These entries will have a PickwaveId of 0. <b>Permissions Required: </b> GlobalPermissions.OrderBook.OpenOrders.PickingWaves.GeneratePickingWavesNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.picking
from linnworks_api.generated.picking.models.get_pickwave_users_with_summary_response import GetPickwaveUsersWithSummaryResponse
from linnworks_api.generated.picking.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.picking.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.picking.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.picking.PickingApi(api_client)
    state = 'state_example' # str | Pickwave state (optional), if not supplied then all states. (optional)
    location_id = 'location_id_example' # str | Location id for waves (optional)
    detail_level = 'detail_level_example' # str | Detail level, if not supplied then all is assumed (optional)

    try:
        # GetPickwaveUsersWithSummary
        api_response = api_instance.get_pickwave_users_with_summary(state=state, location_id=location_id, detail_level=detail_level)
        print("The response of PickingApi->get_pickwave_users_with_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PickingApi->get_pickwave_users_with_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**| Pickwave state (optional), if not supplied then all states. | [optional] 
 **location_id** | **str**| Location id for waves | [optional] 
 **detail_level** | **str**| Detail level, if not supplied then all is assumed | [optional] 

### Return type

[**GetPickwaveUsersWithSummaryResponse**](GetPickwaveUsersWithSummaryResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_picked_item_delta**
> GetPickingWavesResponse update_picked_item_delta(request=request)

UpdatePickedItemDelta

Updates the batch/binrack for allocated pickwave item. Only applicable to pickwave items with batch information <b>Permissions Required: </b> GlobalPermissions.OrderBook.OpenOrders.PickingWavesNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.picking
from linnworks_api.generated.picking.models.get_picking_waves_response import GetPickingWavesResponse
from linnworks_api.generated.picking.models.update_picked_item_delta_request import UpdatePickedItemDeltaRequest
from linnworks_api.generated.picking.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.picking.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.picking.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.picking.PickingApi(api_client)
    request = linnworks_api.generated.picking.UpdatePickedItemDeltaRequest() # UpdatePickedItemDeltaRequest |  (optional)

    try:
        # UpdatePickedItemDelta
        api_response = api_instance.update_picked_item_delta(request=request)
        print("The response of PickingApi->update_picked_item_delta:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PickingApi->update_picked_item_delta: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**UpdatePickedItemDeltaRequest**](UpdatePickedItemDeltaRequest.md)|  | [optional] 

### Return type

[**GetPickingWavesResponse**](GetPickingWavesResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_picking_wave_header**
> GetPickingWavesResponse update_picking_wave_header(request=request)

UpdatePickingWaveHeader

Update a pickwave header <b>Permissions Required: </b> GlobalPermissions.OrderBook.OpenOrders.PickingWavesNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.picking
from linnworks_api.generated.picking.models.get_picking_waves_response import GetPickingWavesResponse
from linnworks_api.generated.picking.models.picking_wave_update_request import PickingWaveUpdateRequest
from linnworks_api.generated.picking.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.picking.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.picking.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.picking.PickingApi(api_client)
    request = linnworks_api.generated.picking.PickingWaveUpdateRequest() # PickingWaveUpdateRequest |  (optional)

    try:
        # UpdatePickingWaveHeader
        api_response = api_instance.update_picking_wave_header(request=request)
        print("The response of PickingApi->update_picking_wave_header:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PickingApi->update_picking_wave_header: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**PickingWaveUpdateRequest**](PickingWaveUpdateRequest.md)|  | [optional] 

### Return type

[**GetPickingWavesResponse**](GetPickingWavesResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_picking_wave_item**
> GetPickingWavesResponse update_picking_wave_item(picking_update_picking_wave_item_request)

UpdatePickingWaveItem

Update on or more pickwave items <b>Permissions Required: </b> GlobalPermissions.OrderBook.OpenOrders.PickingWavesNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.picking
from linnworks_api.generated.picking.models.get_picking_waves_response import GetPickingWavesResponse
from linnworks_api.generated.picking.models.picking_update_picking_wave_item_request import PickingUpdatePickingWaveItemRequest
from linnworks_api.generated.picking.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.picking.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.picking.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.picking.PickingApi(api_client)
    picking_update_picking_wave_item_request = linnworks_api.generated.picking.PickingUpdatePickingWaveItemRequest() # PickingUpdatePickingWaveItemRequest | 

    try:
        # UpdatePickingWaveItem
        api_response = api_instance.update_picking_wave_item(picking_update_picking_wave_item_request)
        print("The response of PickingApi->update_picking_wave_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PickingApi->update_picking_wave_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **picking_update_picking_wave_item_request** | [**PickingUpdatePickingWaveItemRequest**](PickingUpdatePickingWaveItemRequest.md)|  | 

### Return type

[**GetPickingWavesResponse**](GetPickingWavesResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_picking_wave_item_with_new_binrack**
> GetPickingWavesResponse update_picking_wave_item_with_new_binrack(picking_update_picking_wave_item_with_new_binrack_request)

UpdatePickingWaveItemWithNewBinrack

Updates the batch/binrack for allocated pickwave item. Only applicable to pickwave items with batch information <b>Permissions Required: </b> GlobalPermissions.OrderBook.OpenOrders.PickingWavesNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.picking
from linnworks_api.generated.picking.models.get_picking_waves_response import GetPickingWavesResponse
from linnworks_api.generated.picking.models.picking_update_picking_wave_item_with_new_binrack_request import PickingUpdatePickingWaveItemWithNewBinrackRequest
from linnworks_api.generated.picking.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.picking.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.picking.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.picking.PickingApi(api_client)
    picking_update_picking_wave_item_with_new_binrack_request = linnworks_api.generated.picking.PickingUpdatePickingWaveItemWithNewBinrackRequest() # PickingUpdatePickingWaveItemWithNewBinrackRequest | 

    try:
        # UpdatePickingWaveItemWithNewBinrack
        api_response = api_instance.update_picking_wave_item_with_new_binrack(picking_update_picking_wave_item_with_new_binrack_request)
        print("The response of PickingApi->update_picking_wave_item_with_new_binrack:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PickingApi->update_picking_wave_item_with_new_binrack: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **picking_update_picking_wave_item_with_new_binrack_request** | [**PickingUpdatePickingWaveItemWithNewBinrackRequest**](PickingUpdatePickingWaveItemWithNewBinrackRequest.md)|  | 

### Return type

[**GetPickingWavesResponse**](GetPickingWavesResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

