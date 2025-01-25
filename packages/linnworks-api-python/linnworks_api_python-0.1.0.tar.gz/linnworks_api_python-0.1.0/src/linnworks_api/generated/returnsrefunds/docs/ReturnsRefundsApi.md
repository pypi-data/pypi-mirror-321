# linnworks_api.generated.returnsrefunds.ReturnsRefundsApi

All URIs are relative to *https://eu-ext.linnworks.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acknowledge_refund_errors**](ReturnsRefundsApi.md#acknowledge_refund_errors) | **POST** /api/ReturnsRefunds/AcknowledgeRefundErrors | AcknowledgeRefundErrors
[**acknowledge_rma_errors**](ReturnsRefundsApi.md#acknowledge_rma_errors) | **POST** /api/ReturnsRefunds/AcknowledgeRMAErrors | AcknowledgeRMAErrors
[**action_booked_order**](ReturnsRefundsApi.md#action_booked_order) | **POST** /api/ReturnsRefunds/ActionBookedOrder | ActionBookedOrder
[**action_refund**](ReturnsRefundsApi.md#action_refund) | **POST** /api/ReturnsRefunds/ActionRefund | ActionRefund
[**action_rma_booking**](ReturnsRefundsApi.md#action_rma_booking) | **POST** /api/ReturnsRefunds/ActionRMABooking | ActionRMABooking
[**create_refund**](ReturnsRefundsApi.md#create_refund) | **POST** /api/ReturnsRefunds/CreateRefund | CreateRefund
[**create_returns_refunds_csv**](ReturnsRefundsApi.md#create_returns_refunds_csv) | **GET** /api/ReturnsRefunds/CreateReturnsRefundsCSV | CreateReturnsRefundsCSV
[**create_rma_booking**](ReturnsRefundsApi.md#create_rma_booking) | **POST** /api/ReturnsRefunds/CreateRMABooking | CreateRMABooking
[**delete_booked_item**](ReturnsRefundsApi.md#delete_booked_item) | **POST** /api/ReturnsRefunds/DeleteBookedItem | DeleteBookedItem
[**delete_booked_order**](ReturnsRefundsApi.md#delete_booked_order) | **POST** /api/ReturnsRefunds/DeleteBookedOrder | DeleteBookedOrder
[**delete_pending_refund_item**](ReturnsRefundsApi.md#delete_pending_refund_item) | **POST** /api/ReturnsRefunds/DeletePendingRefundItem | DeletePendingRefundItem
[**delete_refund**](ReturnsRefundsApi.md#delete_refund) | **POST** /api/ReturnsRefunds/DeleteRefund | DeleteRefund
[**delete_rma**](ReturnsRefundsApi.md#delete_rma) | **POST** /api/ReturnsRefunds/DeleteRMA | DeleteRMA
[**edit_booked_item_info**](ReturnsRefundsApi.md#edit_booked_item_info) | **POST** /api/ReturnsRefunds/EditBookedItemInfo | EditBookedItemInfo
[**get_actionable_refund_headers**](ReturnsRefundsApi.md#get_actionable_refund_headers) | **POST** /api/ReturnsRefunds/GetActionableRefundHeaders | GetActionableRefundHeaders
[**get_actionable_rma_headers**](ReturnsRefundsApi.md#get_actionable_rma_headers) | **POST** /api/ReturnsRefunds/GetActionableRMAHeaders | GetActionableRMAHeaders
[**get_booked_returns_exchange_orders**](ReturnsRefundsApi.md#get_booked_returns_exchange_orders) | **GET** /api/ReturnsRefunds/GetBookedReturnsExchangeOrders | GetBookedReturnsExchangeOrders
[**get_processed_or_acked_error_refund_headers**](ReturnsRefundsApi.md#get_processed_or_acked_error_refund_headers) | **POST** /api/ReturnsRefunds/GetProcessedOrAckedErrorRefundHeaders | GetProcessedOrAckedErrorRefundHeaders
[**get_processed_or_acked_error_rma_headers**](ReturnsRefundsApi.md#get_processed_or_acked_error_rma_headers) | **POST** /api/ReturnsRefunds/GetProcessedOrAckedErrorRMAHeaders | GetProcessedOrAckedErrorRMAHeaders
[**get_refund_headers_by_order_id**](ReturnsRefundsApi.md#get_refund_headers_by_order_id) | **POST** /api/ReturnsRefunds/GetRefundHeadersByOrderId | GetRefundHeadersByOrderId
[**get_refund_lines_by_header_id**](ReturnsRefundsApi.md#get_refund_lines_by_header_id) | **POST** /api/ReturnsRefunds/GetRefundLinesByHeaderId | GetRefundLinesByHeaderId
[**get_refund_options**](ReturnsRefundsApi.md#get_refund_options) | **POST** /api/ReturnsRefunds/GetRefundOptions | GetRefundOptions
[**get_refund_orders**](ReturnsRefundsApi.md#get_refund_orders) | **GET** /api/ReturnsRefunds/GetRefundOrders | GetRefundOrders
[**get_return_options**](ReturnsRefundsApi.md#get_return_options) | **POST** /api/ReturnsRefunds/GetReturnOptions | GetReturnOptions
[**get_rma_headers_by_order_id**](ReturnsRefundsApi.md#get_rma_headers_by_order_id) | **POST** /api/ReturnsRefunds/GetRMAHeadersByOrderId | GetRMAHeadersByOrderId
[**get_search_types**](ReturnsRefundsApi.md#get_search_types) | **GET** /api/ReturnsRefunds/GetSearchTypes | GetSearchTypes
[**get_total_refunds**](ReturnsRefundsApi.md#get_total_refunds) | **GET** /api/ReturnsRefunds/GetTotalRefunds | GetTotalRefunds
[**get_warehouse_locations**](ReturnsRefundsApi.md#get_warehouse_locations) | **GET** /api/ReturnsRefunds/GetWarehouseLocations | GetWarehouseLocations
[**refund_order**](ReturnsRefundsApi.md#refund_order) | **POST** /api/ReturnsRefunds/RefundOrder | RefundOrder
[**search_returns_refunds_paged**](ReturnsRefundsApi.md#search_returns_refunds_paged) | **GET** /api/ReturnsRefunds/SearchReturnsRefundsPaged | SearchReturnsRefundsPaged
[**update_refund**](ReturnsRefundsApi.md#update_refund) | **POST** /api/ReturnsRefunds/UpdateRefund | UpdateRefund
[**update_rma_booking**](ReturnsRefundsApi.md#update_rma_booking) | **POST** /api/ReturnsRefunds/UpdateRMABooking | UpdateRMABooking


# **acknowledge_refund_errors**
> AcknowledgeRefundErrorsResponse acknowledge_refund_errors(returns_refunds_acknowledge_refund_errors_request)

AcknowledgeRefundErrors

Acknowledges error responses for a given refund header <b>Permissions Required: </b> GlobalPermissions.OrderBook.ReturnsRefunds.Refunds.ApproveRefundsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.returnsrefunds
from linnworks_api.generated.returnsrefunds.models.acknowledge_refund_errors_response import AcknowledgeRefundErrorsResponse
from linnworks_api.generated.returnsrefunds.models.returns_refunds_acknowledge_refund_errors_request import ReturnsRefundsAcknowledgeRefundErrorsRequest
from linnworks_api.generated.returnsrefunds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.returnsrefunds.Configuration(
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
with linnworks_api.generated.returnsrefunds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.returnsrefunds.ReturnsRefundsApi(api_client)
    returns_refunds_acknowledge_refund_errors_request = linnworks_api.generated.returnsrefunds.ReturnsRefundsAcknowledgeRefundErrorsRequest() # ReturnsRefundsAcknowledgeRefundErrorsRequest | 

    try:
        # AcknowledgeRefundErrors
        api_response = api_instance.acknowledge_refund_errors(returns_refunds_acknowledge_refund_errors_request)
        print("The response of ReturnsRefundsApi->acknowledge_refund_errors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnsRefundsApi->acknowledge_refund_errors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **returns_refunds_acknowledge_refund_errors_request** | [**ReturnsRefundsAcknowledgeRefundErrorsRequest**](ReturnsRefundsAcknowledgeRefundErrorsRequest.md)|  | 

### Return type

[**AcknowledgeRefundErrorsResponse**](AcknowledgeRefundErrorsResponse.md)

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

# **acknowledge_rma_errors**
> AcknowledgeRMAErrorsResponse acknowledge_rma_errors(returns_refunds_acknowledge_rma_errors_request)

AcknowledgeRMAErrors

Acknowledges all error responses for a given RMA header <b>Permissions Required: </b> GlobalPermissions.OrderBook.ReturnsRefunds.ReturnsExchanges.AcceptReturnsExchangesNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.returnsrefunds
from linnworks_api.generated.returnsrefunds.models.acknowledge_rma_errors_response import AcknowledgeRMAErrorsResponse
from linnworks_api.generated.returnsrefunds.models.returns_refunds_acknowledge_rma_errors_request import ReturnsRefundsAcknowledgeRMAErrorsRequest
from linnworks_api.generated.returnsrefunds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.returnsrefunds.Configuration(
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
with linnworks_api.generated.returnsrefunds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.returnsrefunds.ReturnsRefundsApi(api_client)
    returns_refunds_acknowledge_rma_errors_request = linnworks_api.generated.returnsrefunds.ReturnsRefundsAcknowledgeRMAErrorsRequest() # ReturnsRefundsAcknowledgeRMAErrorsRequest | 

    try:
        # AcknowledgeRMAErrors
        api_response = api_instance.acknowledge_rma_errors(returns_refunds_acknowledge_rma_errors_request)
        print("The response of ReturnsRefundsApi->acknowledge_rma_errors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnsRefundsApi->acknowledge_rma_errors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **returns_refunds_acknowledge_rma_errors_request** | [**ReturnsRefundsAcknowledgeRMAErrorsRequest**](ReturnsRefundsAcknowledgeRMAErrorsRequest.md)|  | 

### Return type

[**AcknowledgeRMAErrorsResponse**](AcknowledgeRMAErrorsResponse.md)

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

# **action_booked_order**
> action_booked_order(returns_refunds_action_booked_order_request)

ActionBookedOrder

Action list of booked returns/exchange items for a given order ID. If the return is for a batched item, the batch must be booked in manually. <b>Permissions Required: </b> GlobalPermissions.OrderBook.ReturnsRefundsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.returnsrefunds
from linnworks_api.generated.returnsrefunds.models.returns_refunds_action_booked_order_request import ReturnsRefundsActionBookedOrderRequest
from linnworks_api.generated.returnsrefunds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.returnsrefunds.Configuration(
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
with linnworks_api.generated.returnsrefunds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.returnsrefunds.ReturnsRefundsApi(api_client)
    returns_refunds_action_booked_order_request = linnworks_api.generated.returnsrefunds.ReturnsRefundsActionBookedOrderRequest() # ReturnsRefundsActionBookedOrderRequest | 

    try:
        # ActionBookedOrder
        api_instance.action_booked_order(returns_refunds_action_booked_order_request)
    except Exception as e:
        print("Exception when calling ReturnsRefundsApi->action_booked_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **returns_refunds_action_booked_order_request** | [**ReturnsRefundsActionBookedOrderRequest**](ReturnsRefundsActionBookedOrderRequest.md)|  | 

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

# **action_refund**
> ActionRefundResponse action_refund(returns_refunds_action_refund_request)

ActionRefund

Sends a refund to the channel for actioning <b>Permissions Required: </b> GlobalPermissions.OrderBook.ReturnsRefunds.Refunds.ApproveRefundsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.returnsrefunds
from linnworks_api.generated.returnsrefunds.models.action_refund_response import ActionRefundResponse
from linnworks_api.generated.returnsrefunds.models.returns_refunds_action_refund_request import ReturnsRefundsActionRefundRequest
from linnworks_api.generated.returnsrefunds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.returnsrefunds.Configuration(
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
with linnworks_api.generated.returnsrefunds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.returnsrefunds.ReturnsRefundsApi(api_client)
    returns_refunds_action_refund_request = linnworks_api.generated.returnsrefunds.ReturnsRefundsActionRefundRequest() # ReturnsRefundsActionRefundRequest | 

    try:
        # ActionRefund
        api_response = api_instance.action_refund(returns_refunds_action_refund_request)
        print("The response of ReturnsRefundsApi->action_refund:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnsRefundsApi->action_refund: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **returns_refunds_action_refund_request** | [**ReturnsRefundsActionRefundRequest**](ReturnsRefundsActionRefundRequest.md)|  | 

### Return type

[**ActionRefundResponse**](ActionRefundResponse.md)

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

# **action_rma_booking**
> ActionRMABookingResponse action_rma_booking(returns_refunds_action_rma_booking_request)

ActionRMABooking

Accepts a booked return or exchange in the system <b>Permissions Required: </b> GlobalPermissions.OrderBook.ReturnsRefunds.ReturnsExchanges.AcceptReturnsExchangesNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.returnsrefunds
from linnworks_api.generated.returnsrefunds.models.action_rma_booking_response import ActionRMABookingResponse
from linnworks_api.generated.returnsrefunds.models.returns_refunds_action_rma_booking_request import ReturnsRefundsActionRMABookingRequest
from linnworks_api.generated.returnsrefunds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.returnsrefunds.Configuration(
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
with linnworks_api.generated.returnsrefunds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.returnsrefunds.ReturnsRefundsApi(api_client)
    returns_refunds_action_rma_booking_request = linnworks_api.generated.returnsrefunds.ReturnsRefundsActionRMABookingRequest() # ReturnsRefundsActionRMABookingRequest | 

    try:
        # ActionRMABooking
        api_response = api_instance.action_rma_booking(returns_refunds_action_rma_booking_request)
        print("The response of ReturnsRefundsApi->action_rma_booking:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnsRefundsApi->action_rma_booking: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **returns_refunds_action_rma_booking_request** | [**ReturnsRefundsActionRMABookingRequest**](ReturnsRefundsActionRMABookingRequest.md)|  | 

### Return type

[**ActionRMABookingResponse**](ActionRMABookingResponse.md)

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

# **create_refund**
> CreateRefundResponse create_refund(returns_refunds_create_refund_request)

CreateRefund

Creates a refund in the system for approval <b>Permissions Required: </b> GlobalPermissions.OrderBook.ReturnsRefunds.Refunds.CreateRefundsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.returnsrefunds
from linnworks_api.generated.returnsrefunds.models.create_refund_response import CreateRefundResponse
from linnworks_api.generated.returnsrefunds.models.returns_refunds_create_refund_request import ReturnsRefundsCreateRefundRequest
from linnworks_api.generated.returnsrefunds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.returnsrefunds.Configuration(
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
with linnworks_api.generated.returnsrefunds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.returnsrefunds.ReturnsRefundsApi(api_client)
    returns_refunds_create_refund_request = linnworks_api.generated.returnsrefunds.ReturnsRefundsCreateRefundRequest() # ReturnsRefundsCreateRefundRequest | 

    try:
        # CreateRefund
        api_response = api_instance.create_refund(returns_refunds_create_refund_request)
        print("The response of ReturnsRefundsApi->create_refund:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnsRefundsApi->create_refund: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **returns_refunds_create_refund_request** | [**ReturnsRefundsCreateRefundRequest**](ReturnsRefundsCreateRefundRequest.md)|  | 

### Return type

[**CreateRefundResponse**](CreateRefundResponse.md)

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

# **create_returns_refunds_csv**
> str create_returns_refunds_csv(var_from=var_from, to=to, date_type=date_type, search_field=search_field, exact_match=exact_match, search_term=search_term, sort_column=sort_column, sort_direction=sort_direction, history_type=history_type)

CreateReturnsRefundsCSV

Creates a CSV file of the search result for download <b>Permissions Required: </b> GlobalPermissions.OrderBook.ReturnsRefundsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.returnsrefunds
from linnworks_api.generated.returnsrefunds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.returnsrefunds.Configuration(
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
with linnworks_api.generated.returnsrefunds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.returnsrefunds.ReturnsRefundsApi(api_client)
    var_from = '2013-10-20T19:20:30+01:00' # datetime | The lower end of the date range to search. Can be null if searching for 'all dates'. Maximum range is 3 months. (optional)
    to = '2013-10-20T19:20:30+01:00' # datetime | The upper end of the date range to search. Can be null if searching for 'all dates'. Maximum range is 3 months. (optional)
    date_type = 'date_type_example' # str | The search type (e.g. ALLDATES) (optional)
    search_field = 'search_field_example' # str | The field to search by. Can be found by calling GetSearchTypes. (optional)
    exact_match = True # bool | Set to true if an exact match is required for the search data. (optional)
    search_term = 'search_term_example' # str | The term which you are searching for. (optional)
    sort_column = 'sort_column_example' # str | The column to sort by (optional)
    sort_direction = True # bool | The sort direction (true = ascending, false = descending). (optional)
    history_type = 'history_type_example' # str | Search type. Allow RETURNS or REFUNDS (optional)

    try:
        # CreateReturnsRefundsCSV
        api_response = api_instance.create_returns_refunds_csv(var_from=var_from, to=to, date_type=date_type, search_field=search_field, exact_match=exact_match, search_term=search_term, sort_column=sort_column, sort_direction=sort_direction, history_type=history_type)
        print("The response of ReturnsRefundsApi->create_returns_refunds_csv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnsRefundsApi->create_returns_refunds_csv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **datetime**| The lower end of the date range to search. Can be null if searching for &#39;all dates&#39;. Maximum range is 3 months. | [optional] 
 **to** | **datetime**| The upper end of the date range to search. Can be null if searching for &#39;all dates&#39;. Maximum range is 3 months. | [optional] 
 **date_type** | **str**| The search type (e.g. ALLDATES) | [optional] 
 **search_field** | **str**| The field to search by. Can be found by calling GetSearchTypes. | [optional] 
 **exact_match** | **bool**| Set to true if an exact match is required for the search data. | [optional] 
 **search_term** | **str**| The term which you are searching for. | [optional] 
 **sort_column** | **str**| The column to sort by | [optional] 
 **sort_direction** | **bool**| The sort direction (true &#x3D; ascending, false &#x3D; descending). | [optional] 
 **history_type** | **str**| Search type. Allow RETURNS or REFUNDS | [optional] 

### Return type

**str**

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

# **create_rma_booking**
> CreateRMABookingResponse create_rma_booking(returns_refunds_create_rma_booking_request)

CreateRMABooking

Creates an RMA booking in the system <b>Permissions Required: </b> GlobalPermissions.OrderBook.ReturnsRefunds.ReturnsExchanges.CreateReturnsExchangesNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.returnsrefunds
from linnworks_api.generated.returnsrefunds.models.create_rma_booking_response import CreateRMABookingResponse
from linnworks_api.generated.returnsrefunds.models.returns_refunds_create_rma_booking_request import ReturnsRefundsCreateRMABookingRequest
from linnworks_api.generated.returnsrefunds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.returnsrefunds.Configuration(
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
with linnworks_api.generated.returnsrefunds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.returnsrefunds.ReturnsRefundsApi(api_client)
    returns_refunds_create_rma_booking_request = linnworks_api.generated.returnsrefunds.ReturnsRefundsCreateRMABookingRequest() # ReturnsRefundsCreateRMABookingRequest | 

    try:
        # CreateRMABooking
        api_response = api_instance.create_rma_booking(returns_refunds_create_rma_booking_request)
        print("The response of ReturnsRefundsApi->create_rma_booking:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnsRefundsApi->create_rma_booking: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **returns_refunds_create_rma_booking_request** | [**ReturnsRefundsCreateRMABookingRequest**](ReturnsRefundsCreateRMABookingRequest.md)|  | 

### Return type

[**CreateRMABookingResponse**](CreateRMABookingResponse.md)

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

# **delete_booked_item**
> delete_booked_item(returns_refunds_delete_booked_item_request)

DeleteBookedItem

Delete a booked returns/exchange order item <b>Permissions Required: </b> GlobalPermissions.OrderBook.ReturnsRefunds.ReturnsExchanges.DeleteReturnsExchangesNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.returnsrefunds
from linnworks_api.generated.returnsrefunds.models.returns_refunds_delete_booked_item_request import ReturnsRefundsDeleteBookedItemRequest
from linnworks_api.generated.returnsrefunds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.returnsrefunds.Configuration(
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
with linnworks_api.generated.returnsrefunds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.returnsrefunds.ReturnsRefundsApi(api_client)
    returns_refunds_delete_booked_item_request = linnworks_api.generated.returnsrefunds.ReturnsRefundsDeleteBookedItemRequest() # ReturnsRefundsDeleteBookedItemRequest | 

    try:
        # DeleteBookedItem
        api_instance.delete_booked_item(returns_refunds_delete_booked_item_request)
    except Exception as e:
        print("Exception when calling ReturnsRefundsApi->delete_booked_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **returns_refunds_delete_booked_item_request** | [**ReturnsRefundsDeleteBookedItemRequest**](ReturnsRefundsDeleteBookedItemRequest.md)|  | 

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

# **delete_booked_order**
> delete_booked_order(returns_refunds_delete_booked_order_request)

DeleteBookedOrder

Deletes a returns/exchange order <b>Permissions Required: </b> GlobalPermissions.OrderBook.ReturnsRefunds.ReturnsExchanges.DeleteReturnsExchangesNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.returnsrefunds
from linnworks_api.generated.returnsrefunds.models.returns_refunds_delete_booked_order_request import ReturnsRefundsDeleteBookedOrderRequest
from linnworks_api.generated.returnsrefunds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.returnsrefunds.Configuration(
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
with linnworks_api.generated.returnsrefunds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.returnsrefunds.ReturnsRefundsApi(api_client)
    returns_refunds_delete_booked_order_request = linnworks_api.generated.returnsrefunds.ReturnsRefundsDeleteBookedOrderRequest() # ReturnsRefundsDeleteBookedOrderRequest | 

    try:
        # DeleteBookedOrder
        api_instance.delete_booked_order(returns_refunds_delete_booked_order_request)
    except Exception as e:
        print("Exception when calling ReturnsRefundsApi->delete_booked_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **returns_refunds_delete_booked_order_request** | [**ReturnsRefundsDeleteBookedOrderRequest**](ReturnsRefundsDeleteBookedOrderRequest.md)|  | 

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

# **delete_pending_refund_item**
> delete_pending_refund_item(returns_refunds_delete_pending_refund_item_request)

DeletePendingRefundItem

Delete a refund item <b>Permissions Required: </b> GlobalPermissions.OrderBook.ReturnsRefunds.Refunds.DeleteRefundsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.returnsrefunds
from linnworks_api.generated.returnsrefunds.models.returns_refunds_delete_pending_refund_item_request import ReturnsRefundsDeletePendingRefundItemRequest
from linnworks_api.generated.returnsrefunds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.returnsrefunds.Configuration(
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
with linnworks_api.generated.returnsrefunds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.returnsrefunds.ReturnsRefundsApi(api_client)
    returns_refunds_delete_pending_refund_item_request = linnworks_api.generated.returnsrefunds.ReturnsRefundsDeletePendingRefundItemRequest() # ReturnsRefundsDeletePendingRefundItemRequest | 

    try:
        # DeletePendingRefundItem
        api_instance.delete_pending_refund_item(returns_refunds_delete_pending_refund_item_request)
    except Exception as e:
        print("Exception when calling ReturnsRefundsApi->delete_pending_refund_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **returns_refunds_delete_pending_refund_item_request** | [**ReturnsRefundsDeletePendingRefundItemRequest**](ReturnsRefundsDeletePendingRefundItemRequest.md)|  | 

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

# **delete_refund**
> object delete_refund(returns_refunds_delete_refund_request)

DeleteRefund

Deletes all lines from the given refund header that have not yet been processed, or acknowledged as errors, removing it from the \"Actionable Refunds\" screen. If no lines are left, the header row is deleted <b>Permissions Required: </b> GlobalPermissions.OrderBook.ReturnsRefunds.Refunds.DeleteRefundsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.returnsrefunds
from linnworks_api.generated.returnsrefunds.models.returns_refunds_delete_refund_request import ReturnsRefundsDeleteRefundRequest
from linnworks_api.generated.returnsrefunds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.returnsrefunds.Configuration(
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
with linnworks_api.generated.returnsrefunds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.returnsrefunds.ReturnsRefundsApi(api_client)
    returns_refunds_delete_refund_request = linnworks_api.generated.returnsrefunds.ReturnsRefundsDeleteRefundRequest() # ReturnsRefundsDeleteRefundRequest | 

    try:
        # DeleteRefund
        api_response = api_instance.delete_refund(returns_refunds_delete_refund_request)
        print("The response of ReturnsRefundsApi->delete_refund:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnsRefundsApi->delete_refund: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **returns_refunds_delete_refund_request** | [**ReturnsRefundsDeleteRefundRequest**](ReturnsRefundsDeleteRefundRequest.md)|  | 

### Return type

**object**

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

# **delete_rma**
> object delete_rma(returns_refunds_delete_rma_request)

DeleteRMA

Deletes all lines from the given RMA header that have not yet been processed, or acknowledged as errors, removing it from the \"RMA Bookings\" screen. If no lines are left, the header row is deleted <b>Permissions Required: </b> GlobalPermissions.OrderBook.ReturnsRefunds.ReturnsExchanges.DeleteReturnsExchangesNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.returnsrefunds
from linnworks_api.generated.returnsrefunds.models.returns_refunds_delete_rma_request import ReturnsRefundsDeleteRMARequest
from linnworks_api.generated.returnsrefunds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.returnsrefunds.Configuration(
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
with linnworks_api.generated.returnsrefunds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.returnsrefunds.ReturnsRefundsApi(api_client)
    returns_refunds_delete_rma_request = linnworks_api.generated.returnsrefunds.ReturnsRefundsDeleteRMARequest() # ReturnsRefundsDeleteRMARequest | 

    try:
        # DeleteRMA
        api_response = api_instance.delete_rma(returns_refunds_delete_rma_request)
        print("The response of ReturnsRefundsApi->delete_rma:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnsRefundsApi->delete_rma: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **returns_refunds_delete_rma_request** | [**ReturnsRefundsDeleteRMARequest**](ReturnsRefundsDeleteRMARequest.md)|  | 

### Return type

**object**

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

# **edit_booked_item_info**
> edit_booked_item_info(returns_refunds_edit_booked_item_info_request)

EditBookedItemInfo

Edit booked exchange/return item <b>Permissions Required: </b> GlobalPermissions.OrderBook.ReturnsRefundsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.returnsrefunds
from linnworks_api.generated.returnsrefunds.models.returns_refunds_edit_booked_item_info_request import ReturnsRefundsEditBookedItemInfoRequest
from linnworks_api.generated.returnsrefunds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.returnsrefunds.Configuration(
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
with linnworks_api.generated.returnsrefunds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.returnsrefunds.ReturnsRefundsApi(api_client)
    returns_refunds_edit_booked_item_info_request = linnworks_api.generated.returnsrefunds.ReturnsRefundsEditBookedItemInfoRequest() # ReturnsRefundsEditBookedItemInfoRequest | 

    try:
        # EditBookedItemInfo
        api_instance.edit_booked_item_info(returns_refunds_edit_booked_item_info_request)
    except Exception as e:
        print("Exception when calling ReturnsRefundsApi->edit_booked_item_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **returns_refunds_edit_booked_item_info_request** | [**ReturnsRefundsEditBookedItemInfoRequest**](ReturnsRefundsEditBookedItemInfoRequest.md)|  | 

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

# **get_actionable_refund_headers**
> GetActionableRefundHeadersResponse get_actionable_refund_headers(returns_refunds_get_actionable_refund_headers_request)

GetActionableRefundHeaders

Returns a paged list of booked refund headers <b>Permissions Required: </b> GlobalPermissions.OrderBook.ReturnsRefunds.Refunds.ViewRefundsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.returnsrefunds
from linnworks_api.generated.returnsrefunds.models.get_actionable_refund_headers_response import GetActionableRefundHeadersResponse
from linnworks_api.generated.returnsrefunds.models.returns_refunds_get_actionable_refund_headers_request import ReturnsRefundsGetActionableRefundHeadersRequest
from linnworks_api.generated.returnsrefunds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.returnsrefunds.Configuration(
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
with linnworks_api.generated.returnsrefunds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.returnsrefunds.ReturnsRefundsApi(api_client)
    returns_refunds_get_actionable_refund_headers_request = linnworks_api.generated.returnsrefunds.ReturnsRefundsGetActionableRefundHeadersRequest() # ReturnsRefundsGetActionableRefundHeadersRequest | 

    try:
        # GetActionableRefundHeaders
        api_response = api_instance.get_actionable_refund_headers(returns_refunds_get_actionable_refund_headers_request)
        print("The response of ReturnsRefundsApi->get_actionable_refund_headers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnsRefundsApi->get_actionable_refund_headers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **returns_refunds_get_actionable_refund_headers_request** | [**ReturnsRefundsGetActionableRefundHeadersRequest**](ReturnsRefundsGetActionableRefundHeadersRequest.md)|  | 

### Return type

[**GetActionableRefundHeadersResponse**](GetActionableRefundHeadersResponse.md)

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

# **get_actionable_rma_headers**
> GetActionableRMAHeadersResponse get_actionable_rma_headers(returns_refunds_get_actionable_rma_headers_request)

GetActionableRMAHeaders

Returns a paged list of booked refund headers <b>Permissions Required: </b> GlobalPermissions.OrderBook.ReturnsRefunds.ReturnsExchanges.ViewReturnsExchangesNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.returnsrefunds
from linnworks_api.generated.returnsrefunds.models.get_actionable_rma_headers_response import GetActionableRMAHeadersResponse
from linnworks_api.generated.returnsrefunds.models.returns_refunds_get_actionable_rma_headers_request import ReturnsRefundsGetActionableRMAHeadersRequest
from linnworks_api.generated.returnsrefunds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.returnsrefunds.Configuration(
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
with linnworks_api.generated.returnsrefunds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.returnsrefunds.ReturnsRefundsApi(api_client)
    returns_refunds_get_actionable_rma_headers_request = linnworks_api.generated.returnsrefunds.ReturnsRefundsGetActionableRMAHeadersRequest() # ReturnsRefundsGetActionableRMAHeadersRequest | 

    try:
        # GetActionableRMAHeaders
        api_response = api_instance.get_actionable_rma_headers(returns_refunds_get_actionable_rma_headers_request)
        print("The response of ReturnsRefundsApi->get_actionable_rma_headers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnsRefundsApi->get_actionable_rma_headers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **returns_refunds_get_actionable_rma_headers_request** | [**ReturnsRefundsGetActionableRMAHeadersRequest**](ReturnsRefundsGetActionableRMAHeadersRequest.md)|  | 

### Return type

[**GetActionableRMAHeadersResponse**](GetActionableRMAHeadersResponse.md)

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

# **get_booked_returns_exchange_orders**
> List[BookedReturnsExchangeOrder] get_booked_returns_exchange_orders()

GetBookedReturnsExchangeOrders

Gets all booked returns/exchange orders <b>Permissions Required: </b> GlobalPermissions.OrderBook.ReturnsRefundsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.returnsrefunds
from linnworks_api.generated.returnsrefunds.models.booked_returns_exchange_order import BookedReturnsExchangeOrder
from linnworks_api.generated.returnsrefunds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.returnsrefunds.Configuration(
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
with linnworks_api.generated.returnsrefunds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.returnsrefunds.ReturnsRefundsApi(api_client)

    try:
        # GetBookedReturnsExchangeOrders
        api_response = api_instance.get_booked_returns_exchange_orders()
        print("The response of ReturnsRefundsApi->get_booked_returns_exchange_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnsRefundsApi->get_booked_returns_exchange_orders: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[BookedReturnsExchangeOrder]**](BookedReturnsExchangeOrder.md)

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

# **get_processed_or_acked_error_refund_headers**
> GetProcessedOrAckedErrorRefundHeadersResponse get_processed_or_acked_error_refund_headers(returns_refunds_get_processed_or_acked_error_refund_headers_request)

GetProcessedOrAckedErrorRefundHeaders

Returns a paged list of processed or acknowledged error refund headers <b>Permissions Required: </b> GlobalPermissions.OrderBook.ReturnsRefunds.Refunds.ViewRefundsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.returnsrefunds
from linnworks_api.generated.returnsrefunds.models.get_processed_or_acked_error_refund_headers_response import GetProcessedOrAckedErrorRefundHeadersResponse
from linnworks_api.generated.returnsrefunds.models.returns_refunds_get_processed_or_acked_error_refund_headers_request import ReturnsRefundsGetProcessedOrAckedErrorRefundHeadersRequest
from linnworks_api.generated.returnsrefunds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.returnsrefunds.Configuration(
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
with linnworks_api.generated.returnsrefunds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.returnsrefunds.ReturnsRefundsApi(api_client)
    returns_refunds_get_processed_or_acked_error_refund_headers_request = linnworks_api.generated.returnsrefunds.ReturnsRefundsGetProcessedOrAckedErrorRefundHeadersRequest() # ReturnsRefundsGetProcessedOrAckedErrorRefundHeadersRequest | 

    try:
        # GetProcessedOrAckedErrorRefundHeaders
        api_response = api_instance.get_processed_or_acked_error_refund_headers(returns_refunds_get_processed_or_acked_error_refund_headers_request)
        print("The response of ReturnsRefundsApi->get_processed_or_acked_error_refund_headers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnsRefundsApi->get_processed_or_acked_error_refund_headers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **returns_refunds_get_processed_or_acked_error_refund_headers_request** | [**ReturnsRefundsGetProcessedOrAckedErrorRefundHeadersRequest**](ReturnsRefundsGetProcessedOrAckedErrorRefundHeadersRequest.md)|  | 

### Return type

[**GetProcessedOrAckedErrorRefundHeadersResponse**](GetProcessedOrAckedErrorRefundHeadersResponse.md)

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

# **get_processed_or_acked_error_rma_headers**
> GetProcessedOrAckedErrorRMAHeadersResponse get_processed_or_acked_error_rma_headers(returns_refunds_get_processed_or_acked_error_rma_headers_request)

GetProcessedOrAckedErrorRMAHeaders

Returns a paged list of processed or acknowledged error RMA headers <b>Permissions Required: </b> GlobalPermissions.OrderBook.ReturnsRefunds.ReturnsExchanges.ViewReturnsExchangesNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.returnsrefunds
from linnworks_api.generated.returnsrefunds.models.get_processed_or_acked_error_rma_headers_response import GetProcessedOrAckedErrorRMAHeadersResponse
from linnworks_api.generated.returnsrefunds.models.returns_refunds_get_processed_or_acked_error_rma_headers_request import ReturnsRefundsGetProcessedOrAckedErrorRMAHeadersRequest
from linnworks_api.generated.returnsrefunds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.returnsrefunds.Configuration(
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
with linnworks_api.generated.returnsrefunds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.returnsrefunds.ReturnsRefundsApi(api_client)
    returns_refunds_get_processed_or_acked_error_rma_headers_request = linnworks_api.generated.returnsrefunds.ReturnsRefundsGetProcessedOrAckedErrorRMAHeadersRequest() # ReturnsRefundsGetProcessedOrAckedErrorRMAHeadersRequest | 

    try:
        # GetProcessedOrAckedErrorRMAHeaders
        api_response = api_instance.get_processed_or_acked_error_rma_headers(returns_refunds_get_processed_or_acked_error_rma_headers_request)
        print("The response of ReturnsRefundsApi->get_processed_or_acked_error_rma_headers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnsRefundsApi->get_processed_or_acked_error_rma_headers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **returns_refunds_get_processed_or_acked_error_rma_headers_request** | [**ReturnsRefundsGetProcessedOrAckedErrorRMAHeadersRequest**](ReturnsRefundsGetProcessedOrAckedErrorRMAHeadersRequest.md)|  | 

### Return type

[**GetProcessedOrAckedErrorRMAHeadersResponse**](GetProcessedOrAckedErrorRMAHeadersResponse.md)

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

# **get_refund_headers_by_order_id**
> GetRefundHeadersByOrderIdResponse get_refund_headers_by_order_id(returns_refunds_get_refund_headers_by_order_id_request)

GetRefundHeadersByOrderId

Returns all refund headers associated with the given order ID <b>Permissions Required: </b> GlobalPermissions.OrderBook.ReturnsRefunds.Refunds.ViewRefundsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.returnsrefunds
from linnworks_api.generated.returnsrefunds.models.get_refund_headers_by_order_id_response import GetRefundHeadersByOrderIdResponse
from linnworks_api.generated.returnsrefunds.models.returns_refunds_get_refund_headers_by_order_id_request import ReturnsRefundsGetRefundHeadersByOrderIdRequest
from linnworks_api.generated.returnsrefunds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.returnsrefunds.Configuration(
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
with linnworks_api.generated.returnsrefunds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.returnsrefunds.ReturnsRefundsApi(api_client)
    returns_refunds_get_refund_headers_by_order_id_request = linnworks_api.generated.returnsrefunds.ReturnsRefundsGetRefundHeadersByOrderIdRequest() # ReturnsRefundsGetRefundHeadersByOrderIdRequest | 

    try:
        # GetRefundHeadersByOrderId
        api_response = api_instance.get_refund_headers_by_order_id(returns_refunds_get_refund_headers_by_order_id_request)
        print("The response of ReturnsRefundsApi->get_refund_headers_by_order_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnsRefundsApi->get_refund_headers_by_order_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **returns_refunds_get_refund_headers_by_order_id_request** | [**ReturnsRefundsGetRefundHeadersByOrderIdRequest**](ReturnsRefundsGetRefundHeadersByOrderIdRequest.md)|  | 

### Return type

[**GetRefundHeadersByOrderIdResponse**](GetRefundHeadersByOrderIdResponse.md)

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

# **get_refund_lines_by_header_id**
> GetRefundLinesByHeaderIdResponse get_refund_lines_by_header_id(returns_refunds_get_refund_lines_by_header_id_request)

GetRefundLinesByHeaderId

Returns a refund, given its header ID <b>Permissions Required: </b> GlobalPermissions.OrderBook.ReturnsRefunds.Refunds.ViewRefundsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.returnsrefunds
from linnworks_api.generated.returnsrefunds.models.get_refund_lines_by_header_id_response import GetRefundLinesByHeaderIdResponse
from linnworks_api.generated.returnsrefunds.models.returns_refunds_get_refund_lines_by_header_id_request import ReturnsRefundsGetRefundLinesByHeaderIdRequest
from linnworks_api.generated.returnsrefunds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.returnsrefunds.Configuration(
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
with linnworks_api.generated.returnsrefunds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.returnsrefunds.ReturnsRefundsApi(api_client)
    returns_refunds_get_refund_lines_by_header_id_request = linnworks_api.generated.returnsrefunds.ReturnsRefundsGetRefundLinesByHeaderIdRequest() # ReturnsRefundsGetRefundLinesByHeaderIdRequest | 

    try:
        # GetRefundLinesByHeaderId
        api_response = api_instance.get_refund_lines_by_header_id(returns_refunds_get_refund_lines_by_header_id_request)
        print("The response of ReturnsRefundsApi->get_refund_lines_by_header_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnsRefundsApi->get_refund_lines_by_header_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **returns_refunds_get_refund_lines_by_header_id_request** | [**ReturnsRefundsGetRefundLinesByHeaderIdRequest**](ReturnsRefundsGetRefundLinesByHeaderIdRequest.md)|  | 

### Return type

[**GetRefundLinesByHeaderIdResponse**](GetRefundLinesByHeaderIdResponse.md)

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

# **get_refund_options**
> GetRefundOptionsResponse get_refund_options(returns_refunds_get_refund_options_request)

GetRefundOptions

Returns channel-specific information regarding the types of refund that can be applied to the given order <b>Permissions Required: </b> GlobalPermissions.OrderBook.ReturnsRefunds.Refunds.ViewRefundsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.returnsrefunds
from linnworks_api.generated.returnsrefunds.models.get_refund_options_response import GetRefundOptionsResponse
from linnworks_api.generated.returnsrefunds.models.returns_refunds_get_refund_options_request import ReturnsRefundsGetRefundOptionsRequest
from linnworks_api.generated.returnsrefunds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.returnsrefunds.Configuration(
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
with linnworks_api.generated.returnsrefunds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.returnsrefunds.ReturnsRefundsApi(api_client)
    returns_refunds_get_refund_options_request = linnworks_api.generated.returnsrefunds.ReturnsRefundsGetRefundOptionsRequest() # ReturnsRefundsGetRefundOptionsRequest | 

    try:
        # GetRefundOptions
        api_response = api_instance.get_refund_options(returns_refunds_get_refund_options_request)
        print("The response of ReturnsRefundsApi->get_refund_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnsRefundsApi->get_refund_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **returns_refunds_get_refund_options_request** | [**ReturnsRefundsGetRefundOptionsRequest**](ReturnsRefundsGetRefundOptionsRequest.md)|  | 

### Return type

[**GetRefundOptionsResponse**](GetRefundOptionsResponse.md)

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

# **get_refund_orders**
> List[RefundOrder] get_refund_orders()

GetRefundOrders

Gets all refund order items for all orders <b>Permissions Required: </b> GlobalPermissions.OrderBook.ReturnsRefundsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.returnsrefunds
from linnworks_api.generated.returnsrefunds.models.refund_order import RefundOrder
from linnworks_api.generated.returnsrefunds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.returnsrefunds.Configuration(
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
with linnworks_api.generated.returnsrefunds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.returnsrefunds.ReturnsRefundsApi(api_client)

    try:
        # GetRefundOrders
        api_response = api_instance.get_refund_orders()
        print("The response of ReturnsRefundsApi->get_refund_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnsRefundsApi->get_refund_orders: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[RefundOrder]**](RefundOrder.md)

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

# **get_return_options**
> GetReturnOptionsResponse get_return_options(returns_refunds_get_return_options_request)

GetReturnOptions

Returns channel-specific information regarding the types of refund that can be applied to the given order <b>Permissions Required: </b> GlobalPermissions.OrderBook.ReturnsRefunds.ReturnsExchanges.ViewReturnsExchangesNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.returnsrefunds
from linnworks_api.generated.returnsrefunds.models.get_return_options_response import GetReturnOptionsResponse
from linnworks_api.generated.returnsrefunds.models.returns_refunds_get_return_options_request import ReturnsRefundsGetReturnOptionsRequest
from linnworks_api.generated.returnsrefunds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.returnsrefunds.Configuration(
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
with linnworks_api.generated.returnsrefunds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.returnsrefunds.ReturnsRefundsApi(api_client)
    returns_refunds_get_return_options_request = linnworks_api.generated.returnsrefunds.ReturnsRefundsGetReturnOptionsRequest() # ReturnsRefundsGetReturnOptionsRequest | 

    try:
        # GetReturnOptions
        api_response = api_instance.get_return_options(returns_refunds_get_return_options_request)
        print("The response of ReturnsRefundsApi->get_return_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnsRefundsApi->get_return_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **returns_refunds_get_return_options_request** | [**ReturnsRefundsGetReturnOptionsRequest**](ReturnsRefundsGetReturnOptionsRequest.md)|  | 

### Return type

[**GetReturnOptionsResponse**](GetReturnOptionsResponse.md)

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

# **get_rma_headers_by_order_id**
> GetRMAHeadersByOrderIdResponse get_rma_headers_by_order_id(returns_refunds_get_rma_headers_by_order_id_request)

GetRMAHeadersByOrderId

Returns all RMA headers associated with the given order ID <b>Permissions Required: </b> GlobalPermissions.OrderBook.ReturnsRefunds.Refunds.ViewRefundsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.returnsrefunds
from linnworks_api.generated.returnsrefunds.models.get_rma_headers_by_order_id_response import GetRMAHeadersByOrderIdResponse
from linnworks_api.generated.returnsrefunds.models.returns_refunds_get_rma_headers_by_order_id_request import ReturnsRefundsGetRMAHeadersByOrderIdRequest
from linnworks_api.generated.returnsrefunds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.returnsrefunds.Configuration(
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
with linnworks_api.generated.returnsrefunds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.returnsrefunds.ReturnsRefundsApi(api_client)
    returns_refunds_get_rma_headers_by_order_id_request = linnworks_api.generated.returnsrefunds.ReturnsRefundsGetRMAHeadersByOrderIdRequest() # ReturnsRefundsGetRMAHeadersByOrderIdRequest | 

    try:
        # GetRMAHeadersByOrderId
        api_response = api_instance.get_rma_headers_by_order_id(returns_refunds_get_rma_headers_by_order_id_request)
        print("The response of ReturnsRefundsApi->get_rma_headers_by_order_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnsRefundsApi->get_rma_headers_by_order_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **returns_refunds_get_rma_headers_by_order_id_request** | [**ReturnsRefundsGetRMAHeadersByOrderIdRequest**](ReturnsRefundsGetRMAHeadersByOrderIdRequest.md)|  | 

### Return type

[**GetRMAHeadersByOrderIdResponse**](GetRMAHeadersByOrderIdResponse.md)

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

# **get_search_types**
> List[SearchField] get_search_types(history_type=history_type)

GetSearchTypes

Gets a list of valid search types. These are needed to search processed orders. <b>Permissions Required: </b> GlobalPermissions.OrderBook.ReturnsRefundsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.returnsrefunds
from linnworks_api.generated.returnsrefunds.models.search_field import SearchField
from linnworks_api.generated.returnsrefunds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.returnsrefunds.Configuration(
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
with linnworks_api.generated.returnsrefunds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.returnsrefunds.ReturnsRefundsApi(api_client)
    history_type = 'history_type_example' # str | Search type. Allow RETURNS or REFUNDS (optional)

    try:
        # GetSearchTypes
        api_response = api_instance.get_search_types(history_type=history_type)
        print("The response of ReturnsRefundsApi->get_search_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnsRefundsApi->get_search_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **history_type** | **str**| Search type. Allow RETURNS or REFUNDS | [optional] 

### Return type

[**List[SearchField]**](SearchField.md)

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

# **get_total_refunds**
> float get_total_refunds(fk_order_id=fk_order_id)

GetTotalRefunds

Gets the refundable amount of an order <b>Permissions Required: </b> GlobalPermissions.OrderBook.ReturnsRefundsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.returnsrefunds
from linnworks_api.generated.returnsrefunds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.returnsrefunds.Configuration(
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
with linnworks_api.generated.returnsrefunds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.returnsrefunds.ReturnsRefundsApi(api_client)
    fk_order_id = 'fk_order_id_example' # str | unique order ID of the order (optional)

    try:
        # GetTotalRefunds
        api_response = api_instance.get_total_refunds(fk_order_id=fk_order_id)
        print("The response of ReturnsRefundsApi->get_total_refunds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnsRefundsApi->get_total_refunds: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fk_order_id** | **str**| unique order ID of the order | [optional] 

### Return type

**float**

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

# **get_warehouse_locations**
> List[WarehouseLocation] get_warehouse_locations()

GetWarehouseLocations

Gets all warehouse locations <b>Permissions Required: </b> GlobalPermissions.OrderBook.ReturnsRefundsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.returnsrefunds
from linnworks_api.generated.returnsrefunds.models.warehouse_location import WarehouseLocation
from linnworks_api.generated.returnsrefunds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.returnsrefunds.Configuration(
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
with linnworks_api.generated.returnsrefunds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.returnsrefunds.ReturnsRefundsApi(api_client)

    try:
        # GetWarehouseLocations
        api_response = api_instance.get_warehouse_locations()
        print("The response of ReturnsRefundsApi->get_warehouse_locations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnsRefundsApi->get_warehouse_locations: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[WarehouseLocation]**](WarehouseLocation.md)

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

# **refund_order**
> refund_order(returns_refunds_refund_order_request)

RefundOrder

Refund an order given the order ID <b>Permissions Required: </b> GlobalPermissions.OrderBook.ReturnsRefundsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.returnsrefunds
from linnworks_api.generated.returnsrefunds.models.returns_refunds_refund_order_request import ReturnsRefundsRefundOrderRequest
from linnworks_api.generated.returnsrefunds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.returnsrefunds.Configuration(
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
with linnworks_api.generated.returnsrefunds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.returnsrefunds.ReturnsRefundsApi(api_client)
    returns_refunds_refund_order_request = linnworks_api.generated.returnsrefunds.ReturnsRefundsRefundOrderRequest() # ReturnsRefundsRefundOrderRequest | 

    try:
        # RefundOrder
        api_instance.refund_order(returns_refunds_refund_order_request)
    except Exception as e:
        print("Exception when calling ReturnsRefundsApi->refund_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **returns_refunds_refund_order_request** | [**ReturnsRefundsRefundOrderRequest**](ReturnsRefundsRefundOrderRequest.md)|  | 

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

# **search_returns_refunds_paged**
> GenericPagedResultReturnsRefundsWeb search_returns_refunds_paged(var_from=var_from, to=to, date_type=date_type, search_field=search_field, exact_match=exact_match, search_term=search_term, page_num=page_num, num_entries_per_page=num_entries_per_page, history_type=history_type)

SearchReturnsRefundsPaged

Searches through returns/refunds history that meets the parameters' criteria <b>Permissions Required: </b> GlobalPermissions.OrderBook.ReturnsRefundsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.returnsrefunds
from linnworks_api.generated.returnsrefunds.models.generic_paged_result_returns_refunds_web import GenericPagedResultReturnsRefundsWeb
from linnworks_api.generated.returnsrefunds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.returnsrefunds.Configuration(
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
with linnworks_api.generated.returnsrefunds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.returnsrefunds.ReturnsRefundsApi(api_client)
    var_from = '2013-10-20T19:20:30+01:00' # datetime | The lower end of the date range to search. Can be null if searching for 'all dates'. Maximum range is 3 months. (optional)
    to = '2013-10-20T19:20:30+01:00' # datetime | The upper end of the date range to search. Can be null if searching for 'all dates'. Maximum range is 3 months. (optional)
    date_type = 'date_type_example' # str | The search type (e.g. ALLDATES) (optional)
    search_field = 'search_field_example' # str | The field to search by. Can be found by calling GetSearchTypes. (optional)
    exact_match = True # bool | Set to true if an exact match is required for the search data. (optional)
    search_term = 'search_term_example' # str | The term which you are searching for. (optional)
    page_num = 56 # int | The page number of the request. (optional)
    num_entries_per_page = 56 # int | The number of entries required on a page. Maximum 200. (optional)
    history_type = 'history_type_example' # str | Search type. Allow RETURNS or REFUNDS (optional)

    try:
        # SearchReturnsRefundsPaged
        api_response = api_instance.search_returns_refunds_paged(var_from=var_from, to=to, date_type=date_type, search_field=search_field, exact_match=exact_match, search_term=search_term, page_num=page_num, num_entries_per_page=num_entries_per_page, history_type=history_type)
        print("The response of ReturnsRefundsApi->search_returns_refunds_paged:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnsRefundsApi->search_returns_refunds_paged: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **datetime**| The lower end of the date range to search. Can be null if searching for &#39;all dates&#39;. Maximum range is 3 months. | [optional] 
 **to** | **datetime**| The upper end of the date range to search. Can be null if searching for &#39;all dates&#39;. Maximum range is 3 months. | [optional] 
 **date_type** | **str**| The search type (e.g. ALLDATES) | [optional] 
 **search_field** | **str**| The field to search by. Can be found by calling GetSearchTypes. | [optional] 
 **exact_match** | **bool**| Set to true if an exact match is required for the search data. | [optional] 
 **search_term** | **str**| The term which you are searching for. | [optional] 
 **page_num** | **int**| The page number of the request. | [optional] 
 **num_entries_per_page** | **int**| The number of entries required on a page. Maximum 200. | [optional] 
 **history_type** | **str**| Search type. Allow RETURNS or REFUNDS | [optional] 

### Return type

[**GenericPagedResultReturnsRefundsWeb**](GenericPagedResultReturnsRefundsWeb.md)

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

# **update_refund**
> UpdateRefundResponse update_refund(returns_refunds_update_refund_request)

UpdateRefund

Updates an existing refund in the system. Requires create and delete permissions <b>Permissions Required: </b> GlobalPermissions.OrderBook.ReturnsRefunds.Refunds.CreateRefundsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.returnsrefunds
from linnworks_api.generated.returnsrefunds.models.returns_refunds_update_refund_request import ReturnsRefundsUpdateRefundRequest
from linnworks_api.generated.returnsrefunds.models.update_refund_response import UpdateRefundResponse
from linnworks_api.generated.returnsrefunds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.returnsrefunds.Configuration(
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
with linnworks_api.generated.returnsrefunds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.returnsrefunds.ReturnsRefundsApi(api_client)
    returns_refunds_update_refund_request = linnworks_api.generated.returnsrefunds.ReturnsRefundsUpdateRefundRequest() # ReturnsRefundsUpdateRefundRequest | 

    try:
        # UpdateRefund
        api_response = api_instance.update_refund(returns_refunds_update_refund_request)
        print("The response of ReturnsRefundsApi->update_refund:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnsRefundsApi->update_refund: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **returns_refunds_update_refund_request** | [**ReturnsRefundsUpdateRefundRequest**](ReturnsRefundsUpdateRefundRequest.md)|  | 

### Return type

[**UpdateRefundResponse**](UpdateRefundResponse.md)

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

# **update_rma_booking**
> UpdateRMABookingResponse update_rma_booking(returns_refunds_update_rma_booking_request)

UpdateRMABooking

Updates an RMA booking in the system. Requires create and delete permissions <b>Permissions Required: </b> GlobalPermissions.OrderBook.ReturnsRefunds.ReturnsExchanges.CreateReturnsExchangesNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.returnsrefunds
from linnworks_api.generated.returnsrefunds.models.returns_refunds_update_rma_booking_request import ReturnsRefundsUpdateRMABookingRequest
from linnworks_api.generated.returnsrefunds.models.update_rma_booking_response import UpdateRMABookingResponse
from linnworks_api.generated.returnsrefunds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.returnsrefunds.Configuration(
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
with linnworks_api.generated.returnsrefunds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.returnsrefunds.ReturnsRefundsApi(api_client)
    returns_refunds_update_rma_booking_request = linnworks_api.generated.returnsrefunds.ReturnsRefundsUpdateRMABookingRequest() # ReturnsRefundsUpdateRMABookingRequest | 

    try:
        # UpdateRMABooking
        api_response = api_instance.update_rma_booking(returns_refunds_update_rma_booking_request)
        print("The response of ReturnsRefundsApi->update_rma_booking:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnsRefundsApi->update_rma_booking: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **returns_refunds_update_rma_booking_request** | [**ReturnsRefundsUpdateRMABookingRequest**](ReturnsRefundsUpdateRMABookingRequest.md)|  | 

### Return type

[**UpdateRMABookingResponse**](UpdateRMABookingResponse.md)

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

