# linnworks_api.generated.warehousetransfer_new.WarehouseTransferApi

All URIs are relative to *https://eu-api.linnworks.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**warehousetransfer_transfers_add_item_batches_post**](WarehouseTransferApi.md#warehousetransfer_transfers_add_item_batches_post) | **POST** /warehousetransfer/transfers/AddItemBatches | 
[**warehousetransfer_transfers_add_item_put**](WarehouseTransferApi.md#warehousetransfer_transfers_add_item_put) | **PUT** /warehousetransfer/transfers/AddItem | 
[**warehousetransfer_transfers_add_item_received_batches_post**](WarehouseTransferApi.md#warehousetransfer_transfers_add_item_received_batches_post) | **POST** /warehousetransfer/transfers/AddItemReceivedBatches | 
[**warehousetransfer_transfers_add_items_in_bulk_post**](WarehouseTransferApi.md#warehousetransfer_transfers_add_items_in_bulk_post) | **POST** /warehousetransfer/transfers/AddItemsInBulk | 
[**warehousetransfer_transfers_archive_warehouse_transfer_put**](WarehouseTransferApi.md#warehousetransfer_transfers_archive_warehouse_transfer_put) | **PUT** /warehousetransfer/transfers/ArchiveWarehouseTransfer | 
[**warehousetransfer_transfers_check_for_draft_transfer_put**](WarehouseTransferApi.md#warehousetransfer_transfers_check_for_draft_transfer_put) | **PUT** /warehousetransfer/transfers/CheckForDraftTransfer | 
[**warehousetransfer_transfers_create_transfer_post**](WarehouseTransferApi.md#warehousetransfer_transfers_create_transfer_post) | **POST** /warehousetransfer/transfers/CreateTransfer | 
[**warehousetransfer_transfers_delete_items_delete**](WarehouseTransferApi.md#warehousetransfer_transfers_delete_items_delete) | **DELETE** /warehousetransfer/transfers/DeleteItems | 
[**warehousetransfer_transfers_delete_warehouse_transfer_delete**](WarehouseTransferApi.md#warehousetransfer_transfers_delete_warehouse_transfer_delete) | **DELETE** /warehousetransfer/transfers/DeleteWarehouseTransfer | 
[**warehousetransfer_transfers_get_list_transfers_get**](WarehouseTransferApi.md#warehousetransfer_transfers_get_list_transfers_get) | **GET** /warehousetransfer/transfers/GetListTransfers | 
[**warehousetransfer_transfers_get_transfer_cards_by_location_get**](WarehouseTransferApi.md#warehousetransfer_transfers_get_transfer_cards_by_location_get) | **GET** /warehousetransfer/transfers/GetTransferCardsByLocation | 
[**warehousetransfer_transfers_get_transfer_cards_get**](WarehouseTransferApi.md#warehousetransfer_transfers_get_transfer_cards_get) | **GET** /warehousetransfer/transfers/GetTransferCards | 
[**warehousetransfer_transfers_get_transfer_item_batches_transfer_id_get**](WarehouseTransferApi.md#warehousetransfer_transfers_get_transfer_item_batches_transfer_id_get) | **GET** /warehousetransfer/transfers/GetTransferItemBatches/{transferId} | 
[**warehousetransfer_transfers_get_transfer_items_put**](WarehouseTransferApi.md#warehousetransfer_transfers_get_transfer_items_put) | **PUT** /warehousetransfer/transfers/GetTransferItems | 
[**warehousetransfer_transfers_receive_selected_transfer_items_for_wms_post**](WarehouseTransferApi.md#warehousetransfer_transfers_receive_selected_transfer_items_for_wms_post) | **POST** /warehousetransfer/transfers/ReceiveSelectedTransferItemsForWMS | 
[**warehousetransfer_transfers_update_from_location_put**](WarehouseTransferApi.md#warehousetransfer_transfers_update_from_location_put) | **PUT** /warehousetransfer/transfers/UpdateFromLocation | 
[**warehousetransfer_transfers_update_item_received_quantity_put**](WarehouseTransferApi.md#warehousetransfer_transfers_update_item_received_quantity_put) | **PUT** /warehousetransfer/transfers/UpdateItemReceivedQuantity | 
[**warehousetransfer_transfers_update_item_requested_quantity_put**](WarehouseTransferApi.md#warehousetransfer_transfers_update_item_requested_quantity_put) | **PUT** /warehousetransfer/transfers/UpdateItemRequestedQuantity | 
[**warehousetransfer_transfers_update_item_sent_quantity_put**](WarehouseTransferApi.md#warehousetransfer_transfers_update_item_sent_quantity_put) | **PUT** /warehousetransfer/transfers/UpdateItemSentQuantity | 
[**warehousetransfer_transfers_update_status_put**](WarehouseTransferApi.md#warehousetransfer_transfers_update_status_put) | **PUT** /warehousetransfer/transfers/UpdateStatus | 
[**warehousetransfer_transfers_update_to_location_put**](WarehouseTransferApi.md#warehousetransfer_transfers_update_to_location_put) | **PUT** /warehousetransfer/transfers/UpdateToLocation | 


# **warehousetransfer_transfers_add_item_batches_post**
> bool warehousetransfer_transfers_add_item_batches_post(add_item_batches_request=add_item_batches_request)



### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.add_item_batches_request import AddItemBatchesRequest
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
    api_instance = linnworks_api.generated.warehousetransfer_new.WarehouseTransferApi(api_client)
    add_item_batches_request = linnworks_api.generated.warehousetransfer_new.AddItemBatchesRequest() # AddItemBatchesRequest |  (optional)

    try:
        api_response = api_instance.warehousetransfer_transfers_add_item_batches_post(add_item_batches_request=add_item_batches_request)
        print("The response of WarehouseTransferApi->warehousetransfer_transfers_add_item_batches_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehouseTransferApi->warehousetransfer_transfers_add_item_batches_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_item_batches_request** | [**AddItemBatchesRequest**](AddItemBatchesRequest.md)|  | [optional] 

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
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehousetransfer_transfers_add_item_put**
> TransferItemViewModel warehousetransfer_transfers_add_item_put(add_item_request=add_item_request)



Use this call to add an item to the stock transfer (only works for transfers in draft/request states)

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.add_item_request import AddItemRequest
from linnworks_api.generated.warehousetransfer_new.models.transfer_item_view_model import TransferItemViewModel
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
    api_instance = linnworks_api.generated.warehousetransfer_new.WarehouseTransferApi(api_client)
    add_item_request = linnworks_api.generated.warehousetransfer_new.AddItemRequest() # AddItemRequest |  (optional)

    try:
        api_response = api_instance.warehousetransfer_transfers_add_item_put(add_item_request=add_item_request)
        print("The response of WarehouseTransferApi->warehousetransfer_transfers_add_item_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehouseTransferApi->warehousetransfer_transfers_add_item_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_item_request** | [**AddItemRequest**](AddItemRequest.md)|  | [optional] 

### Return type

[**TransferItemViewModel**](TransferItemViewModel.md)

### Authorization

[Linnworks](../README.md#Linnworks)

### HTTP request headers

 - **Content-Type**: application/json-patch+json; x-api-version=1.0, application/json; x-api-version=1.0, text/json; x-api-version=1.0, application/*+json; x-api-version=1.0
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehousetransfer_transfers_add_item_received_batches_post**
> bool warehousetransfer_transfers_add_item_received_batches_post(add_item_received_batches_request=add_item_received_batches_request)



### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.add_item_received_batches_request import AddItemReceivedBatchesRequest
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
    api_instance = linnworks_api.generated.warehousetransfer_new.WarehouseTransferApi(api_client)
    add_item_received_batches_request = linnworks_api.generated.warehousetransfer_new.AddItemReceivedBatchesRequest() # AddItemReceivedBatchesRequest |  (optional)

    try:
        api_response = api_instance.warehousetransfer_transfers_add_item_received_batches_post(add_item_received_batches_request=add_item_received_batches_request)
        print("The response of WarehouseTransferApi->warehousetransfer_transfers_add_item_received_batches_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehouseTransferApi->warehousetransfer_transfers_add_item_received_batches_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_item_received_batches_request** | [**AddItemReceivedBatchesRequest**](AddItemReceivedBatchesRequest.md)|  | [optional] 

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
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehousetransfer_transfers_add_items_in_bulk_post**
> bool warehousetransfer_transfers_add_items_in_bulk_post(add_items_in_bulk_request=add_items_in_bulk_request)



### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.add_items_in_bulk_request import AddItemsInBulkRequest
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
    api_instance = linnworks_api.generated.warehousetransfer_new.WarehouseTransferApi(api_client)
    add_items_in_bulk_request = linnworks_api.generated.warehousetransfer_new.AddItemsInBulkRequest() # AddItemsInBulkRequest |  (optional)

    try:
        api_response = api_instance.warehousetransfer_transfers_add_items_in_bulk_post(add_items_in_bulk_request=add_items_in_bulk_request)
        print("The response of WarehouseTransferApi->warehousetransfer_transfers_add_items_in_bulk_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehouseTransferApi->warehousetransfer_transfers_add_items_in_bulk_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_items_in_bulk_request** | [**AddItemsInBulkRequest**](AddItemsInBulkRequest.md)|  | [optional] 

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
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehousetransfer_transfers_archive_warehouse_transfer_put**
> int warehousetransfer_transfers_archive_warehouse_transfer_put(archive_transfer_request=archive_transfer_request)



### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.archive_transfer_request import ArchiveTransferRequest
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
    api_instance = linnworks_api.generated.warehousetransfer_new.WarehouseTransferApi(api_client)
    archive_transfer_request = linnworks_api.generated.warehousetransfer_new.ArchiveTransferRequest() # ArchiveTransferRequest |  (optional)

    try:
        api_response = api_instance.warehousetransfer_transfers_archive_warehouse_transfer_put(archive_transfer_request=archive_transfer_request)
        print("The response of WarehouseTransferApi->warehousetransfer_transfers_archive_warehouse_transfer_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehouseTransferApi->warehousetransfer_transfers_archive_warehouse_transfer_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **archive_transfer_request** | [**ArchiveTransferRequest**](ArchiveTransferRequest.md)|  | [optional] 

### Return type

**int**

### Authorization

[Linnworks](../README.md#Linnworks)

### HTTP request headers

 - **Content-Type**: application/json-patch+json; x-api-version=1.0, application/json; x-api-version=1.0, text/json; x-api-version=1.0, application/*+json; x-api-version=1.0
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehousetransfer_transfers_check_for_draft_transfer_put**
> int warehousetransfer_transfers_check_for_draft_transfer_put(check_for_draft_transfer_request=check_for_draft_transfer_request)



Use this call to see if a draft transfer already exists for the two locations

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.check_for_draft_transfer_request import CheckForDraftTransferRequest
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
    api_instance = linnworks_api.generated.warehousetransfer_new.WarehouseTransferApi(api_client)
    check_for_draft_transfer_request = linnworks_api.generated.warehousetransfer_new.CheckForDraftTransferRequest() # CheckForDraftTransferRequest |  (optional)

    try:
        api_response = api_instance.warehousetransfer_transfers_check_for_draft_transfer_put(check_for_draft_transfer_request=check_for_draft_transfer_request)
        print("The response of WarehouseTransferApi->warehousetransfer_transfers_check_for_draft_transfer_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehouseTransferApi->warehousetransfer_transfers_check_for_draft_transfer_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_for_draft_transfer_request** | [**CheckForDraftTransferRequest**](CheckForDraftTransferRequest.md)|  | [optional] 

### Return type

**int**

### Authorization

[Linnworks](../README.md#Linnworks)

### HTTP request headers

 - **Content-Type**: application/json-patch+json; x-api-version=1.0, application/json; x-api-version=1.0, text/json; x-api-version=1.0, application/*+json; x-api-version=1.0
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehousetransfer_transfers_create_transfer_post**
> WarehouseTransferViewModel warehousetransfer_transfers_create_transfer_post(create_transfer_request=create_transfer_request)



Use this call to create a new transfer request with default reference number

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.create_transfer_request import CreateTransferRequest
from linnworks_api.generated.warehousetransfer_new.models.warehouse_transfer_view_model import WarehouseTransferViewModel
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
    api_instance = linnworks_api.generated.warehousetransfer_new.WarehouseTransferApi(api_client)
    create_transfer_request = linnworks_api.generated.warehousetransfer_new.CreateTransferRequest() # CreateTransferRequest |  (optional)

    try:
        api_response = api_instance.warehousetransfer_transfers_create_transfer_post(create_transfer_request=create_transfer_request)
        print("The response of WarehouseTransferApi->warehousetransfer_transfers_create_transfer_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehouseTransferApi->warehousetransfer_transfers_create_transfer_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_transfer_request** | [**CreateTransferRequest**](CreateTransferRequest.md)|  | [optional] 

### Return type

[**WarehouseTransferViewModel**](WarehouseTransferViewModel.md)

### Authorization

[Linnworks](../README.md#Linnworks)

### HTTP request headers

 - **Content-Type**: application/json-patch+json; x-api-version=1.0, application/json; x-api-version=1.0, text/json; x-api-version=1.0, application/*+json; x-api-version=1.0
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehousetransfer_transfers_delete_items_delete**
> int warehousetransfer_transfers_delete_items_delete(delete_items_request=delete_items_request)



Use this call to remove items from a stock transfer.

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.delete_items_request import DeleteItemsRequest
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
    api_instance = linnworks_api.generated.warehousetransfer_new.WarehouseTransferApi(api_client)
    delete_items_request = linnworks_api.generated.warehousetransfer_new.DeleteItemsRequest() # DeleteItemsRequest |  (optional)

    try:
        api_response = api_instance.warehousetransfer_transfers_delete_items_delete(delete_items_request=delete_items_request)
        print("The response of WarehouseTransferApi->warehousetransfer_transfers_delete_items_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehouseTransferApi->warehousetransfer_transfers_delete_items_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_items_request** | [**DeleteItemsRequest**](DeleteItemsRequest.md)|  | [optional] 

### Return type

**int**

### Authorization

[Linnworks](../README.md#Linnworks)

### HTTP request headers

 - **Content-Type**: application/json-patch+json; x-api-version=1.0, application/json; x-api-version=1.0, text/json; x-api-version=1.0, application/*+json; x-api-version=1.0
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehousetransfer_transfers_delete_warehouse_transfer_delete**
> int warehousetransfer_transfers_delete_warehouse_transfer_delete(delete_transfer_request=delete_transfer_request)



Use this call to delete a stock transfer

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.delete_transfer_request import DeleteTransferRequest
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
    api_instance = linnworks_api.generated.warehousetransfer_new.WarehouseTransferApi(api_client)
    delete_transfer_request = linnworks_api.generated.warehousetransfer_new.DeleteTransferRequest() # DeleteTransferRequest |  (optional)

    try:
        api_response = api_instance.warehousetransfer_transfers_delete_warehouse_transfer_delete(delete_transfer_request=delete_transfer_request)
        print("The response of WarehouseTransferApi->warehousetransfer_transfers_delete_warehouse_transfer_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehouseTransferApi->warehousetransfer_transfers_delete_warehouse_transfer_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_transfer_request** | [**DeleteTransferRequest**](DeleteTransferRequest.md)|  | [optional] 

### Return type

**int**

### Authorization

[Linnworks](../README.md#Linnworks)

### HTTP request headers

 - **Content-Type**: application/json-patch+json; x-api-version=1.0, application/json; x-api-version=1.0, text/json; x-api-version=1.0, application/*+json; x-api-version=1.0
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehousetransfer_transfers_get_list_transfers_get**
> WarehouseTransferViewModel warehousetransfer_transfers_get_list_transfers_get(ids=ids)



Use this call to retrieve a list of items on  the order and request/sent/received levels. This method will return multiple entries for a single item if the item exists in multiple bins.

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.warehouse_transfer_view_model import WarehouseTransferViewModel
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
    api_instance = linnworks_api.generated.warehousetransfer_new.WarehouseTransferApi(api_client)
    ids = [56] # List[int] | The Ids to load (optional)

    try:
        api_response = api_instance.warehousetransfer_transfers_get_list_transfers_get(ids=ids)
        print("The response of WarehouseTransferApi->warehousetransfer_transfers_get_list_transfers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehouseTransferApi->warehousetransfer_transfers_get_list_transfers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**List[int]**](int.md)| The Ids to load | [optional] 

### Return type

[**WarehouseTransferViewModel**](WarehouseTransferViewModel.md)

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
**405** | Method Not Allowed |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehousetransfer_transfers_get_transfer_cards_by_location_get**
> WarehouseTransferViewModel warehousetransfer_transfers_get_transfer_cards_by_location_get(location_id=location_id)



### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.warehouse_transfer_view_model import WarehouseTransferViewModel
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
    api_instance = linnworks_api.generated.warehousetransfer_new.WarehouseTransferApi(api_client)
    location_id = 'location_id_example' # str |  (optional)

    try:
        api_response = api_instance.warehousetransfer_transfers_get_transfer_cards_by_location_get(location_id=location_id)
        print("The response of WarehouseTransferApi->warehousetransfer_transfers_get_transfer_cards_by_location_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehouseTransferApi->warehousetransfer_transfers_get_transfer_cards_by_location_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **str**|  | [optional] 

### Return type

[**WarehouseTransferViewModel**](WarehouseTransferViewModel.md)

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
**405** | Method Not Allowed |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehousetransfer_transfers_get_transfer_cards_get**
> WarehouseTransferViewModel warehousetransfer_transfers_get_transfer_cards_get()



Getting all warehouse transfers with stock item details for searching

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.warehouse_transfer_view_model import WarehouseTransferViewModel
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
    api_instance = linnworks_api.generated.warehousetransfer_new.WarehouseTransferApi(api_client)

    try:
        api_response = api_instance.warehousetransfer_transfers_get_transfer_cards_get()
        print("The response of WarehouseTransferApi->warehousetransfer_transfers_get_transfer_cards_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehouseTransferApi->warehousetransfer_transfers_get_transfer_cards_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WarehouseTransferViewModel**](WarehouseTransferViewModel.md)

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
**405** | Method Not Allowed |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehousetransfer_transfers_get_transfer_item_batches_transfer_id_get**
> GetBatchesByWarehouseTransferIdResponse warehousetransfer_transfers_get_transfer_item_batches_transfer_id_get(transfer_id, stock_item_ids=stock_item_ids, location_type=location_type)



### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.get_batches_by_warehouse_transfer_id_response import GetBatchesByWarehouseTransferIdResponse
from linnworks_api.generated.warehousetransfer_new.models.transfer_location_type import TransferLocationType
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
    api_instance = linnworks_api.generated.warehousetransfer_new.WarehouseTransferApi(api_client)
    transfer_id = 56 # int | 
    stock_item_ids = [56] # List[int] |  (optional)
    location_type = linnworks_api.generated.warehousetransfer_new.TransferLocationType() # TransferLocationType |  (optional)

    try:
        api_response = api_instance.warehousetransfer_transfers_get_transfer_item_batches_transfer_id_get(transfer_id, stock_item_ids=stock_item_ids, location_type=location_type)
        print("The response of WarehouseTransferApi->warehousetransfer_transfers_get_transfer_item_batches_transfer_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehouseTransferApi->warehousetransfer_transfers_get_transfer_item_batches_transfer_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_id** | **int**|  | 
 **stock_item_ids** | [**List[int]**](int.md)|  | [optional] 
 **location_type** | [**TransferLocationType**](.md)|  | [optional] 

### Return type

[**GetBatchesByWarehouseTransferIdResponse**](GetBatchesByWarehouseTransferIdResponse.md)

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
**405** | Method Not Allowed |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehousetransfer_transfers_get_transfer_items_put**
> TransferItemViewModel warehousetransfer_transfers_get_transfer_items_put(pk_transfer_id=pk_transfer_id)



Getting warehouse transfers for appropriate location with stock item details for searching

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.transfer_item_view_model import TransferItemViewModel
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
    api_instance = linnworks_api.generated.warehousetransfer_new.WarehouseTransferApi(api_client)
    pk_transfer_id = 56 # int | pkTransferId for transfer requiring status change (optional)

    try:
        api_response = api_instance.warehousetransfer_transfers_get_transfer_items_put(pk_transfer_id=pk_transfer_id)
        print("The response of WarehouseTransferApi->warehousetransfer_transfers_get_transfer_items_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehouseTransferApi->warehousetransfer_transfers_get_transfer_items_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pk_transfer_id** | **int**| pkTransferId for transfer requiring status change | [optional] 

### Return type

[**TransferItemViewModel**](TransferItemViewModel.md)

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
**405** | Method Not Allowed |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehousetransfer_transfers_receive_selected_transfer_items_for_wms_post**
> WarehousetransferTransfersReceiveSelectedTransferItemsForWMSPost200Response warehousetransfer_transfers_receive_selected_transfer_items_for_wms_post(receive_selected_transfer_items_for_wms_request=receive_selected_transfer_items_for_wms_request)



Use this call to update transfer item receive quantity with the sent quantity for WMS location

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.receive_selected_transfer_items_for_wms_request import ReceiveSelectedTransferItemsForWmsRequest
from linnworks_api.generated.warehousetransfer_new.models.warehousetransfer_transfers_receive_selected_transfer_items_for_wms_post200_response import WarehousetransferTransfersReceiveSelectedTransferItemsForWMSPost200Response
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
    api_instance = linnworks_api.generated.warehousetransfer_new.WarehouseTransferApi(api_client)
    receive_selected_transfer_items_for_wms_request = linnworks_api.generated.warehousetransfer_new.ReceiveSelectedTransferItemsForWmsRequest() # ReceiveSelectedTransferItemsForWmsRequest |  (optional)

    try:
        api_response = api_instance.warehousetransfer_transfers_receive_selected_transfer_items_for_wms_post(receive_selected_transfer_items_for_wms_request=receive_selected_transfer_items_for_wms_request)
        print("The response of WarehouseTransferApi->warehousetransfer_transfers_receive_selected_transfer_items_for_wms_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehouseTransferApi->warehousetransfer_transfers_receive_selected_transfer_items_for_wms_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receive_selected_transfer_items_for_wms_request** | [**ReceiveSelectedTransferItemsForWmsRequest**](ReceiveSelectedTransferItemsForWmsRequest.md)|  | [optional] 

### Return type

[**WarehousetransferTransfersReceiveSelectedTransferItemsForWMSPost200Response**](WarehousetransferTransfersReceiveSelectedTransferItemsForWMSPost200Response.md)

### Authorization

[Linnworks](../README.md#Linnworks)

### HTTP request headers

 - **Content-Type**: application/json-patch+json; x-api-version=1.0, application/json; x-api-version=1.0, text/json; x-api-version=1.0, application/*+json; x-api-version=1.0
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehousetransfer_transfers_update_from_location_put**
> int warehousetransfer_transfers_update_from_location_put(update_from_location_request=update_from_location_request)



Use this call to update the from location of a transfer.

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.update_from_location_request import UpdateFromLocationRequest
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
    api_instance = linnworks_api.generated.warehousetransfer_new.WarehouseTransferApi(api_client)
    update_from_location_request = linnworks_api.generated.warehousetransfer_new.UpdateFromLocationRequest() # UpdateFromLocationRequest |  (optional)

    try:
        api_response = api_instance.warehousetransfer_transfers_update_from_location_put(update_from_location_request=update_from_location_request)
        print("The response of WarehouseTransferApi->warehousetransfer_transfers_update_from_location_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehouseTransferApi->warehousetransfer_transfers_update_from_location_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_from_location_request** | [**UpdateFromLocationRequest**](UpdateFromLocationRequest.md)|  | [optional] 

### Return type

**int**

### Authorization

[Linnworks](../README.md#Linnworks)

### HTTP request headers

 - **Content-Type**: application/json-patch+json; x-api-version=1.0, application/json; x-api-version=1.0, text/json; x-api-version=1.0, application/*+json; x-api-version=1.0
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehousetransfer_transfers_update_item_received_quantity_put**
> int warehousetransfer_transfers_update_item_received_quantity_put(update_item_received_quantity_request=update_item_received_quantity_request)



Use this call to change the received quantity of a stock transfer item, adjusting stock levels.

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.update_item_received_quantity_request import UpdateItemReceivedQuantityRequest
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
    api_instance = linnworks_api.generated.warehousetransfer_new.WarehouseTransferApi(api_client)
    update_item_received_quantity_request = linnworks_api.generated.warehousetransfer_new.UpdateItemReceivedQuantityRequest() # UpdateItemReceivedQuantityRequest |  (optional)

    try:
        api_response = api_instance.warehousetransfer_transfers_update_item_received_quantity_put(update_item_received_quantity_request=update_item_received_quantity_request)
        print("The response of WarehouseTransferApi->warehousetransfer_transfers_update_item_received_quantity_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehouseTransferApi->warehousetransfer_transfers_update_item_received_quantity_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_item_received_quantity_request** | [**UpdateItemReceivedQuantityRequest**](UpdateItemReceivedQuantityRequest.md)|  | [optional] 

### Return type

**int**

### Authorization

[Linnworks](../README.md#Linnworks)

### HTTP request headers

 - **Content-Type**: application/json-patch+json; x-api-version=1.0, application/json; x-api-version=1.0, text/json; x-api-version=1.0, application/*+json; x-api-version=1.0
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehousetransfer_transfers_update_item_requested_quantity_put**
> int warehousetransfer_transfers_update_item_requested_quantity_put(update_item_requested_quantity_request=update_item_requested_quantity_request)



Use this call to change the received quantity of a stock transfer item, adjusting stock levels.

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.update_item_requested_quantity_request import UpdateItemRequestedQuantityRequest
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
    api_instance = linnworks_api.generated.warehousetransfer_new.WarehouseTransferApi(api_client)
    update_item_requested_quantity_request = linnworks_api.generated.warehousetransfer_new.UpdateItemRequestedQuantityRequest() # UpdateItemRequestedQuantityRequest |  (optional)

    try:
        api_response = api_instance.warehousetransfer_transfers_update_item_requested_quantity_put(update_item_requested_quantity_request=update_item_requested_quantity_request)
        print("The response of WarehouseTransferApi->warehousetransfer_transfers_update_item_requested_quantity_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehouseTransferApi->warehousetransfer_transfers_update_item_requested_quantity_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_item_requested_quantity_request** | [**UpdateItemRequestedQuantityRequest**](UpdateItemRequestedQuantityRequest.md)|  | [optional] 

### Return type

**int**

### Authorization

[Linnworks](../README.md#Linnworks)

### HTTP request headers

 - **Content-Type**: application/json-patch+json; x-api-version=1.0, application/json; x-api-version=1.0, text/json; x-api-version=1.0, application/*+json; x-api-version=1.0
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehousetransfer_transfers_update_item_sent_quantity_put**
> bool warehousetransfer_transfers_update_item_sent_quantity_put(update_item_sent_quantity_request=update_item_sent_quantity_request)



Use this call to change the sent quantity of a stock transfer item, adjusting stock levels.

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.update_item_sent_quantity_request import UpdateItemSentQuantityRequest
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
    api_instance = linnworks_api.generated.warehousetransfer_new.WarehouseTransferApi(api_client)
    update_item_sent_quantity_request = linnworks_api.generated.warehousetransfer_new.UpdateItemSentQuantityRequest() # UpdateItemSentQuantityRequest |  (optional)

    try:
        api_response = api_instance.warehousetransfer_transfers_update_item_sent_quantity_put(update_item_sent_quantity_request=update_item_sent_quantity_request)
        print("The response of WarehouseTransferApi->warehousetransfer_transfers_update_item_sent_quantity_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehouseTransferApi->warehousetransfer_transfers_update_item_sent_quantity_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_item_sent_quantity_request** | [**UpdateItemSentQuantityRequest**](UpdateItemSentQuantityRequest.md)|  | [optional] 

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
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehousetransfer_transfers_update_status_put**
> int warehousetransfer_transfers_update_status_put(update_status_request=update_status_request)



Use this call to change a transfers status

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.update_status_request import UpdateStatusRequest
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
    api_instance = linnworks_api.generated.warehousetransfer_new.WarehouseTransferApi(api_client)
    update_status_request = linnworks_api.generated.warehousetransfer_new.UpdateStatusRequest() # UpdateStatusRequest |  (optional)

    try:
        api_response = api_instance.warehousetransfer_transfers_update_status_put(update_status_request=update_status_request)
        print("The response of WarehouseTransferApi->warehousetransfer_transfers_update_status_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehouseTransferApi->warehousetransfer_transfers_update_status_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_status_request** | [**UpdateStatusRequest**](UpdateStatusRequest.md)|  | [optional] 

### Return type

**int**

### Authorization

[Linnworks](../README.md#Linnworks)

### HTTP request headers

 - **Content-Type**: application/json-patch+json; x-api-version=1.0, application/json; x-api-version=1.0, text/json; x-api-version=1.0, application/*+json; x-api-version=1.0
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehousetransfer_transfers_update_to_location_put**
> int warehousetransfer_transfers_update_to_location_put(update_to_location_request=update_to_location_request)



Use this call to update the to location of a transfer.

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.update_to_location_request import UpdateToLocationRequest
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
    api_instance = linnworks_api.generated.warehousetransfer_new.WarehouseTransferApi(api_client)
    update_to_location_request = linnworks_api.generated.warehousetransfer_new.UpdateToLocationRequest() # UpdateToLocationRequest |  (optional)

    try:
        api_response = api_instance.warehousetransfer_transfers_update_to_location_put(update_to_location_request=update_to_location_request)
        print("The response of WarehouseTransferApi->warehousetransfer_transfers_update_to_location_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehouseTransferApi->warehousetransfer_transfers_update_to_location_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_to_location_request** | [**UpdateToLocationRequest**](UpdateToLocationRequest.md)|  | [optional] 

### Return type

**int**

### Authorization

[Linnworks](../README.md#Linnworks)

### HTTP request headers

 - **Content-Type**: application/json-patch+json; x-api-version=1.0, application/json; x-api-version=1.0, text/json; x-api-version=1.0, application/*+json; x-api-version=1.0
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

