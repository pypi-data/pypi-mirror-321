# linnworks_api.generated.processedorders.ProcessedOrdersApi

All URIs are relative to *https://eu-ext.linnworks.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_order_note**](ProcessedOrdersApi.md#add_order_note) | **POST** /api/ProcessedOrders/AddOrderNote | AddOrderNote
[**add_return_category**](ProcessedOrdersApi.md#add_return_category) | **POST** /api/ProcessedOrders/AddReturnCategory | AddReturnCategory
[**change_order_note**](ProcessedOrdersApi.md#change_order_note) | **POST** /api/ProcessedOrders/ChangeOrderNote | ChangeOrderNote
[**check_order_fully_returned**](ProcessedOrdersApi.md#check_order_fully_returned) | **GET** /api/ProcessedOrders/CheckOrderFullyReturned | CheckOrderFullyReturned
[**create_exchange**](ProcessedOrdersApi.md#create_exchange) | **POST** /api/ProcessedOrders/CreateExchange | CreateExchange
[**create_full_resend**](ProcessedOrdersApi.md#create_full_resend) | **POST** /api/ProcessedOrders/CreateFullResend | CreateFullResend
[**create_resend**](ProcessedOrdersApi.md#create_resend) | **POST** /api/ProcessedOrders/CreateResend | CreateResend
[**delete_order_note**](ProcessedOrdersApi.md#delete_order_note) | **POST** /api/ProcessedOrders/DeleteOrderNote | DeleteOrderNote
[**delete_return_category**](ProcessedOrdersApi.md#delete_return_category) | **POST** /api/ProcessedOrders/DeleteReturnCategory | DeleteReturnCategory
[**download_orders_to_csv**](ProcessedOrdersApi.md#download_orders_to_csv) | **POST** /api/ProcessedOrders/DownloadOrdersToCSV | DownloadOrdersToCSV
[**get_channel_refund_reasons**](ProcessedOrdersApi.md#get_channel_refund_reasons) | **GET** /api/ProcessedOrders/GetChannelRefundReasons | GetChannelRefundReasons
[**get_order_info**](ProcessedOrdersApi.md#get_order_info) | **GET** /api/ProcessedOrders/GetOrderInfo | GetOrderInfo
[**get_order_tracking_urls**](ProcessedOrdersApi.md#get_order_tracking_urls) | **POST** /api/ProcessedOrders/GetOrderTrackingURLs | GetOrderTrackingURLs
[**get_package_split**](ProcessedOrdersApi.md#get_package_split) | **GET** /api/ProcessedOrders/GetPackageSplit | GetPackageSplit
[**get_processed_audit_trail**](ProcessedOrdersApi.md#get_processed_audit_trail) | **GET** /api/ProcessedOrders/GetProcessedAuditTrail | GetProcessedAuditTrail
[**get_processed_order_extended_properties**](ProcessedOrdersApi.md#get_processed_order_extended_properties) | **GET** /api/ProcessedOrders/GetProcessedOrderExtendedProperties | GetProcessedOrderExtendedProperties
[**get_processed_order_notes**](ProcessedOrdersApi.md#get_processed_order_notes) | **GET** /api/ProcessedOrders/GetProcessedOrderNotes | GetProcessedOrderNotes
[**get_processed_relatives**](ProcessedOrdersApi.md#get_processed_relatives) | **GET** /api/ProcessedOrders/GetProcessedRelatives | GetProcessedRelatives
[**get_refundable_service_items**](ProcessedOrdersApi.md#get_refundable_service_items) | **GET** /api/ProcessedOrders/GetRefundableServiceItems | GetRefundableServiceItems
[**get_refunds**](ProcessedOrdersApi.md#get_refunds) | **GET** /api/ProcessedOrders/GetRefunds | GetRefunds
[**get_refunds_options**](ProcessedOrdersApi.md#get_refunds_options) | **GET** /api/ProcessedOrders/GetRefundsOptions | GetRefundsOptions
[**get_return_categories**](ProcessedOrdersApi.md#get_return_categories) | **GET** /api/ProcessedOrders/GetReturnCategories | GetReturnCategories
[**get_return_items_info**](ProcessedOrdersApi.md#get_return_items_info) | **GET** /api/ProcessedOrders/GetReturnItemsInfo | GetReturnItemsInfo
[**get_return_order_info**](ProcessedOrdersApi.md#get_return_order_info) | **GET** /api/ProcessedOrders/GetReturnOrderInfo | GetReturnOrderInfo
[**get_returns_exchanges**](ProcessedOrdersApi.md#get_returns_exchanges) | **GET** /api/ProcessedOrders/GetReturnsExchanges | GetReturnsExchanges
[**get_total_refunds**](ProcessedOrdersApi.md#get_total_refunds) | **GET** /api/ProcessedOrders/GetTotalRefunds | GetTotalRefunds
[**is_refund_valid**](ProcessedOrdersApi.md#is_refund_valid) | **POST** /api/ProcessedOrders/IsRefundValid | IsRefundValid
[**is_refund_validation_required_by_order_id**](ProcessedOrdersApi.md#is_refund_validation_required_by_order_id) | **GET** /api/ProcessedOrders/IsRefundValidationRequiredByOrderId | IsRefundValidationRequiredByOrderId
[**mark_manual_refunds_as_actioned**](ProcessedOrdersApi.md#mark_manual_refunds_as_actioned) | **POST** /api/ProcessedOrders/MarkManualRefundsAsActioned | MarkManualRefundsAsActioned
[**refund_free_text**](ProcessedOrdersApi.md#refund_free_text) | **POST** /api/ProcessedOrders/RefundFreeText | RefundFreeText
[**refund_services**](ProcessedOrdersApi.md#refund_services) | **POST** /api/ProcessedOrders/RefundServices | RefundServices
[**refund_shipping**](ProcessedOrdersApi.md#refund_shipping) | **POST** /api/ProcessedOrders/RefundShipping | RefundShipping
[**rename_return_category**](ProcessedOrdersApi.md#rename_return_category) | **POST** /api/ProcessedOrders/RenameReturnCategory | RenameReturnCategory
[**search_processed_orders**](ProcessedOrdersApi.md#search_processed_orders) | **POST** /api/ProcessedOrders/SearchProcessedOrders | SearchProcessedOrders
[**search_processed_orders_paged**](ProcessedOrdersApi.md#search_processed_orders_paged) | **POST** /api/ProcessedOrders/SearchProcessedOrdersPaged | SearchProcessedOrdersPaged
[**validate_complete_order_refund**](ProcessedOrdersApi.md#validate_complete_order_refund) | **POST** /api/ProcessedOrders/ValidateCompleteOrderRefund | ValidateCompleteOrderRefund


# **add_order_note**
> str add_order_note(processed_orders_add_order_note_request)

AddOrderNote

Use this call to add a new note to an order <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>250</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.processedorders
from linnworks_api.generated.processedorders.models.processed_orders_add_order_note_request import ProcessedOrdersAddOrderNoteRequest
from linnworks_api.generated.processedorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.processedorders.Configuration(
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
with linnworks_api.generated.processedorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.processedorders.ProcessedOrdersApi(api_client)
    processed_orders_add_order_note_request = linnworks_api.generated.processedorders.ProcessedOrdersAddOrderNoteRequest() # ProcessedOrdersAddOrderNoteRequest | 

    try:
        # AddOrderNote
        api_response = api_instance.add_order_note(processed_orders_add_order_note_request)
        print("The response of ProcessedOrdersApi->add_order_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessedOrdersApi->add_order_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processed_orders_add_order_note_request** | [**ProcessedOrdersAddOrderNoteRequest**](ProcessedOrdersAddOrderNoteRequest.md)|  | 

### Return type

**str**

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

# **add_return_category**
> OrderReturnCategory add_return_category(processed_orders_add_return_category_request)

AddReturnCategory

Use this call to add a new return category. <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.processedorders
from linnworks_api.generated.processedorders.models.order_return_category import OrderReturnCategory
from linnworks_api.generated.processedorders.models.processed_orders_add_return_category_request import ProcessedOrdersAddReturnCategoryRequest
from linnworks_api.generated.processedorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.processedorders.Configuration(
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
with linnworks_api.generated.processedorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.processedorders.ProcessedOrdersApi(api_client)
    processed_orders_add_return_category_request = linnworks_api.generated.processedorders.ProcessedOrdersAddReturnCategoryRequest() # ProcessedOrdersAddReturnCategoryRequest | 

    try:
        # AddReturnCategory
        api_response = api_instance.add_return_category(processed_orders_add_return_category_request)
        print("The response of ProcessedOrdersApi->add_return_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessedOrdersApi->add_return_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processed_orders_add_return_category_request** | [**ProcessedOrdersAddReturnCategoryRequest**](ProcessedOrdersAddReturnCategoryRequest.md)|  | 

### Return type

[**OrderReturnCategory**](OrderReturnCategory.md)

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

# **change_order_note**
> change_order_note(processed_orders_change_order_note_request)

ChangeOrderNote

Edit an existing order note <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.processedorders
from linnworks_api.generated.processedorders.models.processed_orders_change_order_note_request import ProcessedOrdersChangeOrderNoteRequest
from linnworks_api.generated.processedorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.processedorders.Configuration(
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
with linnworks_api.generated.processedorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.processedorders.ProcessedOrdersApi(api_client)
    processed_orders_change_order_note_request = linnworks_api.generated.processedorders.ProcessedOrdersChangeOrderNoteRequest() # ProcessedOrdersChangeOrderNoteRequest | 

    try:
        # ChangeOrderNote
        api_instance.change_order_note(processed_orders_change_order_note_request)
    except Exception as e:
        print("Exception when calling ProcessedOrdersApi->change_order_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processed_orders_change_order_note_request** | [**ProcessedOrdersChangeOrderNoteRequest**](ProcessedOrdersChangeOrderNoteRequest.md)|  | 

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

# **check_order_fully_returned**
> bool check_order_fully_returned(pk_order_id=pk_order_id)

CheckOrderFullyReturned

Checks if order was fully returned <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.processedorders
from linnworks_api.generated.processedorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.processedorders.Configuration(
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
with linnworks_api.generated.processedorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.processedorders.ProcessedOrdersApi(api_client)
    pk_order_id = 'pk_order_id_example' # str | Primary key for an order (optional)

    try:
        # CheckOrderFullyReturned
        api_response = api_instance.check_order_fully_returned(pk_order_id=pk_order_id)
        print("The response of ProcessedOrdersApi->check_order_fully_returned:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessedOrdersApi->check_order_fully_returned: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pk_order_id** | **str**| Primary key for an order | [optional] 

### Return type

**bool**

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

# **create_exchange**
> List[ReturnInfo] create_exchange(processed_orders_create_exchange_request)

CreateExchange

 <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.processedorders
from linnworks_api.generated.processedorders.models.processed_orders_create_exchange_request import ProcessedOrdersCreateExchangeRequest
from linnworks_api.generated.processedorders.models.return_info import ReturnInfo
from linnworks_api.generated.processedorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.processedorders.Configuration(
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
with linnworks_api.generated.processedorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.processedorders.ProcessedOrdersApi(api_client)
    processed_orders_create_exchange_request = linnworks_api.generated.processedorders.ProcessedOrdersCreateExchangeRequest() # ProcessedOrdersCreateExchangeRequest | 

    try:
        # CreateExchange
        api_response = api_instance.create_exchange(processed_orders_create_exchange_request)
        print("The response of ProcessedOrdersApi->create_exchange:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessedOrdersApi->create_exchange: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processed_orders_create_exchange_request** | [**ProcessedOrdersCreateExchangeRequest**](ProcessedOrdersCreateExchangeRequest.md)|  | 

### Return type

[**List[ReturnInfo]**](ReturnInfo.md)

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

# **create_full_resend**
> List[ReturnInfo] create_full_resend(processed_orders_create_full_resend_request)

CreateFullResend

 <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.processedorders
from linnworks_api.generated.processedorders.models.processed_orders_create_full_resend_request import ProcessedOrdersCreateFullResendRequest
from linnworks_api.generated.processedorders.models.return_info import ReturnInfo
from linnworks_api.generated.processedorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.processedorders.Configuration(
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
with linnworks_api.generated.processedorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.processedorders.ProcessedOrdersApi(api_client)
    processed_orders_create_full_resend_request = linnworks_api.generated.processedorders.ProcessedOrdersCreateFullResendRequest() # ProcessedOrdersCreateFullResendRequest | 

    try:
        # CreateFullResend
        api_response = api_instance.create_full_resend(processed_orders_create_full_resend_request)
        print("The response of ProcessedOrdersApi->create_full_resend:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessedOrdersApi->create_full_resend: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processed_orders_create_full_resend_request** | [**ProcessedOrdersCreateFullResendRequest**](ProcessedOrdersCreateFullResendRequest.md)|  | 

### Return type

[**List[ReturnInfo]**](ReturnInfo.md)

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

# **create_resend**
> List[ReturnInfo] create_resend(processed_orders_create_resend_request)

CreateResend

Creates a resend <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.processedorders
from linnworks_api.generated.processedorders.models.processed_orders_create_resend_request import ProcessedOrdersCreateResendRequest
from linnworks_api.generated.processedorders.models.return_info import ReturnInfo
from linnworks_api.generated.processedorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.processedorders.Configuration(
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
with linnworks_api.generated.processedorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.processedorders.ProcessedOrdersApi(api_client)
    processed_orders_create_resend_request = linnworks_api.generated.processedorders.ProcessedOrdersCreateResendRequest() # ProcessedOrdersCreateResendRequest | 

    try:
        # CreateResend
        api_response = api_instance.create_resend(processed_orders_create_resend_request)
        print("The response of ProcessedOrdersApi->create_resend:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessedOrdersApi->create_resend: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processed_orders_create_resend_request** | [**ProcessedOrdersCreateResendRequest**](ProcessedOrdersCreateResendRequest.md)|  | 

### Return type

[**List[ReturnInfo]**](ReturnInfo.md)

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

# **delete_order_note**
> delete_order_note(processed_orders_delete_order_note_request)

DeleteOrderNote

Delete an existing order note <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.processedorders
from linnworks_api.generated.processedorders.models.processed_orders_delete_order_note_request import ProcessedOrdersDeleteOrderNoteRequest
from linnworks_api.generated.processedorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.processedorders.Configuration(
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
with linnworks_api.generated.processedorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.processedorders.ProcessedOrdersApi(api_client)
    processed_orders_delete_order_note_request = linnworks_api.generated.processedorders.ProcessedOrdersDeleteOrderNoteRequest() # ProcessedOrdersDeleteOrderNoteRequest | 

    try:
        # DeleteOrderNote
        api_instance.delete_order_note(processed_orders_delete_order_note_request)
    except Exception as e:
        print("Exception when calling ProcessedOrdersApi->delete_order_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processed_orders_delete_order_note_request** | [**ProcessedOrdersDeleteOrderNoteRequest**](ProcessedOrdersDeleteOrderNoteRequest.md)|  | 

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

# **delete_return_category**
> delete_return_category(processed_orders_delete_return_category_request)

DeleteReturnCategory

Use this call to delete an existing return category. <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.processedorders
from linnworks_api.generated.processedorders.models.processed_orders_delete_return_category_request import ProcessedOrdersDeleteReturnCategoryRequest
from linnworks_api.generated.processedorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.processedorders.Configuration(
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
with linnworks_api.generated.processedorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.processedorders.ProcessedOrdersApi(api_client)
    processed_orders_delete_return_category_request = linnworks_api.generated.processedorders.ProcessedOrdersDeleteReturnCategoryRequest() # ProcessedOrdersDeleteReturnCategoryRequest | 

    try:
        # DeleteReturnCategory
        api_instance.delete_return_category(processed_orders_delete_return_category_request)
    except Exception as e:
        print("Exception when calling ProcessedOrdersApi->delete_return_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processed_orders_delete_return_category_request** | [**ProcessedOrdersDeleteReturnCategoryRequest**](ProcessedOrdersDeleteReturnCategoryRequest.md)|  | 

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

# **download_orders_to_csv**
> DownloadOrdersToCSVResponse download_orders_to_csv(processed_orders_download_orders_to_csv_request)

DownloadOrdersToCSV

Download Processed Orders to CSV <b>Permissions Required: </b> GlobalPermissions.OrderBook.ProcessedOrders.DownloadProcessedOrdersNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.processedorders
from linnworks_api.generated.processedorders.models.download_orders_to_csv_response import DownloadOrdersToCSVResponse
from linnworks_api.generated.processedorders.models.processed_orders_download_orders_to_csv_request import ProcessedOrdersDownloadOrdersToCSVRequest
from linnworks_api.generated.processedorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.processedorders.Configuration(
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
with linnworks_api.generated.processedorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.processedorders.ProcessedOrdersApi(api_client)
    processed_orders_download_orders_to_csv_request = linnworks_api.generated.processedorders.ProcessedOrdersDownloadOrdersToCSVRequest() # ProcessedOrdersDownloadOrdersToCSVRequest | 

    try:
        # DownloadOrdersToCSV
        api_response = api_instance.download_orders_to_csv(processed_orders_download_orders_to_csv_request)
        print("The response of ProcessedOrdersApi->download_orders_to_csv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessedOrdersApi->download_orders_to_csv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processed_orders_download_orders_to_csv_request** | [**ProcessedOrdersDownloadOrdersToCSVRequest**](ProcessedOrdersDownloadOrdersToCSVRequest.md)|  | 

### Return type

[**DownloadOrdersToCSVResponse**](DownloadOrdersToCSVResponse.md)

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

# **get_channel_refund_reasons**
> List[ChannelRefundReason] get_channel_refund_reasons(pk_order_id=pk_order_id)

GetChannelRefundReasons

Use this call to get a list of valid channel refund reasons for a given order. These are needed for channel refunds. <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.processedorders
from linnworks_api.generated.processedorders.models.channel_refund_reason import ChannelRefundReason
from linnworks_api.generated.processedorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.processedorders.Configuration(
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
with linnworks_api.generated.processedorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.processedorders.ProcessedOrdersApi(api_client)
    pk_order_id = 'pk_order_id_example' # str | The order id to get reasons for (optional)

    try:
        # GetChannelRefundReasons
        api_response = api_instance.get_channel_refund_reasons(pk_order_id=pk_order_id)
        print("The response of ProcessedOrdersApi->get_channel_refund_reasons:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessedOrdersApi->get_channel_refund_reasons: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pk_order_id** | **str**| The order id to get reasons for | [optional] 

### Return type

[**List[ChannelRefundReason]**](ChannelRefundReason.md)

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

# **get_order_info**
> ProcessedOrderWeb get_order_info(pk_order_id=pk_order_id)

GetOrderInfo

Use this call to retrieve detailed information about a processed order (header level). <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>250</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.processedorders
from linnworks_api.generated.processedorders.models.processed_order_web import ProcessedOrderWeb
from linnworks_api.generated.processedorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.processedorders.Configuration(
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
with linnworks_api.generated.processedorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.processedorders.ProcessedOrdersApi(api_client)
    pk_order_id = 'pk_order_id_example' # str | The id of the order. (optional)

    try:
        # GetOrderInfo
        api_response = api_instance.get_order_info(pk_order_id=pk_order_id)
        print("The response of ProcessedOrdersApi->get_order_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessedOrdersApi->get_order_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pk_order_id** | **str**| The id of the order. | [optional] 

### Return type

[**ProcessedOrderWeb**](ProcessedOrderWeb.md)

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

# **get_order_tracking_urls**
> GetOrderTrackingURLsResponse get_order_tracking_urls(request=request)

GetOrderTrackingURLs

Use this call to retrieve detailed TrackingURL for orders Vendor and TrackingNumber. <b>Permissions Required: </b> GlobalPermissions.OrderBook.ProcessedOrdersNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.processedorders
from linnworks_api.generated.processedorders.models.get_order_tracking_urls_request import GetOrderTrackingURLsRequest
from linnworks_api.generated.processedorders.models.get_order_tracking_urls_response import GetOrderTrackingURLsResponse
from linnworks_api.generated.processedorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.processedorders.Configuration(
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
with linnworks_api.generated.processedorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.processedorders.ProcessedOrdersApi(api_client)
    request = linnworks_api.generated.processedorders.GetOrderTrackingURLsRequest() # GetOrderTrackingURLsRequest | The request for TrackingURL. (optional)

    try:
        # GetOrderTrackingURLs
        api_response = api_instance.get_order_tracking_urls(request=request)
        print("The response of ProcessedOrdersApi->get_order_tracking_urls:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessedOrdersApi->get_order_tracking_urls: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**GetOrderTrackingURLsRequest**](GetOrderTrackingURLsRequest.md)| The request for TrackingURL. | [optional] 

### Return type

[**GetOrderTrackingURLsResponse**](GetOrderTrackingURLsResponse.md)

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

# **get_package_split**
> List[SplitPackaging] get_package_split(pk_order_id=pk_order_id)

GetPackageSplit

Use this call to get split packaging information for an order <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.processedorders
from linnworks_api.generated.processedorders.models.split_packaging import SplitPackaging
from linnworks_api.generated.processedorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.processedorders.Configuration(
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
with linnworks_api.generated.processedorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.processedorders.ProcessedOrdersApi(api_client)
    pk_order_id = 'pk_order_id_example' # str | The order id (optional)

    try:
        # GetPackageSplit
        api_response = api_instance.get_package_split(pk_order_id=pk_order_id)
        print("The response of ProcessedOrdersApi->get_package_split:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessedOrdersApi->get_package_split: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pk_order_id** | **str**| The order id | [optional] 

### Return type

[**List[SplitPackaging]**](SplitPackaging.md)

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

# **get_processed_audit_trail**
> List[AuditEntry] get_processed_audit_trail(pk_order_id=pk_order_id)

GetProcessedAuditTrail

Use this call to get an order's audit trail information <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.processedorders
from linnworks_api.generated.processedorders.models.audit_entry import AuditEntry
from linnworks_api.generated.processedorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.processedorders.Configuration(
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
with linnworks_api.generated.processedorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.processedorders.ProcessedOrdersApi(api_client)
    pk_order_id = 'pk_order_id_example' # str | The order id (optional)

    try:
        # GetProcessedAuditTrail
        api_response = api_instance.get_processed_audit_trail(pk_order_id=pk_order_id)
        print("The response of ProcessedOrdersApi->get_processed_audit_trail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessedOrdersApi->get_processed_audit_trail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pk_order_id** | **str**| The order id | [optional] 

### Return type

[**List[AuditEntry]**](AuditEntry.md)

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

# **get_processed_order_extended_properties**
> List[OrderExtendedProperty] get_processed_order_extended_properties(pk_order_id=pk_order_id)

GetProcessedOrderExtendedProperties

Use this call to retrieve a list of order-level extended properties. <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>250</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.processedorders
from linnworks_api.generated.processedorders.models.order_extended_property import OrderExtendedProperty
from linnworks_api.generated.processedorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.processedorders.Configuration(
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
with linnworks_api.generated.processedorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.processedorders.ProcessedOrdersApi(api_client)
    pk_order_id = 'pk_order_id_example' # str | The order id (optional)

    try:
        # GetProcessedOrderExtendedProperties
        api_response = api_instance.get_processed_order_extended_properties(pk_order_id=pk_order_id)
        print("The response of ProcessedOrdersApi->get_processed_order_extended_properties:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessedOrdersApi->get_processed_order_extended_properties: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pk_order_id** | **str**| The order id | [optional] 

### Return type

[**List[OrderExtendedProperty]**](OrderExtendedProperty.md)

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

# **get_processed_order_notes**
> List[ProcessedOrderNote] get_processed_order_notes(pk_order_id=pk_order_id)

GetProcessedOrderNotes

Use this call to get a list of order notes for a given order <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.processedorders
from linnworks_api.generated.processedorders.models.processed_order_note import ProcessedOrderNote
from linnworks_api.generated.processedorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.processedorders.Configuration(
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
with linnworks_api.generated.processedorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.processedorders.ProcessedOrdersApi(api_client)
    pk_order_id = 'pk_order_id_example' # str | The order id (optional)

    try:
        # GetProcessedOrderNotes
        api_response = api_instance.get_processed_order_notes(pk_order_id=pk_order_id)
        print("The response of ProcessedOrdersApi->get_processed_order_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessedOrdersApi->get_processed_order_notes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pk_order_id** | **str**| The order id | [optional] 

### Return type

[**List[ProcessedOrderNote]**](ProcessedOrderNote.md)

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

# **get_processed_relatives**
> List[ProcessedOrderRelation] get_processed_relatives(pk_order_id=pk_order_id)

GetProcessedRelatives

Use this call to get a list of related orders. <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.processedorders
from linnworks_api.generated.processedorders.models.processed_order_relation import ProcessedOrderRelation
from linnworks_api.generated.processedorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.processedorders.Configuration(
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
with linnworks_api.generated.processedorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.processedorders.ProcessedOrdersApi(api_client)
    pk_order_id = 'pk_order_id_example' # str | The order id (optional)

    try:
        # GetProcessedRelatives
        api_response = api_instance.get_processed_relatives(pk_order_id=pk_order_id)
        print("The response of ProcessedOrdersApi->get_processed_relatives:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessedOrdersApi->get_processed_relatives: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pk_order_id** | **str**| The order id | [optional] 

### Return type

[**List[ProcessedOrderRelation]**](ProcessedOrderRelation.md)

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

# **get_refundable_service_items**
> List[ServiceItem] get_refundable_service_items(pk_order_id=pk_order_id)

GetRefundableServiceItems

Use this call to get a list of service items which can be refunded. <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.processedorders
from linnworks_api.generated.processedorders.models.service_item import ServiceItem
from linnworks_api.generated.processedorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.processedorders.Configuration(
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
with linnworks_api.generated.processedorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.processedorders.ProcessedOrdersApi(api_client)
    pk_order_id = 'pk_order_id_example' # str | The id of the order which the service items belong to. (optional)

    try:
        # GetRefundableServiceItems
        api_response = api_instance.get_refundable_service_items(pk_order_id=pk_order_id)
        print("The response of ProcessedOrdersApi->get_refundable_service_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessedOrdersApi->get_refundable_service_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pk_order_id** | **str**| The id of the order which the service items belong to. | [optional] 

### Return type

[**List[ServiceItem]**](ServiceItem.md)

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

# **get_refunds**
> List[RefundInfo] get_refunds(pk_order_id=pk_order_id)

GetRefunds

Gets all refund order items for an order <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.processedorders
from linnworks_api.generated.processedorders.models.refund_info import RefundInfo
from linnworks_api.generated.processedorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.processedorders.Configuration(
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
with linnworks_api.generated.processedorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.processedorders.ProcessedOrdersApi(api_client)
    pk_order_id = 'pk_order_id_example' # str | Primary key for order (optional)

    try:
        # GetRefunds
        api_response = api_instance.get_refunds(pk_order_id=pk_order_id)
        print("The response of ProcessedOrdersApi->get_refunds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessedOrdersApi->get_refunds: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pk_order_id** | **str**| Primary key for order | [optional] 

### Return type

[**List[RefundInfo]**](RefundInfo.md)

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

# **get_refunds_options**
> RefundScreenOptions get_refunds_options(pk_order_id=pk_order_id)

GetRefundsOptions

Use this call to get information about manual/automated refunds (which kinds of refunds are possible) for a given order. <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.processedorders
from linnworks_api.generated.processedorders.models.refund_screen_options import RefundScreenOptions
from linnworks_api.generated.processedorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.processedorders.Configuration(
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
with linnworks_api.generated.processedorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.processedorders.ProcessedOrdersApi(api_client)
    pk_order_id = 'pk_order_id_example' # str | The id of the order (optional)

    try:
        # GetRefundsOptions
        api_response = api_instance.get_refunds_options(pk_order_id=pk_order_id)
        print("The response of ProcessedOrdersApi->get_refunds_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessedOrdersApi->get_refunds_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pk_order_id** | **str**| The id of the order | [optional] 

### Return type

[**RefundScreenOptions**](RefundScreenOptions.md)

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

# **get_return_categories**
> List[OrderReturnCategory] get_return_categories()

GetReturnCategories

Use this call to retrieve a list of return categories. Used for refunds, resends and exchanges. <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.processedorders
from linnworks_api.generated.processedorders.models.order_return_category import OrderReturnCategory
from linnworks_api.generated.processedorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.processedorders.Configuration(
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
with linnworks_api.generated.processedorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.processedorders.ProcessedOrdersApi(api_client)

    try:
        # GetReturnCategories
        api_response = api_instance.get_return_categories()
        print("The response of ProcessedOrdersApi->get_return_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessedOrdersApi->get_return_categories: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[OrderReturnCategory]**](OrderReturnCategory.md)

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

# **get_return_items_info**
> List[OrderItemReturnInfo] get_return_items_info(pk_order_id=pk_order_id)

GetReturnItemsInfo

Use this call to get a list of all items on an order, including return quantities and resend quantities. The information can be used to calculate how many items has already been returned. <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>250</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.processedorders
from linnworks_api.generated.processedorders.models.order_item_return_info import OrderItemReturnInfo
from linnworks_api.generated.processedorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.processedorders.Configuration(
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
with linnworks_api.generated.processedorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.processedorders.ProcessedOrdersApi(api_client)
    pk_order_id = 'pk_order_id_example' # str | The order id to get the returns for (optional)

    try:
        # GetReturnItemsInfo
        api_response = api_instance.get_return_items_info(pk_order_id=pk_order_id)
        print("The response of ProcessedOrdersApi->get_return_items_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessedOrdersApi->get_return_items_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pk_order_id** | **str**| The order id to get the returns for | [optional] 

### Return type

[**List[OrderItemReturnInfo]**](OrderItemReturnInfo.md)

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

# **get_return_order_info**
> ReturnOrderHeader get_return_order_info(pk_order_id=pk_order_id, include_refund_link=include_refund_link)

GetReturnOrderInfo

Use this call to get basic information about a processed order (e.g. source, subsource, address) as seen on the Returns/Refunds screens. <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.processedorders
from linnworks_api.generated.processedorders.models.return_order_header import ReturnOrderHeader
from linnworks_api.generated.processedorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.processedorders.Configuration(
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
with linnworks_api.generated.processedorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.processedorders.ProcessedOrdersApi(api_client)
    pk_order_id = 'pk_order_id_example' # str | The id of the order. (optional)
    include_refund_link = True # bool | Is a refund link required (not available for all channels). (optional)

    try:
        # GetReturnOrderInfo
        api_response = api_instance.get_return_order_info(pk_order_id=pk_order_id, include_refund_link=include_refund_link)
        print("The response of ProcessedOrdersApi->get_return_order_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessedOrdersApi->get_return_order_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pk_order_id** | **str**| The id of the order. | [optional] 
 **include_refund_link** | **bool**| Is a refund link required (not available for all channels). | [optional] 

### Return type

[**ReturnOrderHeader**](ReturnOrderHeader.md)

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

# **get_returns_exchanges**
> List[ReturnInfo] get_returns_exchanges(pk_order_id=pk_order_id)

GetReturnsExchanges

Use this call to get a basic list of returns, exchanges and resends for an order. <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.processedorders
from linnworks_api.generated.processedorders.models.return_info import ReturnInfo
from linnworks_api.generated.processedorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.processedorders.Configuration(
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
with linnworks_api.generated.processedorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.processedorders.ProcessedOrdersApi(api_client)
    pk_order_id = 'pk_order_id_example' # str | The order id to get the returns for (optional)

    try:
        # GetReturnsExchanges
        api_response = api_instance.get_returns_exchanges(pk_order_id=pk_order_id)
        print("The response of ProcessedOrdersApi->get_returns_exchanges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessedOrdersApi->get_returns_exchanges: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pk_order_id** | **str**| The order id to get the returns for | [optional] 

### Return type

[**List[ReturnInfo]**](ReturnInfo.md)

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
> ExistingRefundTotal get_total_refunds(pk_order_id=pk_order_id, include_bookings=include_bookings)

GetTotalRefunds

Use this call to retrieve the total value of refunds against an order. <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.processedorders
from linnworks_api.generated.processedorders.models.existing_refund_total import ExistingRefundTotal
from linnworks_api.generated.processedorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.processedorders.Configuration(
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
with linnworks_api.generated.processedorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.processedorders.ProcessedOrdersApi(api_client)
    pk_order_id = 'pk_order_id_example' # str | The id of the order (optional)
    include_bookings = True # bool | If true, pending refunds against return bookings and exchange bookings will be included. (Optional, default is false.) (optional)

    try:
        # GetTotalRefunds
        api_response = api_instance.get_total_refunds(pk_order_id=pk_order_id, include_bookings=include_bookings)
        print("The response of ProcessedOrdersApi->get_total_refunds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessedOrdersApi->get_total_refunds: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pk_order_id** | **str**| The id of the order | [optional] 
 **include_bookings** | **bool**| If true, pending refunds against return bookings and exchange bookings will be included. (Optional, default is false.) | [optional] 

### Return type

[**ExistingRefundTotal**](ExistingRefundTotal.md)

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

# **is_refund_valid**
> ValidationResult is_refund_valid(processed_orders_is_refund_valid_request)

IsRefundValid

Use this call to determine if the refunds in a given return set are valid. <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.processedorders
from linnworks_api.generated.processedorders.models.processed_orders_is_refund_valid_request import ProcessedOrdersIsRefundValidRequest
from linnworks_api.generated.processedorders.models.validation_result import ValidationResult
from linnworks_api.generated.processedorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.processedorders.Configuration(
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
with linnworks_api.generated.processedorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.processedorders.ProcessedOrdersApi(api_client)
    processed_orders_is_refund_valid_request = linnworks_api.generated.processedorders.ProcessedOrdersIsRefundValidRequest() # ProcessedOrdersIsRefundValidRequest | 

    try:
        # IsRefundValid
        api_response = api_instance.is_refund_valid(processed_orders_is_refund_valid_request)
        print("The response of ProcessedOrdersApi->is_refund_valid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessedOrdersApi->is_refund_valid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processed_orders_is_refund_valid_request** | [**ProcessedOrdersIsRefundValidRequest**](ProcessedOrdersIsRefundValidRequest.md)|  | 

### Return type

[**ValidationResult**](ValidationResult.md)

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

# **is_refund_validation_required_by_order_id**
> bool is_refund_validation_required_by_order_id(pk_order_id=pk_order_id)

IsRefundValidationRequiredByOrderId

Use this call to determine if validation of refunds or returns/exchanges with refund components is required for a given order. <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.processedorders
from linnworks_api.generated.processedorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.processedorders.Configuration(
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
with linnworks_api.generated.processedorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.processedorders.ProcessedOrdersApi(api_client)
    pk_order_id = 'pk_order_id_example' # str | The order id of the order which requires validation (optional)

    try:
        # IsRefundValidationRequiredByOrderId
        api_response = api_instance.is_refund_validation_required_by_order_id(pk_order_id=pk_order_id)
        print("The response of ProcessedOrdersApi->is_refund_validation_required_by_order_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessedOrdersApi->is_refund_validation_required_by_order_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pk_order_id** | **str**| The order id of the order which requires validation | [optional] 

### Return type

**bool**

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

# **mark_manual_refunds_as_actioned**
> mark_manual_refunds_as_actioned(processed_orders_mark_manual_refunds_as_actioned_request)

MarkManualRefundsAsActioned

Use this call to update pending manual refunds to the actioned state. <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.processedorders
from linnworks_api.generated.processedorders.models.processed_orders_mark_manual_refunds_as_actioned_request import ProcessedOrdersMarkManualRefundsAsActionedRequest
from linnworks_api.generated.processedorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.processedorders.Configuration(
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
with linnworks_api.generated.processedorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.processedorders.ProcessedOrdersApi(api_client)
    processed_orders_mark_manual_refunds_as_actioned_request = linnworks_api.generated.processedorders.ProcessedOrdersMarkManualRefundsAsActionedRequest() # ProcessedOrdersMarkManualRefundsAsActionedRequest | 

    try:
        # MarkManualRefundsAsActioned
        api_instance.mark_manual_refunds_as_actioned(processed_orders_mark_manual_refunds_as_actioned_request)
    except Exception as e:
        print("Exception when calling ProcessedOrdersApi->mark_manual_refunds_as_actioned: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processed_orders_mark_manual_refunds_as_actioned_request** | [**ProcessedOrdersMarkManualRefundsAsActionedRequest**](ProcessedOrdersMarkManualRefundsAsActionedRequest.md)|  | 

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

# **refund_free_text**
> List[RefundInfo] refund_free_text(processed_orders_refund_free_text_request)

RefundFreeText

Use this call to add or update a free text refund. This method can also be used to change the refund amount for any pending manual refund. Please check any automated refunds are valid prior to calling this method. <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.processedorders
from linnworks_api.generated.processedorders.models.processed_orders_refund_free_text_request import ProcessedOrdersRefundFreeTextRequest
from linnworks_api.generated.processedorders.models.refund_info import RefundInfo
from linnworks_api.generated.processedorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.processedorders.Configuration(
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
with linnworks_api.generated.processedorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.processedorders.ProcessedOrdersApi(api_client)
    processed_orders_refund_free_text_request = linnworks_api.generated.processedorders.ProcessedOrdersRefundFreeTextRequest() # ProcessedOrdersRefundFreeTextRequest | 

    try:
        # RefundFreeText
        api_response = api_instance.refund_free_text(processed_orders_refund_free_text_request)
        print("The response of ProcessedOrdersApi->refund_free_text:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessedOrdersApi->refund_free_text: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processed_orders_refund_free_text_request** | [**ProcessedOrdersRefundFreeTextRequest**](ProcessedOrdersRefundFreeTextRequest.md)|  | 

### Return type

[**List[RefundInfo]**](RefundInfo.md)

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

# **refund_services**
> List[RefundInfo] refund_services(processed_orders_refund_services_request)

RefundServices

Use this call to refund one or more services on an order. Please check that any automated refunds are valid prior to calling this method. <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.processedorders
from linnworks_api.generated.processedorders.models.processed_orders_refund_services_request import ProcessedOrdersRefundServicesRequest
from linnworks_api.generated.processedorders.models.refund_info import RefundInfo
from linnworks_api.generated.processedorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.processedorders.Configuration(
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
with linnworks_api.generated.processedorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.processedorders.ProcessedOrdersApi(api_client)
    processed_orders_refund_services_request = linnworks_api.generated.processedorders.ProcessedOrdersRefundServicesRequest() # ProcessedOrdersRefundServicesRequest | 

    try:
        # RefundServices
        api_response = api_instance.refund_services(processed_orders_refund_services_request)
        print("The response of ProcessedOrdersApi->refund_services:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessedOrdersApi->refund_services: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processed_orders_refund_services_request** | [**ProcessedOrdersRefundServicesRequest**](ProcessedOrdersRefundServicesRequest.md)|  | 

### Return type

[**List[RefundInfo]**](RefundInfo.md)

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

# **refund_shipping**
> List[RefundInfo] refund_shipping(processed_orders_refund_shipping_request)

RefundShipping

Use this call to refund shipping for an order. Please check the refund options to ensure that a shipping refund is possible. <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.processedorders
from linnworks_api.generated.processedorders.models.processed_orders_refund_shipping_request import ProcessedOrdersRefundShippingRequest
from linnworks_api.generated.processedorders.models.refund_info import RefundInfo
from linnworks_api.generated.processedorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.processedorders.Configuration(
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
with linnworks_api.generated.processedorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.processedorders.ProcessedOrdersApi(api_client)
    processed_orders_refund_shipping_request = linnworks_api.generated.processedorders.ProcessedOrdersRefundShippingRequest() # ProcessedOrdersRefundShippingRequest | 

    try:
        # RefundShipping
        api_response = api_instance.refund_shipping(processed_orders_refund_shipping_request)
        print("The response of ProcessedOrdersApi->refund_shipping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessedOrdersApi->refund_shipping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processed_orders_refund_shipping_request** | [**ProcessedOrdersRefundShippingRequest**](ProcessedOrdersRefundShippingRequest.md)|  | 

### Return type

[**List[RefundInfo]**](RefundInfo.md)

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

# **rename_return_category**
> rename_return_category(processed_orders_rename_return_category_request)

RenameReturnCategory

Use this call to rename an existing return category. <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.processedorders
from linnworks_api.generated.processedorders.models.processed_orders_rename_return_category_request import ProcessedOrdersRenameReturnCategoryRequest
from linnworks_api.generated.processedorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.processedorders.Configuration(
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
with linnworks_api.generated.processedorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.processedorders.ProcessedOrdersApi(api_client)
    processed_orders_rename_return_category_request = linnworks_api.generated.processedorders.ProcessedOrdersRenameReturnCategoryRequest() # ProcessedOrdersRenameReturnCategoryRequest | 

    try:
        # RenameReturnCategory
        api_instance.rename_return_category(processed_orders_rename_return_category_request)
    except Exception as e:
        print("Exception when calling ProcessedOrdersApi->rename_return_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processed_orders_rename_return_category_request** | [**ProcessedOrdersRenameReturnCategoryRequest**](ProcessedOrdersRenameReturnCategoryRequest.md)|  | 

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

# **search_processed_orders**
> SearchProcessedOrdersResponse search_processed_orders(processed_orders_search_processed_orders_request)

SearchProcessedOrders

Search Processed Orders <b>Permissions Required: </b> GlobalPermissions.OrderBook.ProcessedOrdersNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.processedorders
from linnworks_api.generated.processedorders.models.processed_orders_search_processed_orders_request import ProcessedOrdersSearchProcessedOrdersRequest
from linnworks_api.generated.processedorders.models.search_processed_orders_response import SearchProcessedOrdersResponse
from linnworks_api.generated.processedorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.processedorders.Configuration(
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
with linnworks_api.generated.processedorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.processedorders.ProcessedOrdersApi(api_client)
    processed_orders_search_processed_orders_request = linnworks_api.generated.processedorders.ProcessedOrdersSearchProcessedOrdersRequest() # ProcessedOrdersSearchProcessedOrdersRequest | 

    try:
        # SearchProcessedOrders
        api_response = api_instance.search_processed_orders(processed_orders_search_processed_orders_request)
        print("The response of ProcessedOrdersApi->search_processed_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessedOrdersApi->search_processed_orders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processed_orders_search_processed_orders_request** | [**ProcessedOrdersSearchProcessedOrdersRequest**](ProcessedOrdersSearchProcessedOrdersRequest.md)|  | 

### Return type

[**SearchProcessedOrdersResponse**](SearchProcessedOrdersResponse.md)

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

# **search_processed_orders_paged**
> GenericPagedResultProcessedOrderWeb search_processed_orders_paged(processed_orders_search_processed_orders_paged_request)

SearchProcessedOrdersPaged

Use this call to search for processed orders. <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.processedorders
from linnworks_api.generated.processedorders.models.generic_paged_result_processed_order_web import GenericPagedResultProcessedOrderWeb
from linnworks_api.generated.processedorders.models.processed_orders_search_processed_orders_paged_request import ProcessedOrdersSearchProcessedOrdersPagedRequest
from linnworks_api.generated.processedorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.processedorders.Configuration(
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
with linnworks_api.generated.processedorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.processedorders.ProcessedOrdersApi(api_client)
    processed_orders_search_processed_orders_paged_request = linnworks_api.generated.processedorders.ProcessedOrdersSearchProcessedOrdersPagedRequest() # ProcessedOrdersSearchProcessedOrdersPagedRequest | 

    try:
        # SearchProcessedOrdersPaged
        api_response = api_instance.search_processed_orders_paged(processed_orders_search_processed_orders_paged_request)
        print("The response of ProcessedOrdersApi->search_processed_orders_paged:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessedOrdersApi->search_processed_orders_paged: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processed_orders_search_processed_orders_paged_request** | [**ProcessedOrdersSearchProcessedOrdersPagedRequest**](ProcessedOrdersSearchProcessedOrdersPagedRequest.md)|  | 

### Return type

[**GenericPagedResultProcessedOrderWeb**](GenericPagedResultProcessedOrderWeb.md)

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

# **validate_complete_order_refund**
> ValidationResult validate_complete_order_refund(processed_orders_validate_complete_order_refund_request)

ValidateCompleteOrderRefund

Use this call to check if it is possible to do an automated full-order refund. <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.processedorders
from linnworks_api.generated.processedorders.models.processed_orders_validate_complete_order_refund_request import ProcessedOrdersValidateCompleteOrderRefundRequest
from linnworks_api.generated.processedorders.models.validation_result import ValidationResult
from linnworks_api.generated.processedorders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.processedorders.Configuration(
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
with linnworks_api.generated.processedorders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.processedorders.ProcessedOrdersApi(api_client)
    processed_orders_validate_complete_order_refund_request = linnworks_api.generated.processedorders.ProcessedOrdersValidateCompleteOrderRefundRequest() # ProcessedOrdersValidateCompleteOrderRefundRequest | 

    try:
        # ValidateCompleteOrderRefund
        api_response = api_instance.validate_complete_order_refund(processed_orders_validate_complete_order_refund_request)
        print("The response of ProcessedOrdersApi->validate_complete_order_refund:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessedOrdersApi->validate_complete_order_refund: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processed_orders_validate_complete_order_refund_request** | [**ProcessedOrdersValidateCompleteOrderRefundRequest**](ProcessedOrdersValidateCompleteOrderRefundRequest.md)|  | 

### Return type

[**ValidationResult**](ValidationResult.md)

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

