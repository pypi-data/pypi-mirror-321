# linnworks_api.generated.warehousetransfer_new.StockItemApi

All URIs are relative to *https://eu-api.linnworks.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**warehousetransfer_stock_find_warehouse_transfer_stock_items_get**](StockItemApi.md#warehousetransfer_stock_find_warehouse_transfer_stock_items_get) | **GET** /warehousetransfer/stock/FindWarehouseTransferStockItems | FindWarehouseTransferStockItems
[**warehousetransfer_stock_get**](StockItemApi.md#warehousetransfer_stock_get) | **GET** /warehousetransfer/stock | FindStockItem


# **warehousetransfer_stock_find_warehouse_transfer_stock_items_get**
> WarehouseTransferStockItemModelGenericPagedResult warehousetransfer_stock_find_warehouse_transfer_stock_items_get(keyword=keyword, from_location_id=from_location_id, to_location_id=to_location_id, entries_per_page=entries_per_page, page_number=page_number, sort_column=sort_column, sort_direction=sort_direction)

FindWarehouseTransferStockItems

Used to get stock items for warehouse transfer

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.warehouse_transfer_stock_item_model_generic_paged_result import WarehouseTransferStockItemModelGenericPagedResult
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
    api_instance = linnworks_api.generated.warehousetransfer_new.StockItemApi(api_client)
    keyword = 'keyword_example' # str |  (optional)
    from_location_id = 'from_location_id_example' # str |  (optional)
    to_location_id = 'to_location_id_example' # str |  (optional)
    entries_per_page = 56 # int |  (optional)
    page_number = 56 # int |  (optional)
    sort_column = 'sort_column_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)

    try:
        # FindWarehouseTransferStockItems
        api_response = api_instance.warehousetransfer_stock_find_warehouse_transfer_stock_items_get(keyword=keyword, from_location_id=from_location_id, to_location_id=to_location_id, entries_per_page=entries_per_page, page_number=page_number, sort_column=sort_column, sort_direction=sort_direction)
        print("The response of StockItemApi->warehousetransfer_stock_find_warehouse_transfer_stock_items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StockItemApi->warehousetransfer_stock_find_warehouse_transfer_stock_items_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyword** | **str**|  | [optional] 
 **from_location_id** | **str**|  | [optional] 
 **to_location_id** | **str**|  | [optional] 
 **entries_per_page** | **int**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **sort_column** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 

### Return type

[**WarehouseTransferStockItemModelGenericPagedResult**](WarehouseTransferStockItemModelGenericPagedResult.md)

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

# **warehousetransfer_stock_get**
> StockItemModelGenericPagedResult warehousetransfer_stock_get(keyword=keyword, from_location_id=from_location_id, channel_id=channel_id, sort_column=sort_column, sort_direction=sort_direction, entries_per_page=entries_per_page, page_number=page_number)

FindStockItem

Used to get shipment items by shipping plan id

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.stock_item_model_generic_paged_result import StockItemModelGenericPagedResult
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
    api_instance = linnworks_api.generated.warehousetransfer_new.StockItemApi(api_client)
    keyword = 'keyword_example' # str |  (optional)
    from_location_id = 'from_location_id_example' # str |  (optional)
    channel_id = 56 # int |  (optional)
    sort_column = 'sort_column_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    entries_per_page = 56 # int |  (optional)
    page_number = 56 # int |  (optional)

    try:
        # FindStockItem
        api_response = api_instance.warehousetransfer_stock_get(keyword=keyword, from_location_id=from_location_id, channel_id=channel_id, sort_column=sort_column, sort_direction=sort_direction, entries_per_page=entries_per_page, page_number=page_number)
        print("The response of StockItemApi->warehousetransfer_stock_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StockItemApi->warehousetransfer_stock_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyword** | **str**|  | [optional] 
 **from_location_id** | **str**|  | [optional] 
 **channel_id** | **int**|  | [optional] 
 **sort_column** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **entries_per_page** | **int**|  | [optional] 
 **page_number** | **int**|  | [optional] 

### Return type

[**StockItemModelGenericPagedResult**](StockItemModelGenericPagedResult.md)

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

