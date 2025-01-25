# linnworks_api.generated.openorders.OpenOrdersApi

All URIs are relative to *https://eu-ext.linnworks.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_order_identifier**](OpenOrdersApi.md#assign_order_identifier) | **POST** /api/OpenOrders/AssignOrderIdentifier | AssignOrderIdentifier
[**assign_stock_to_orders**](OpenOrdersApi.md#assign_stock_to_orders) | **POST** /api/OpenOrders/AssignStockToOrders | AssignStockToOrders
[**delete_assigned_stock**](OpenOrdersApi.md#delete_assigned_stock) | **POST** /api/OpenOrders/DeleteAssignedStock | DeleteAssignedStock
[**delete_identifier**](OpenOrdersApi.md#delete_identifier) | **POST** /api/OpenOrders/DeleteIdentifier | DeleteIdentifier
[**get_available_channels**](OpenOrdersApi.md#get_available_channels) | **GET** /api/OpenOrders/GetAvailableChannels | GetAvailableChannels
[**get_identifiers**](OpenOrdersApi.md#get_identifiers) | **GET** /api/OpenOrders/GetIdentifiers | GetIdentifiers
[**get_identifiers_by_order_ids**](OpenOrdersApi.md#get_identifiers_by_order_ids) | **POST** /api/OpenOrders/GetIdentifiersByOrderIds | GetIdentifiersByOrderIds
[**get_open_order_ids**](OpenOrdersApi.md#get_open_order_ids) | **POST** /api/OpenOrders/GetOpenOrderIds | GetOpenOrderIds
[**get_open_orders**](OpenOrdersApi.md#get_open_orders) | **POST** /api/OpenOrders/GetOpenOrders | GetOpenOrders
[**get_open_orders_details**](OpenOrdersApi.md#get_open_orders_details) | **POST** /api/OpenOrders/GetOpenOrdersDetails | GetOpenOrdersDetails
[**get_order_item_indicators**](OpenOrdersApi.md#get_order_item_indicators) | **POST** /api/OpenOrders/GetOrderItemIndicators | GetOrderItemIndicators
[**get_orders_low_fidelity**](OpenOrdersApi.md#get_orders_low_fidelity) | **POST** /api/OpenOrders/GetOrdersLowFidelity | GetOrdersLowFidelity
[**get_view_stats**](OpenOrdersApi.md#get_view_stats) | **POST** /api/OpenOrders/GetViewStats | GetViewStats
[**mark_ready_for_collection**](OpenOrdersApi.md#mark_ready_for_collection) | **POST** /api/OpenOrders/MarkReadyForCollection | MarkReadyForCollection
[**save_identifier**](OpenOrdersApi.md#save_identifier) | **POST** /api/OpenOrders/SaveIdentifier | SaveIdentifier
[**search_orders**](OpenOrdersApi.md#search_orders) | **POST** /api/OpenOrders/SearchOrders | SearchOrders
[**unassign_order_identifier**](OpenOrdersApi.md#unassign_order_identifier) | **POST** /api/OpenOrders/UnassignOrderIdentifier | UnassignOrderIdentifier


# **assign_order_identifier**
> AssignResult assign_order_identifier(request=request)

AssignOrderIdentifier

Add an identifier to an order <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>250</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.openorders
from linnworks_api.generated.openorders.models.assign_result import AssignResult
from linnworks_api.generated.openorders.models.change_order_identifier_request import ChangeOrderIdentifierRequest
from linnworks_api.generated.openorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.openorders.Configuration(
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
with linnworks_api.generated.openorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.openorders.OpenOrdersApi(api_client)
    request = linnworks_api.generated.openorders.ChangeOrderIdentifierRequest() # ChangeOrderIdentifierRequest |  (optional)

    try:
        # AssignOrderIdentifier
        api_response = api_instance.assign_order_identifier(request=request)
        print("The response of OpenOrdersApi->assign_order_identifier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenOrdersApi->assign_order_identifier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ChangeOrderIdentifierRequest**](ChangeOrderIdentifierRequest.md)|  | [optional] 

### Return type

[**AssignResult**](AssignResult.md)

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

# **assign_stock_to_orders**
> AssignStockToOrdersResponseOrderItemBatchExtendedGuid assign_stock_to_orders(request=request)

AssignStockToOrders

Assign Stock to Orders <b>Permissions Required: </b> GlobalPermissions.OrderBook.OpenOrdersNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.openorders
from linnworks_api.generated.openorders.models.assign_stock_to_orders_request import AssignStockToOrdersRequest
from linnworks_api.generated.openorders.models.assign_stock_to_orders_response_order_item_batch_extended_guid import AssignStockToOrdersResponseOrderItemBatchExtendedGuid
from linnworks_api.generated.openorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.openorders.Configuration(
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
with linnworks_api.generated.openorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.openorders.OpenOrdersApi(api_client)
    request = linnworks_api.generated.openorders.AssignStockToOrdersRequest() # AssignStockToOrdersRequest |  (optional)

    try:
        # AssignStockToOrders
        api_response = api_instance.assign_stock_to_orders(request=request)
        print("The response of OpenOrdersApi->assign_stock_to_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenOrdersApi->assign_stock_to_orders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**AssignStockToOrdersRequest**](AssignStockToOrdersRequest.md)|  | [optional] 

### Return type

[**AssignStockToOrdersResponseOrderItemBatchExtendedGuid**](AssignStockToOrdersResponseOrderItemBatchExtendedGuid.md)

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

# **delete_assigned_stock**
> AssignStockToOrdersResponseInt32Int32 delete_assigned_stock(request=request)

DeleteAssignedStock

 <b>Permissions Required: </b> GlobalPermissions.OrderBook.OpenOrdersNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.openorders
from linnworks_api.generated.openorders.models.assign_stock_to_orders_response_int32_int32 import AssignStockToOrdersResponseInt32Int32
from linnworks_api.generated.openorders.models.clear_stock_assignment_request import ClearStockAssignmentRequest
from linnworks_api.generated.openorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.openorders.Configuration(
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
with linnworks_api.generated.openorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.openorders.OpenOrdersApi(api_client)
    request = linnworks_api.generated.openorders.ClearStockAssignmentRequest() # ClearStockAssignmentRequest |  (optional)

    try:
        # DeleteAssignedStock
        api_response = api_instance.delete_assigned_stock(request=request)
        print("The response of OpenOrdersApi->delete_assigned_stock:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenOrdersApi->delete_assigned_stock: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ClearStockAssignmentRequest**](ClearStockAssignmentRequest.md)|  | [optional] 

### Return type

[**AssignStockToOrdersResponseInt32Int32**](AssignStockToOrdersResponseInt32Int32.md)

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

# **delete_identifier**
> delete_identifier(request=request)

DeleteIdentifier

Delete an identifier. This will also remove the identifier from all orders that it's assigned to <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.openorders
from linnworks_api.generated.openorders.models.delete_identifiers_request import DeleteIdentifiersRequest
from linnworks_api.generated.openorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.openorders.Configuration(
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
with linnworks_api.generated.openorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.openorders.OpenOrdersApi(api_client)
    request = linnworks_api.generated.openorders.DeleteIdentifiersRequest() # DeleteIdentifiersRequest |  (optional)

    try:
        # DeleteIdentifier
        api_instance.delete_identifier(request=request)
    except Exception as e:
        print("Exception when calling OpenOrdersApi->delete_identifier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**DeleteIdentifiersRequest**](DeleteIdentifiersRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_channels**
> GetAvailableChannelsResponse get_available_channels()

GetAvailableChannels

 <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.openorders
from linnworks_api.generated.openorders.models.get_available_channels_response import GetAvailableChannelsResponse
from linnworks_api.generated.openorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.openorders.Configuration(
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
with linnworks_api.generated.openorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.openorders.OpenOrdersApi(api_client)

    try:
        # GetAvailableChannels
        api_response = api_instance.get_available_channels()
        print("The response of OpenOrdersApi->get_available_channels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenOrdersApi->get_available_channels: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetAvailableChannelsResponse**](GetAvailableChannelsResponse.md)

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

# **get_identifiers**
> List[Identifier] get_identifiers()

GetIdentifiers

Get all identifiers that are available to add to an order <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.openorders
from linnworks_api.generated.openorders.models.identifier import Identifier
from linnworks_api.generated.openorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.openorders.Configuration(
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
with linnworks_api.generated.openorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.openorders.OpenOrdersApi(api_client)

    try:
        # GetIdentifiers
        api_response = api_instance.get_identifiers()
        print("The response of OpenOrdersApi->get_identifiers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenOrdersApi->get_identifiers: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Identifier]**](Identifier.md)

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

# **get_identifiers_by_order_ids**
> List[OrderIdentifier] get_identifiers_by_order_ids(request=request)

GetIdentifiersByOrderIds

Get all identifiers for a list of orderIds <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.openorders
from linnworks_api.generated.openorders.models.get_order_identifier_request import GetOrderIdentifierRequest
from linnworks_api.generated.openorders.models.order_identifier import OrderIdentifier
from linnworks_api.generated.openorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.openorders.Configuration(
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
with linnworks_api.generated.openorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.openorders.OpenOrdersApi(api_client)
    request = linnworks_api.generated.openorders.GetOrderIdentifierRequest() # GetOrderIdentifierRequest |  (optional)

    try:
        # GetIdentifiersByOrderIds
        api_response = api_instance.get_identifiers_by_order_ids(request=request)
        print("The response of OpenOrdersApi->get_identifiers_by_order_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenOrdersApi->get_identifiers_by_order_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**GetOrderIdentifierRequest**](GetOrderIdentifierRequest.md)|  | [optional] 

### Return type

[**List[OrderIdentifier]**](OrderIdentifier.md)

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

# **get_open_order_ids**
> GenericPagedResultGuid get_open_order_ids(request=request)

GetOpenOrderIds

 <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.openorders
from linnworks_api.generated.openorders.models.generic_paged_result_guid import GenericPagedResultGuid
from linnworks_api.generated.openorders.models.get_open_orders_request import GetOpenOrdersRequest
from linnworks_api.generated.openorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.openorders.Configuration(
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
with linnworks_api.generated.openorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.openorders.OpenOrdersApi(api_client)
    request = linnworks_api.generated.openorders.GetOpenOrdersRequest() # GetOpenOrdersRequest |  (optional)

    try:
        # GetOpenOrderIds
        api_response = api_instance.get_open_order_ids(request=request)
        print("The response of OpenOrdersApi->get_open_order_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenOrdersApi->get_open_order_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**GetOpenOrdersRequest**](GetOpenOrdersRequest.md)|  | [optional] 

### Return type

[**GenericPagedResultGuid**](GenericPagedResultGuid.md)

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

# **get_open_orders**
> PostFilterPagedResponseOpenOrder get_open_orders(request=request)

GetOpenOrders

 <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.openorders
from linnworks_api.generated.openorders.models.get_open_orders_request import GetOpenOrdersRequest
from linnworks_api.generated.openorders.models.post_filter_paged_response_open_order import PostFilterPagedResponseOpenOrder
from linnworks_api.generated.openorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.openorders.Configuration(
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
with linnworks_api.generated.openorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.openorders.OpenOrdersApi(api_client)
    request = linnworks_api.generated.openorders.GetOpenOrdersRequest() # GetOpenOrdersRequest |  (optional)

    try:
        # GetOpenOrders
        api_response = api_instance.get_open_orders(request=request)
        print("The response of OpenOrdersApi->get_open_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenOrdersApi->get_open_orders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**GetOpenOrdersRequest**](GetOpenOrdersRequest.md)|  | [optional] 

### Return type

[**PostFilterPagedResponseOpenOrder**](PostFilterPagedResponseOpenOrder.md)

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

# **get_open_orders_details**
> GetOpenOrdersDetailsResponse get_open_orders_details(request=request)

GetOpenOrdersDetails

Open order details by order ids. Not limited by the number of orders you can retrieve. This call is designed to return ONLY open orders,   it is much faster than GetOrderDetail call <b>Permissions Required: </b> GlobalPermissions.OrderBook.ViewOrderDetailsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.openorders
from linnworks_api.generated.openorders.models.get_open_orders_details_request import GetOpenOrdersDetailsRequest
from linnworks_api.generated.openorders.models.get_open_orders_details_response import GetOpenOrdersDetailsResponse
from linnworks_api.generated.openorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.openorders.Configuration(
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
with linnworks_api.generated.openorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.openorders.OpenOrdersApi(api_client)
    request = linnworks_api.generated.openorders.GetOpenOrdersDetailsRequest() # GetOpenOrdersDetailsRequest |  (optional)

    try:
        # GetOpenOrdersDetails
        api_response = api_instance.get_open_orders_details(request=request)
        print("The response of OpenOrdersApi->get_open_orders_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenOrdersApi->get_open_orders_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**GetOpenOrdersDetailsRequest**](GetOpenOrdersDetailsRequest.md)|  | [optional] 

### Return type

[**GetOpenOrdersDetailsResponse**](GetOpenOrdersDetailsResponse.md)

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

# **get_order_item_indicators**
> GetOrderItemIndicatorResponse get_order_item_indicators(request=request)

GetOrderItemIndicators

 <b>Permissions Required: </b> GlobalPermissions.OrderBook.OpenOrdersNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.openorders
from linnworks_api.generated.openorders.models.get_order_item_indicator_request import GetOrderItemIndicatorRequest
from linnworks_api.generated.openorders.models.get_order_item_indicator_response import GetOrderItemIndicatorResponse
from linnworks_api.generated.openorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.openorders.Configuration(
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
with linnworks_api.generated.openorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.openorders.OpenOrdersApi(api_client)
    request = linnworks_api.generated.openorders.GetOrderItemIndicatorRequest() # GetOrderItemIndicatorRequest |  (optional)

    try:
        # GetOrderItemIndicators
        api_response = api_instance.get_order_item_indicators(request=request)
        print("The response of OpenOrdersApi->get_order_item_indicators:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenOrdersApi->get_order_item_indicators: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**GetOrderItemIndicatorRequest**](GetOrderItemIndicatorRequest.md)|  | [optional] 

### Return type

[**GetOrderItemIndicatorResponse**](GetOrderItemIndicatorResponse.md)

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

# **get_orders_low_fidelity**
> GetOrdersLowFidelityResponse get_orders_low_fidelity(request=request)

GetOrdersLowFidelity

Returns low fidelity view of open orders. The data is generally useful for very basic view or counters of what is in the open orders. Useful for finding orders quickly as it returns all scannable fields of the order and order items such as order ids, skus, barcodes etc. <b>Permissions Required: </b> GlobalPermissions.OrderBook.DespatchConsoleNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.openorders
from linnworks_api.generated.openorders.models.get_orders_low_fidelity_request import GetOrdersLowFidelityRequest
from linnworks_api.generated.openorders.models.get_orders_low_fidelity_response import GetOrdersLowFidelityResponse
from linnworks_api.generated.openorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.openorders.Configuration(
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
with linnworks_api.generated.openorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.openorders.OpenOrdersApi(api_client)
    request = linnworks_api.generated.openorders.GetOrdersLowFidelityRequest() # GetOrdersLowFidelityRequest |  (optional)

    try:
        # GetOrdersLowFidelity
        api_response = api_instance.get_orders_low_fidelity(request=request)
        print("The response of OpenOrdersApi->get_orders_low_fidelity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenOrdersApi->get_orders_low_fidelity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**GetOrdersLowFidelityRequest**](GetOrdersLowFidelityRequest.md)|  | [optional] 

### Return type

[**GetOrdersLowFidelityResponse**](GetOrdersLowFidelityResponse.md)

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

# **get_view_stats**
> List[OrderViewStats] get_view_stats(request=request)

GetViewStats

 <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.openorders
from linnworks_api.generated.openorders.models.get_view_stats_request import GetViewStatsRequest
from linnworks_api.generated.openorders.models.order_view_stats import OrderViewStats
from linnworks_api.generated.openorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.openorders.Configuration(
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
with linnworks_api.generated.openorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.openorders.OpenOrdersApi(api_client)
    request = linnworks_api.generated.openorders.GetViewStatsRequest() # GetViewStatsRequest |  (optional)

    try:
        # GetViewStats
        api_response = api_instance.get_view_stats(request=request)
        print("The response of OpenOrdersApi->get_view_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenOrdersApi->get_view_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**GetViewStatsRequest**](GetViewStatsRequest.md)|  | [optional] 

### Return type

[**List[OrderViewStats]**](OrderViewStats.md)

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

# **mark_ready_for_collection**
> GenericOrderOperationResult mark_ready_for_collection(request=request)

MarkReadyForCollection

 <b>Permissions Required: </b> GlobalPermissions.OrderBook.OpenOrdersNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.openorders
from linnworks_api.generated.openorders.models.generic_order_operation_result import GenericOrderOperationResult
from linnworks_api.generated.openorders.models.mark_ready_for_collection_request import MarkReadyForCollectionRequest
from linnworks_api.generated.openorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.openorders.Configuration(
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
with linnworks_api.generated.openorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.openorders.OpenOrdersApi(api_client)
    request = linnworks_api.generated.openorders.MarkReadyForCollectionRequest() # MarkReadyForCollectionRequest |  (optional)

    try:
        # MarkReadyForCollection
        api_response = api_instance.mark_ready_for_collection(request=request)
        print("The response of OpenOrdersApi->mark_ready_for_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenOrdersApi->mark_ready_for_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**MarkReadyForCollectionRequest**](MarkReadyForCollectionRequest.md)|  | [optional] 

### Return type

[**GenericOrderOperationResult**](GenericOrderOperationResult.md)

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

# **save_identifier**
> Identifier save_identifier(request=request)

SaveIdentifier

Create or update an order identifier <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.openorders
from linnworks_api.generated.openorders.models.identifier import Identifier
from linnworks_api.generated.openorders.models.save_identifiers_request import SaveIdentifiersRequest
from linnworks_api.generated.openorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.openorders.Configuration(
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
with linnworks_api.generated.openorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.openorders.OpenOrdersApi(api_client)
    request = linnworks_api.generated.openorders.SaveIdentifiersRequest() # SaveIdentifiersRequest |  (optional)

    try:
        # SaveIdentifier
        api_response = api_instance.save_identifier(request=request)
        print("The response of OpenOrdersApi->save_identifier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenOrdersApi->save_identifier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**SaveIdentifiersRequest**](SaveIdentifiersRequest.md)|  | [optional] 

### Return type

[**Identifier**](Identifier.md)

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

# **search_orders**
> SearchOrdersResponse search_orders(request=request)

SearchOrders

 <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.openorders
from linnworks_api.generated.openorders.models.search_orders_request import SearchOrdersRequest
from linnworks_api.generated.openorders.models.search_orders_response import SearchOrdersResponse
from linnworks_api.generated.openorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.openorders.Configuration(
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
with linnworks_api.generated.openorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.openorders.OpenOrdersApi(api_client)
    request = linnworks_api.generated.openorders.SearchOrdersRequest() # SearchOrdersRequest |  (optional)

    try:
        # SearchOrders
        api_response = api_instance.search_orders(request=request)
        print("The response of OpenOrdersApi->search_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenOrdersApi->search_orders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**SearchOrdersRequest**](SearchOrdersRequest.md)|  | [optional] 

### Return type

[**SearchOrdersResponse**](SearchOrdersResponse.md)

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

# **unassign_order_identifier**
> AssignResult unassign_order_identifier(request=request)

UnassignOrderIdentifier

Remove an identifier from an order <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>250</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.openorders
from linnworks_api.generated.openorders.models.assign_result import AssignResult
from linnworks_api.generated.openorders.models.change_order_identifier_request import ChangeOrderIdentifierRequest
from linnworks_api.generated.openorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.openorders.Configuration(
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
with linnworks_api.generated.openorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.openorders.OpenOrdersApi(api_client)
    request = linnworks_api.generated.openorders.ChangeOrderIdentifierRequest() # ChangeOrderIdentifierRequest |  (optional)

    try:
        # UnassignOrderIdentifier
        api_response = api_instance.unassign_order_identifier(request=request)
        print("The response of OpenOrdersApi->unassign_order_identifier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenOrdersApi->unassign_order_identifier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ChangeOrderIdentifierRequest**](ChangeOrderIdentifierRequest.md)|  | [optional] 

### Return type

[**AssignResult**](AssignResult.md)

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

