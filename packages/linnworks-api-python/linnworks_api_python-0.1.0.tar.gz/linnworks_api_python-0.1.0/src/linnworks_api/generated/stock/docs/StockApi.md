# linnworks_api.generated.stock.StockApi

All URIs are relative to *https://eu-ext.linnworks.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_rolling_stock_take**](StockApi.md#add_rolling_stock_take) | **POST** /api/Stock/AddRollingStockTake | AddRollingStockTake
[**add_variation_items**](StockApi.md#add_variation_items) | **POST** /api/Stock/AddVariationItems | AddVariationItems
[**batch_stock_level_delta**](StockApi.md#batch_stock_level_delta) | **POST** /api/Stock/BatchStockLevelDelta | BatchStockLevelDelta
[**book_in_stock_batch**](StockApi.md#book_in_stock_batch) | **POST** /api/Stock/BookInStockBatch | BookInStockBatch
[**book_in_stock_item**](StockApi.md#book_in_stock_item) | **POST** /api/Stock/BookInStockItem | BookInStockItem
[**check_variation_parent_sku_exists**](StockApi.md#check_variation_parent_sku_exists) | **GET** /api/Stock/CheckVariationParentSKUExists | CheckVariationParentSKUExists
[**complete_warehouse_move**](StockApi.md#complete_warehouse_move) | **POST** /api/Stock/CompleteWarehouseMove | CompleteWarehouseMove
[**create_stock_batches**](StockApi.md#create_stock_batches) | **POST** /api/Stock/CreateStockBatches | CreateStockBatches
[**create_variation_group**](StockApi.md#create_variation_group) | **POST** /api/Stock/CreateVariationGroup | CreateVariationGroup
[**create_warehouse_move**](StockApi.md#create_warehouse_move) | **POST** /api/Stock/CreateWarehouseMove | CreateWarehouseMove
[**delete_move**](StockApi.md#delete_move) | **POST** /api/Stock/DeleteMove | DeleteMove
[**delete_variation_group**](StockApi.md#delete_variation_group) | **GET** /api/Stock/DeleteVariationGroup | DeleteVariationGroup
[**delete_variation_groups**](StockApi.md#delete_variation_groups) | **POST** /api/Stock/DeleteVariationGroups | DeleteVariationGroups
[**delete_variation_item**](StockApi.md#delete_variation_item) | **POST** /api/Stock/DeleteVariationItem | DeleteVariationItem
[**delete_variation_items**](StockApi.md#delete_variation_items) | **POST** /api/Stock/DeleteVariationItems | DeleteVariationItems
[**get_bin_racks_by_id**](StockApi.md#get_bin_racks_by_id) | **POST** /api/Stock/GetBinRacksById | GetBinRacksById
[**get_binrack_skus**](StockApi.md#get_binrack_skus) | **POST** /api/Stock/GetBinrackSkus | GetBinrackSkus
[**get_item_changes_history**](StockApi.md#get_item_changes_history) | **GET** /api/Stock/GetItemChangesHistory | GetItemChangesHistory
[**get_item_changes_history_csv**](StockApi.md#get_item_changes_history_csv) | **GET** /api/Stock/GetItemChangesHistoryCSV | GetItemChangesHistoryCSV
[**get_sold_stat**](StockApi.md#get_sold_stat) | **GET** /api/Stock/GetSoldStat | GetSoldStat
[**get_stock_consumption**](StockApi.md#get_stock_consumption) | **GET** /api/Stock/GetStockConsumption | GetStockConsumption
[**get_stock_due_po**](StockApi.md#get_stock_due_po) | **GET** /api/Stock/GetStockDuePO | GetStockDuePO
[**get_stock_item_return_stat**](StockApi.md#get_stock_item_return_stat) | **GET** /api/Stock/GetStockItemReturnStat | GetStockItemReturnStat
[**get_stock_item_scrap_stat**](StockApi.md#get_stock_item_scrap_stat) | **GET** /api/Stock/GetStockItemScrapStat | GetStockItemScrapStat
[**get_stock_item_type_info**](StockApi.md#get_stock_item_type_info) | **POST** /api/Stock/GetStockItemTypeInfo | GetStockItemTypeInfo
[**get_stock_items**](StockApi.md#get_stock_items) | **GET** /api/Stock/GetStockItems | GetStockItems
[**get_stock_items_by_ids**](StockApi.md#get_stock_items_by_ids) | **POST** /api/Stock/GetStockItemsByIds | GetStockItemsByIds
[**get_stock_items_by_key**](StockApi.md#get_stock_items_by_key) | **POST** /api/Stock/GetStockItemsByKey | GetStockItemsByKey
[**get_stock_items_full**](StockApi.md#get_stock_items_full) | **POST** /api/Stock/GetStockItemsFull | GetStockItemsFull
[**get_stock_items_full_by_ids**](StockApi.md#get_stock_items_full_by_ids) | **POST** /api/Stock/GetStockItemsFullByIds | GetStockItemsFullByIds
[**get_stock_items_location**](StockApi.md#get_stock_items_location) | **POST** /api/Stock/GetStockItemsLocation | GetStockItemsLocation
[**get_stock_level**](StockApi.md#get_stock_level) | **GET** /api/Stock/GetStockLevel | GetStockLevel
[**get_stock_level_batch**](StockApi.md#get_stock_level_batch) | **POST** /api/Stock/GetStockLevel_Batch | GetStockLevel_Batch
[**get_stock_level_by_location**](StockApi.md#get_stock_level_by_location) | **POST** /api/Stock/GetStockLevelByLocation | GetStockLevelByLocation
[**get_stock_sold**](StockApi.md#get_stock_sold) | **GET** /api/Stock/GetStockSold | GetStockSold
[**get_variation_group_by_name**](StockApi.md#get_variation_group_by_name) | **GET** /api/Stock/GetVariationGroupByName | GetVariationGroupByName
[**get_variation_group_by_parent_id**](StockApi.md#get_variation_group_by_parent_id) | **GET** /api/Stock/GetVariationGroupByParentId | GetVariationGroupByParentId
[**get_variation_group_search_types**](StockApi.md#get_variation_group_search_types) | **GET** /api/Stock/GetVariationGroupSearchTypes | GetVariationGroupSearchTypes
[**get_variation_items**](StockApi.md#get_variation_items) | **GET** /api/Stock/GetVariationItems | GetVariationItems
[**get_warehouse_move**](StockApi.md#get_warehouse_move) | **POST** /api/Stock/GetWarehouseMove | GetWarehouseMove
[**get_warehouse_moves_by_binrack**](StockApi.md#get_warehouse_moves_by_binrack) | **POST** /api/Stock/GetWarehouseMovesByBinrack | GetWarehouseMovesByBinrack
[**rename_variation_group**](StockApi.md#rename_variation_group) | **POST** /api/Stock/RenameVariationGroup | RenameVariationGroup
[**s_ku_exists**](StockApi.md#s_ku_exists) | **GET** /api/Stock/SKUExists | SKUExists
[**search_binracks**](StockApi.md#search_binracks) | **POST** /api/Stock/SearchBinracks | SearchBinracks
[**search_variation_groups**](StockApi.md#search_variation_groups) | **GET** /api/Stock/SearchVariationGroups | SearchVariationGroups
[**set_stock_level**](StockApi.md#set_stock_level) | **POST** /api/Stock/SetStockLevel | SetStockLevel
[**update_sku_group_identifier**](StockApi.md#update_sku_group_identifier) | **POST** /api/Stock/UpdateSkuGroupIdentifier | UpdateSkuGroupIdentifier
[**update_stock_levels_bulk**](StockApi.md#update_stock_levels_bulk) | **POST** /api/Stock/UpdateStockLevelsBulk | UpdateStockLevelsBulk
[**update_stock_levels_by_sku**](StockApi.md#update_stock_levels_by_sku) | **POST** /api/Stock/UpdateStockLevelsBySKU | UpdateStockLevelsBySKU
[**update_stock_minimum_level**](StockApi.md#update_stock_minimum_level) | **POST** /api/Stock/UpdateStockMinimumLevel | UpdateStockMinimumLevel
[**update_warehouse_move**](StockApi.md#update_warehouse_move) | **POST** /api/Stock/UpdateWarehouseMove | UpdateWarehouseMove


# **add_rolling_stock_take**
> AddRollingStockTakeResponse add_rolling_stock_take(request=request)

AddRollingStockTake

Add rolling stock take/count. Rolling stock count will create a stock count header for every day (UTC based). Every request will create a session, adds all entries into the stock count  recounts all totals and discrepancies. WMS location or batched items requires BatchInventoryId to be specified. If you are submitting stock level for item that doesn't have batch inventory you must create it first, get its id and submit in the count  The method validates all entries, if any errors encountered the whole request will be rejected. <b>Permissions Required: </b> GlobalPermissions.Inventory.StockTake.RollingStockCountNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.stock
from linnworks_api.generated.stock.models.add_rolling_stock_take_request import AddRollingStockTakeRequest
from linnworks_api.generated.stock.models.add_rolling_stock_take_response import AddRollingStockTakeResponse
from linnworks_api.generated.stock.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.stock.Configuration(
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
with linnworks_api.generated.stock.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.stock.StockApi(api_client)
    request = linnworks_api.generated.stock.AddRollingStockTakeRequest() # AddRollingStockTakeRequest |  (optional)

    try:
        # AddRollingStockTake
        api_response = api_instance.add_rolling_stock_take(request=request)
        print("The response of StockApi->add_rolling_stock_take:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StockApi->add_rolling_stock_take: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**AddRollingStockTakeRequest**](AddRollingStockTakeRequest.md)|  | [optional] 

### Return type

[**AddRollingStockTakeResponse**](AddRollingStockTakeResponse.md)

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

# **add_variation_items**
> List[VariationItem] add_variation_items(stock_add_variation_items_request)

AddVariationItems

Use this call to add a new item to a variation group <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>250</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.stock
from linnworks_api.generated.stock.models.stock_add_variation_items_request import StockAddVariationItemsRequest
from linnworks_api.generated.stock.models.variation_item import VariationItem
from linnworks_api.generated.stock.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.stock.Configuration(
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
with linnworks_api.generated.stock.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.stock.StockApi(api_client)
    stock_add_variation_items_request = linnworks_api.generated.stock.StockAddVariationItemsRequest() # StockAddVariationItemsRequest | 

    try:
        # AddVariationItems
        api_response = api_instance.add_variation_items(stock_add_variation_items_request)
        print("The response of StockApi->add_variation_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StockApi->add_variation_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_add_variation_items_request** | [**StockAddVariationItemsRequest**](StockAddVariationItemsRequest.md)|  | 

### Return type

[**List[VariationItem]**](VariationItem.md)

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

# **batch_stock_level_delta**
> BatchStockLevelDeltaResponse batch_stock_level_delta(stock_batch_stock_level_delta_request)

BatchStockLevelDelta

 <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.stock
from linnworks_api.generated.stock.models.batch_stock_level_delta_response import BatchStockLevelDeltaResponse
from linnworks_api.generated.stock.models.stock_batch_stock_level_delta_request import StockBatchStockLevelDeltaRequest
from linnworks_api.generated.stock.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.stock.Configuration(
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
with linnworks_api.generated.stock.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.stock.StockApi(api_client)
    stock_batch_stock_level_delta_request = linnworks_api.generated.stock.StockBatchStockLevelDeltaRequest() # StockBatchStockLevelDeltaRequest | 

    try:
        # BatchStockLevelDelta
        api_response = api_instance.batch_stock_level_delta(stock_batch_stock_level_delta_request)
        print("The response of StockApi->batch_stock_level_delta:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StockApi->batch_stock_level_delta: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_batch_stock_level_delta_request** | [**StockBatchStockLevelDeltaRequest**](StockBatchStockLevelDeltaRequest.md)|  | 

### Return type

[**BatchStockLevelDeltaResponse**](BatchStockLevelDeltaResponse.md)

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

# **book_in_stock_batch**
> StockItemBatch book_in_stock_batch(stock_book_in_stock_batch_request)

BookInStockBatch

Increases the stock level and current stock value of a batched stock item by the specified quantity <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.stock
from linnworks_api.generated.stock.models.stock_book_in_stock_batch_request import StockBookInStockBatchRequest
from linnworks_api.generated.stock.models.stock_item_batch import StockItemBatch
from linnworks_api.generated.stock.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.stock.Configuration(
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
with linnworks_api.generated.stock.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.stock.StockApi(api_client)
    stock_book_in_stock_batch_request = linnworks_api.generated.stock.StockBookInStockBatchRequest() # StockBookInStockBatchRequest | 

    try:
        # BookInStockBatch
        api_response = api_instance.book_in_stock_batch(stock_book_in_stock_batch_request)
        print("The response of StockApi->book_in_stock_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StockApi->book_in_stock_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_book_in_stock_batch_request** | [**StockBookInStockBatchRequest**](StockBookInStockBatchRequest.md)|  | 

### Return type

[**StockItemBatch**](StockItemBatch.md)

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

# **book_in_stock_item**
> book_in_stock_item(stock_book_in_stock_item_request)

BookInStockItem

Increases the stock level and current stock value of a stock item by the specified quantity. <b>Permissions Required: </b> GlobalPermissions.Inventory.Stock.StockWrite.ChangeStockLevelsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.stock
from linnworks_api.generated.stock.models.stock_book_in_stock_item_request import StockBookInStockItemRequest
from linnworks_api.generated.stock.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.stock.Configuration(
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
with linnworks_api.generated.stock.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.stock.StockApi(api_client)
    stock_book_in_stock_item_request = linnworks_api.generated.stock.StockBookInStockItemRequest() # StockBookInStockItemRequest | 

    try:
        # BookInStockItem
        api_instance.book_in_stock_item(stock_book_in_stock_item_request)
    except Exception as e:
        print("Exception when calling StockApi->book_in_stock_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_book_in_stock_item_request** | [**StockBookInStockItemRequest**](StockBookInStockItemRequest.md)|  | 

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

# **check_variation_parent_sku_exists**
> str check_variation_parent_sku_exists(parent_sku=parent_sku)

CheckVariationParentSKUExists

Use this call to check if a potential parent SKU exist and its current status. <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.stock
from linnworks_api.generated.stock.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.stock.Configuration(
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
with linnworks_api.generated.stock.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.stock.StockApi(api_client)
    parent_sku = 'parent_sku_example' # str | The SKU (optional)

    try:
        # CheckVariationParentSKUExists
        api_response = api_instance.check_variation_parent_sku_exists(parent_sku=parent_sku)
        print("The response of StockApi->check_variation_parent_sku_exists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StockApi->check_variation_parent_sku_exists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_sku** | **str**| The SKU | [optional] 

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

# **complete_warehouse_move**
> complete_warehouse_move(stock_complete_warehouse_move_request)

CompleteWarehouseMove

 <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.stock
from linnworks_api.generated.stock.models.stock_complete_warehouse_move_request import StockCompleteWarehouseMoveRequest
from linnworks_api.generated.stock.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.stock.Configuration(
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
with linnworks_api.generated.stock.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.stock.StockApi(api_client)
    stock_complete_warehouse_move_request = linnworks_api.generated.stock.StockCompleteWarehouseMoveRequest() # StockCompleteWarehouseMoveRequest | 

    try:
        # CompleteWarehouseMove
        api_instance.complete_warehouse_move(stock_complete_warehouse_move_request)
    except Exception as e:
        print("Exception when calling StockApi->complete_warehouse_move: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_complete_warehouse_move_request** | [**StockCompleteWarehouseMoveRequest**](StockCompleteWarehouseMoveRequest.md)|  | 

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

# **create_stock_batches**
> List[StockItemBatch] create_stock_batches(stock_create_stock_batches_request)

CreateStockBatches

Creates stock item batches <b>Permissions Required: </b> GlobalPermissions.Inventory.Stock.StockWrite.ChangeStockLevelsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.stock
from linnworks_api.generated.stock.models.stock_create_stock_batches_request import StockCreateStockBatchesRequest
from linnworks_api.generated.stock.models.stock_item_batch import StockItemBatch
from linnworks_api.generated.stock.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.stock.Configuration(
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
with linnworks_api.generated.stock.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.stock.StockApi(api_client)
    stock_create_stock_batches_request = linnworks_api.generated.stock.StockCreateStockBatchesRequest() # StockCreateStockBatchesRequest | 

    try:
        # CreateStockBatches
        api_response = api_instance.create_stock_batches(stock_create_stock_batches_request)
        print("The response of StockApi->create_stock_batches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StockApi->create_stock_batches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_create_stock_batches_request** | [**StockCreateStockBatchesRequest**](StockCreateStockBatchesRequest.md)|  | 

### Return type

[**List[StockItemBatch]**](StockItemBatch.md)

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

# **create_variation_group**
> VariationGroup create_variation_group(stock_create_variation_group_request)

CreateVariationGroup

Use this call to create a variation group <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.stock
from linnworks_api.generated.stock.models.stock_create_variation_group_request import StockCreateVariationGroupRequest
from linnworks_api.generated.stock.models.variation_group import VariationGroup
from linnworks_api.generated.stock.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.stock.Configuration(
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
with linnworks_api.generated.stock.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.stock.StockApi(api_client)
    stock_create_variation_group_request = linnworks_api.generated.stock.StockCreateVariationGroupRequest() # StockCreateVariationGroupRequest | 

    try:
        # CreateVariationGroup
        api_response = api_instance.create_variation_group(stock_create_variation_group_request)
        print("The response of StockApi->create_variation_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StockApi->create_variation_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_create_variation_group_request** | [**StockCreateVariationGroupRequest**](StockCreateVariationGroupRequest.md)|  | 

### Return type

[**VariationGroup**](VariationGroup.md)

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

# **create_warehouse_move**
> GetWarehouseMoveResponse create_warehouse_move(request=request)

CreateWarehouseMove

Create a new warehouse move in state of In Transit or Open.   To create a new move you need the exact batch inventory id and bin rack id of the destination. However it is possible to create a move without knowing where it is going specifically,   in which case don't supply BinrackIdDestination (or send null) <b>Permissions Required: </b> GlobalPermissions.Inventory.WarehouseManagement.StockMoveNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.stock
from linnworks_api.generated.stock.models.create_warehouse_move_request import CreateWarehouseMoveRequest
from linnworks_api.generated.stock.models.get_warehouse_move_response import GetWarehouseMoveResponse
from linnworks_api.generated.stock.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.stock.Configuration(
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
with linnworks_api.generated.stock.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.stock.StockApi(api_client)
    request = linnworks_api.generated.stock.CreateWarehouseMoveRequest() # CreateWarehouseMoveRequest |  (optional)

    try:
        # CreateWarehouseMove
        api_response = api_instance.create_warehouse_move(request=request)
        print("The response of StockApi->create_warehouse_move:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StockApi->create_warehouse_move: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CreateWarehouseMoveRequest**](CreateWarehouseMoveRequest.md)|  | [optional] 

### Return type

[**GetWarehouseMoveResponse**](GetWarehouseMoveResponse.md)

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

# **delete_move**
> delete_move(request=request)

DeleteMove

Use this call to delete a stock move <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.stock
from linnworks_api.generated.stock.models.delete_move_request import DeleteMoveRequest
from linnworks_api.generated.stock.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.stock.Configuration(
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
with linnworks_api.generated.stock.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.stock.StockApi(api_client)
    request = linnworks_api.generated.stock.DeleteMoveRequest() # DeleteMoveRequest |  (optional)

    try:
        # DeleteMove
        api_instance.delete_move(request=request)
    except Exception as e:
        print("Exception when calling StockApi->delete_move: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**DeleteMoveRequest**](DeleteMoveRequest.md)|  | [optional] 

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

# **delete_variation_group**
> delete_variation_group(pk_variation_group_id=pk_variation_group_id)

DeleteVariationGroup

Use this call to delete variation group by id <b>Permissions Required: </b> GlobalPermissions.Inventory.DeleteMyInventoryItems.DeleteItemsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.stock
from linnworks_api.generated.stock.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.stock.Configuration(
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
with linnworks_api.generated.stock.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.stock.StockApi(api_client)
    pk_variation_group_id = 'pk_variation_group_id_example' # str |  (optional)

    try:
        # DeleteVariationGroup
        api_instance.delete_variation_group(pk_variation_group_id=pk_variation_group_id)
    except Exception as e:
        print("Exception when calling StockApi->delete_variation_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pk_variation_group_id** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_variation_groups**
> delete_variation_groups(stock_delete_variation_groups_request)

DeleteVariationGroups

Use this call to delete variation groups by ids <b>Permissions Required: </b> GlobalPermissions.Inventory.DeleteMyInventoryItems.DeleteItemsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.stock
from linnworks_api.generated.stock.models.stock_delete_variation_groups_request import StockDeleteVariationGroupsRequest
from linnworks_api.generated.stock.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.stock.Configuration(
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
with linnworks_api.generated.stock.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.stock.StockApi(api_client)
    stock_delete_variation_groups_request = linnworks_api.generated.stock.StockDeleteVariationGroupsRequest() # StockDeleteVariationGroupsRequest | 

    try:
        # DeleteVariationGroups
        api_instance.delete_variation_groups(stock_delete_variation_groups_request)
    except Exception as e:
        print("Exception when calling StockApi->delete_variation_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_delete_variation_groups_request** | [**StockDeleteVariationGroupsRequest**](StockDeleteVariationGroupsRequest.md)|  | 

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

# **delete_variation_item**
> delete_variation_item(stock_delete_variation_item_request)

DeleteVariationItem

Use this call to add a new item to a variation group <b>Permissions Required: </b> GlobalPermissions.Inventory.DeleteMyInventoryItems.DeleteItemsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.stock
from linnworks_api.generated.stock.models.stock_delete_variation_item_request import StockDeleteVariationItemRequest
from linnworks_api.generated.stock.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.stock.Configuration(
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
with linnworks_api.generated.stock.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.stock.StockApi(api_client)
    stock_delete_variation_item_request = linnworks_api.generated.stock.StockDeleteVariationItemRequest() # StockDeleteVariationItemRequest | 

    try:
        # DeleteVariationItem
        api_instance.delete_variation_item(stock_delete_variation_item_request)
    except Exception as e:
        print("Exception when calling StockApi->delete_variation_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_delete_variation_item_request** | [**StockDeleteVariationItemRequest**](StockDeleteVariationItemRequest.md)|  | 

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

# **delete_variation_items**
> delete_variation_items(stock_delete_variation_items_request)

DeleteVariationItems

Use this call to delete variation items in bulk <b>Permissions Required: </b> GlobalPermissions.Inventory.DeleteMyInventoryItems.DeleteItemsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.stock
from linnworks_api.generated.stock.models.stock_delete_variation_items_request import StockDeleteVariationItemsRequest
from linnworks_api.generated.stock.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.stock.Configuration(
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
with linnworks_api.generated.stock.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.stock.StockApi(api_client)
    stock_delete_variation_items_request = linnworks_api.generated.stock.StockDeleteVariationItemsRequest() # StockDeleteVariationItemsRequest | 

    try:
        # DeleteVariationItems
        api_instance.delete_variation_items(stock_delete_variation_items_request)
    except Exception as e:
        print("Exception when calling StockApi->delete_variation_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_delete_variation_items_request** | [**StockDeleteVariationItemsRequest**](StockDeleteVariationItemsRequest.md)|  | 

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

# **get_bin_racks_by_id**
> BinracksResponse get_bin_racks_by_id(request=request)

GetBinRacksById

Returns the list of BinRacks by BinRack Ids for WMS locations. <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.stock
from linnworks_api.generated.stock.models.binracks_response import BinracksResponse
from linnworks_api.generated.stock.models.get_binrack_by_id_request import GetBinrackByIdRequest
from linnworks_api.generated.stock.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.stock.Configuration(
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
with linnworks_api.generated.stock.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.stock.StockApi(api_client)
    request = linnworks_api.generated.stock.GetBinrackByIdRequest() # GetBinrackByIdRequest |  (optional)

    try:
        # GetBinRacksById
        api_response = api_instance.get_bin_racks_by_id(request=request)
        print("The response of StockApi->get_bin_racks_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StockApi->get_bin_racks_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**GetBinrackByIdRequest**](GetBinrackByIdRequest.md)|  | [optional] 

### Return type

[**BinracksResponse**](BinracksResponse.md)

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

# **get_binrack_skus**
> BinrackSkuResponse get_binrack_skus(request=request)

GetBinrackSkus

 <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.stock
from linnworks_api.generated.stock.models.binrack_sku_response import BinrackSkuResponse
from linnworks_api.generated.stock.models.get_bin_rack_skus_request import GetBinRackSkusRequest
from linnworks_api.generated.stock.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.stock.Configuration(
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
with linnworks_api.generated.stock.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.stock.StockApi(api_client)
    request = linnworks_api.generated.stock.GetBinRackSkusRequest() # GetBinRackSkusRequest |  (optional)

    try:
        # GetBinrackSkus
        api_response = api_instance.get_binrack_skus(request=request)
        print("The response of StockApi->get_binrack_skus:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StockApi->get_binrack_skus: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**GetBinRackSkusRequest**](GetBinRackSkusRequest.md)|  | [optional] 

### Return type

[**BinrackSkuResponse**](BinrackSkuResponse.md)

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

# **get_item_changes_history**
> GenericPagedResultStockItemChangeHistory get_item_changes_history(stock_item_id=stock_item_id, location_id=location_id, entries_per_page=entries_per_page, page_number=page_number)

GetItemChangesHistory

Use this call to retrieve report about \"stock changes of an item\" <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>250</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.stock
from linnworks_api.generated.stock.models.generic_paged_result_stock_item_change_history import GenericPagedResultStockItemChangeHistory
from linnworks_api.generated.stock.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.stock.Configuration(
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
with linnworks_api.generated.stock.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.stock.StockApi(api_client)
    stock_item_id = 'stock_item_id_example' # str | Used to specify report stock item id (optional)
    location_id = 'location_id_example' # str | Used to specify report location id. If null then combined (optional)
    entries_per_page = 56 # int | Used to specify number of entries per page in report (optional)
    page_number = 56 # int | Used to specify report page number. If -1 then will return all pages (optional)

    try:
        # GetItemChangesHistory
        api_response = api_instance.get_item_changes_history(stock_item_id=stock_item_id, location_id=location_id, entries_per_page=entries_per_page, page_number=page_number)
        print("The response of StockApi->get_item_changes_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StockApi->get_item_changes_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_item_id** | **str**| Used to specify report stock item id | [optional] 
 **location_id** | **str**| Used to specify report location id. If null then combined | [optional] 
 **entries_per_page** | **int**| Used to specify number of entries per page in report | [optional] 
 **page_number** | **int**| Used to specify report page number. If -1 then will return all pages | [optional] 

### Return type

[**GenericPagedResultStockItemChangeHistory**](GenericPagedResultStockItemChangeHistory.md)

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

# **get_item_changes_history_csv**
> TempFile get_item_changes_history_csv(stock_item_id=stock_item_id, location_id=location_id)

GetItemChangesHistoryCSV

Use this call to retrieve link to csv file report about \"Stock changes of an item\" <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.stock
from linnworks_api.generated.stock.models.temp_file import TempFile
from linnworks_api.generated.stock.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.stock.Configuration(
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
with linnworks_api.generated.stock.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.stock.StockApi(api_client)
    stock_item_id = 'stock_item_id_example' # str | Used to specify stock item id (optional)
    location_id = 'location_id_example' # str | Used to specify location id. If null then combined (optional)

    try:
        # GetItemChangesHistoryCSV
        api_response = api_instance.get_item_changes_history_csv(stock_item_id=stock_item_id, location_id=location_id)
        print("The response of StockApi->get_item_changes_history_csv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StockApi->get_item_changes_history_csv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_item_id** | **str**| Used to specify stock item id | [optional] 
 **location_id** | **str**| Used to specify location id. If null then combined | [optional] 

### Return type

[**TempFile**](TempFile.md)

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

# **get_sold_stat**
> List[StockItemSoldStat] get_sold_stat(stock_item_id=stock_item_id)

GetSoldStat

Use this call to retrieve report about \"item sold stat\" <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>250</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.stock
from linnworks_api.generated.stock.models.stock_item_sold_stat import StockItemSoldStat
from linnworks_api.generated.stock.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.stock.Configuration(
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
with linnworks_api.generated.stock.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.stock.StockApi(api_client)
    stock_item_id = 'stock_item_id_example' # str | Used to specify report stock item id (optional)

    try:
        # GetSoldStat
        api_response = api_instance.get_sold_stat(stock_item_id=stock_item_id)
        print("The response of StockApi->get_sold_stat:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StockApi->get_sold_stat: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_item_id** | **str**| Used to specify report stock item id | [optional] 

### Return type

[**List[StockItemSoldStat]**](StockItemSoldStat.md)

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

# **get_stock_consumption**
> List[StockConsumption] get_stock_consumption(stock_item_id=stock_item_id, location_id=location_id, start_date=start_date, end_date=end_date)

GetStockConsumption

Use this call to retrieve report about \"stock consumption between two dates\" <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>250</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.stock
from linnworks_api.generated.stock.models.stock_consumption import StockConsumption
from linnworks_api.generated.stock.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.stock.Configuration(
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
with linnworks_api.generated.stock.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.stock.StockApi(api_client)
    stock_item_id = 'stock_item_id_example' # str | Used to specify report stock id (optional)
    location_id = 'location_id_example' # str | Used to specify location id. If null, then will return combined result of every location (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | Used to specify report start date (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime | Used to specify report end date (optional)

    try:
        # GetStockConsumption
        api_response = api_instance.get_stock_consumption(stock_item_id=stock_item_id, location_id=location_id, start_date=start_date, end_date=end_date)
        print("The response of StockApi->get_stock_consumption:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StockApi->get_stock_consumption: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_item_id** | **str**| Used to specify report stock id | [optional] 
 **location_id** | **str**| Used to specify location id. If null, then will return combined result of every location | [optional] 
 **start_date** | **datetime**| Used to specify report start date | [optional] 
 **end_date** | **datetime**| Used to specify report end date | [optional] 

### Return type

[**List[StockConsumption]**](StockConsumption.md)

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

# **get_stock_due_po**
> List[StockItemDuePO] get_stock_due_po(stock_item_id=stock_item_id)

GetStockDuePO

Use this call to retrieve report about \"item stock due po\" <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.stock
from linnworks_api.generated.stock.models.stock_item_due_po import StockItemDuePO
from linnworks_api.generated.stock.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.stock.Configuration(
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
with linnworks_api.generated.stock.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.stock.StockApi(api_client)
    stock_item_id = 'stock_item_id_example' # str | Used to specify report stock item id (optional)

    try:
        # GetStockDuePO
        api_response = api_instance.get_stock_due_po(stock_item_id=stock_item_id)
        print("The response of StockApi->get_stock_due_po:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StockApi->get_stock_due_po: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_item_id** | **str**| Used to specify report stock item id | [optional] 

### Return type

[**List[StockItemDuePO]**](StockItemDuePO.md)

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

# **get_stock_item_return_stat**
> List[StockItemReturn] get_stock_item_return_stat(stock_item_id=stock_item_id)

GetStockItemReturnStat

Use this call to retrieve report about \"item return stat\" <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.stock
from linnworks_api.generated.stock.models.stock_item_return import StockItemReturn
from linnworks_api.generated.stock.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.stock.Configuration(
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
with linnworks_api.generated.stock.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.stock.StockApi(api_client)
    stock_item_id = 'stock_item_id_example' # str | Used to specify report stock item id (optional)

    try:
        # GetStockItemReturnStat
        api_response = api_instance.get_stock_item_return_stat(stock_item_id=stock_item_id)
        print("The response of StockApi->get_stock_item_return_stat:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StockApi->get_stock_item_return_stat: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_item_id** | **str**| Used to specify report stock item id | [optional] 

### Return type

[**List[StockItemReturn]**](StockItemReturn.md)

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

# **get_stock_item_scrap_stat**
> List[StockItemScrap] get_stock_item_scrap_stat(stock_item_id=stock_item_id)

GetStockItemScrapStat

Use this call to retrieve report about \"item stock scrap stat\" <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.stock
from linnworks_api.generated.stock.models.stock_item_scrap import StockItemScrap
from linnworks_api.generated.stock.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.stock.Configuration(
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
with linnworks_api.generated.stock.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.stock.StockApi(api_client)
    stock_item_id = 'stock_item_id_example' # str | Used to specify report stock item id (optional)

    try:
        # GetStockItemScrapStat
        api_response = api_instance.get_stock_item_scrap_stat(stock_item_id=stock_item_id)
        print("The response of StockApi->get_stock_item_scrap_stat:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StockApi->get_stock_item_scrap_stat: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_item_id** | **str**| Used to specify report stock item id | [optional] 

### Return type

[**List[StockItemScrap]**](StockItemScrap.md)

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

# **get_stock_item_type_info**
> GetStockItemTypeInfoResponse get_stock_item_type_info(request=request)

GetStockItemTypeInfo

 <b>Permissions Required: </b> GlobalPermissions.Inventory.Stock.StockReadNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.stock
from linnworks_api.generated.stock.models.get_stock_item_type_info_request import GetStockItemTypeInfoRequest
from linnworks_api.generated.stock.models.get_stock_item_type_info_response import GetStockItemTypeInfoResponse
from linnworks_api.generated.stock.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.stock.Configuration(
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
with linnworks_api.generated.stock.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.stock.StockApi(api_client)
    request = linnworks_api.generated.stock.GetStockItemTypeInfoRequest() # GetStockItemTypeInfoRequest |  (optional)

    try:
        # GetStockItemTypeInfo
        api_response = api_instance.get_stock_item_type_info(request=request)
        print("The response of StockApi->get_stock_item_type_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StockApi->get_stock_item_type_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**GetStockItemTypeInfoRequest**](GetStockItemTypeInfoRequest.md)|  | [optional] 

### Return type

[**GetStockItemTypeInfoResponse**](GetStockItemTypeInfoResponse.md)

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

# **get_stock_items**
> GenericPagedResultStockItem get_stock_items(key_word=key_word, location_id=location_id, entries_per_page=entries_per_page, page_number=page_number, exclude_composites=exclude_composites, exclude_variations=exclude_variations, exclude_batches=exclude_batches)

GetStockItems

Use this call to retrieve report about \"Found stock items\" <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.stock
from linnworks_api.generated.stock.models.generic_paged_result_stock_item import GenericPagedResultStockItem
from linnworks_api.generated.stock.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.stock.Configuration(
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
with linnworks_api.generated.stock.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.stock.StockApi(api_client)
    key_word = 'key_word_example' # str |  (optional)
    location_id = 'location_id_example' # str |  (optional)
    entries_per_page = 56 # int |  (optional)
    page_number = 56 # int |  (optional)
    exclude_composites = True # bool |  (optional)
    exclude_variations = True # bool |  (optional)
    exclude_batches = True # bool |  (optional)

    try:
        # GetStockItems
        api_response = api_instance.get_stock_items(key_word=key_word, location_id=location_id, entries_per_page=entries_per_page, page_number=page_number, exclude_composites=exclude_composites, exclude_variations=exclude_variations, exclude_batches=exclude_batches)
        print("The response of StockApi->get_stock_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StockApi->get_stock_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_word** | **str**|  | [optional] 
 **location_id** | **str**|  | [optional] 
 **entries_per_page** | **int**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **exclude_composites** | **bool**|  | [optional] 
 **exclude_variations** | **bool**|  | [optional] 
 **exclude_batches** | **bool**|  | [optional] 

### Return type

[**GenericPagedResultStockItem**](GenericPagedResultStockItem.md)

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

# **get_stock_items_by_ids**
> GetStockItemsByIdsResponse get_stock_items_by_ids(request=request)

GetStockItemsByIds

 <b>Permissions Required: </b> GlobalPermissions.Inventory.Stock.StockReadNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.stock
from linnworks_api.generated.stock.models.get_stock_items_by_ids_request import GetStockItemsByIdsRequest
from linnworks_api.generated.stock.models.get_stock_items_by_ids_response import GetStockItemsByIdsResponse
from linnworks_api.generated.stock.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.stock.Configuration(
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
with linnworks_api.generated.stock.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.stock.StockApi(api_client)
    request = linnworks_api.generated.stock.GetStockItemsByIdsRequest() # GetStockItemsByIdsRequest |  (optional)

    try:
        # GetStockItemsByIds
        api_response = api_instance.get_stock_items_by_ids(request=request)
        print("The response of StockApi->get_stock_items_by_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StockApi->get_stock_items_by_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**GetStockItemsByIdsRequest**](GetStockItemsByIdsRequest.md)|  | [optional] 

### Return type

[**GetStockItemsByIdsResponse**](GetStockItemsByIdsResponse.md)

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

# **get_stock_items_by_key**
> List[StockItem] get_stock_items_by_key(stock_get_stock_items_by_key_request)

GetStockItemsByKey

Returns a list of Stock Items for the provided key and location <b>Permissions Required: </b> GlobalPermissions.Inventory.Stock.StockReadNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>250</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.stock
from linnworks_api.generated.stock.models.stock_get_stock_items_by_key_request import StockGetStockItemsByKeyRequest
from linnworks_api.generated.stock.models.stock_item import StockItem
from linnworks_api.generated.stock.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.stock.Configuration(
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
with linnworks_api.generated.stock.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.stock.StockApi(api_client)
    stock_get_stock_items_by_key_request = linnworks_api.generated.stock.StockGetStockItemsByKeyRequest() # StockGetStockItemsByKeyRequest | 

    try:
        # GetStockItemsByKey
        api_response = api_instance.get_stock_items_by_key(stock_get_stock_items_by_key_request)
        print("The response of StockApi->get_stock_items_by_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StockApi->get_stock_items_by_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_get_stock_items_by_key_request** | [**StockGetStockItemsByKeyRequest**](StockGetStockItemsByKeyRequest.md)|  | 

### Return type

[**List[StockItem]**](StockItem.md)

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

# **get_stock_items_full**
> List[StockItemFull] get_stock_items_full(stock_get_stock_items_full_request)

GetStockItemsFull

Used to get inventory information at a basic level <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.stock
from linnworks_api.generated.stock.models.stock_get_stock_items_full_request import StockGetStockItemsFullRequest
from linnworks_api.generated.stock.models.stock_item_full import StockItemFull
from linnworks_api.generated.stock.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.stock.Configuration(
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
with linnworks_api.generated.stock.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.stock.StockApi(api_client)
    stock_get_stock_items_full_request = linnworks_api.generated.stock.StockGetStockItemsFullRequest() # StockGetStockItemsFullRequest | 

    try:
        # GetStockItemsFull
        api_response = api_instance.get_stock_items_full(stock_get_stock_items_full_request)
        print("The response of StockApi->get_stock_items_full:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StockApi->get_stock_items_full: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_get_stock_items_full_request** | [**StockGetStockItemsFullRequest**](StockGetStockItemsFullRequest.md)|  | 

### Return type

[**List[StockItemFull]**](StockItemFull.md)

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

# **get_stock_items_full_by_ids**
> GetStockItemsFullByIdsResponse get_stock_items_full_by_ids(stock_get_stock_items_full_by_ids_request)

GetStockItemsFullByIds

Used to get inventory item information at a basic level from ids. <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>250</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.stock
from linnworks_api.generated.stock.models.get_stock_items_full_by_ids_response import GetStockItemsFullByIdsResponse
from linnworks_api.generated.stock.models.stock_get_stock_items_full_by_ids_request import StockGetStockItemsFullByIdsRequest
from linnworks_api.generated.stock.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.stock.Configuration(
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
with linnworks_api.generated.stock.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.stock.StockApi(api_client)
    stock_get_stock_items_full_by_ids_request = linnworks_api.generated.stock.StockGetStockItemsFullByIdsRequest() # StockGetStockItemsFullByIdsRequest | 

    try:
        # GetStockItemsFullByIds
        api_response = api_instance.get_stock_items_full_by_ids(stock_get_stock_items_full_by_ids_request)
        print("The response of StockApi->get_stock_items_full_by_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StockApi->get_stock_items_full_by_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_get_stock_items_full_by_ids_request** | [**StockGetStockItemsFullByIdsRequest**](StockGetStockItemsFullByIdsRequest.md)|  | 

### Return type

[**GetStockItemsFullByIdsResponse**](GetStockItemsFullByIdsResponse.md)

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

# **get_stock_items_location**
> GetStockItemsLocationResponse get_stock_items_location(stock_get_stock_items_location_request)

GetStockItemsLocation

Get the location (including binrack) of a given list of stockItemIds and stockLocationIds <b>Permissions Required: </b> GlobalPermissions.Inventory.MyInventoryNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.stock
from linnworks_api.generated.stock.models.get_stock_items_location_response import GetStockItemsLocationResponse
from linnworks_api.generated.stock.models.stock_get_stock_items_location_request import StockGetStockItemsLocationRequest
from linnworks_api.generated.stock.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.stock.Configuration(
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
with linnworks_api.generated.stock.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.stock.StockApi(api_client)
    stock_get_stock_items_location_request = linnworks_api.generated.stock.StockGetStockItemsLocationRequest() # StockGetStockItemsLocationRequest | 

    try:
        # GetStockItemsLocation
        api_response = api_instance.get_stock_items_location(stock_get_stock_items_location_request)
        print("The response of StockApi->get_stock_items_location:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StockApi->get_stock_items_location: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_get_stock_items_location_request** | [**StockGetStockItemsLocationRequest**](StockGetStockItemsLocationRequest.md)|  | 

### Return type

[**GetStockItemsLocationResponse**](GetStockItemsLocationResponse.md)

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

# **get_stock_level**
> List[StockItemLevel] get_stock_level(stock_item_id=stock_item_id)

GetStockLevel

Use this call to retrieve report about \"item stock level\" <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>250</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.stock
from linnworks_api.generated.stock.models.stock_item_level import StockItemLevel
from linnworks_api.generated.stock.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.stock.Configuration(
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
with linnworks_api.generated.stock.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.stock.StockApi(api_client)
    stock_item_id = 'stock_item_id_example' # str | Used to specify stock item id (optional)

    try:
        # GetStockLevel
        api_response = api_instance.get_stock_level(stock_item_id=stock_item_id)
        print("The response of StockApi->get_stock_level:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StockApi->get_stock_level: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_item_id** | **str**| Used to specify stock item id | [optional] 

### Return type

[**List[StockItemLevel]**](StockItemLevel.md)

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

# **get_stock_level_batch**
> List[GetStockLevelBatchResponse] get_stock_level_batch(stock_get_stock_level_batch_request)

GetStockLevel_Batch

Use this call to retrieve report about \"item stock level\" <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>250</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.stock
from linnworks_api.generated.stock.models.get_stock_level_batch_response import GetStockLevelBatchResponse
from linnworks_api.generated.stock.models.stock_get_stock_level_batch_request import StockGetStockLevelBatchRequest
from linnworks_api.generated.stock.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.stock.Configuration(
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
with linnworks_api.generated.stock.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.stock.StockApi(api_client)
    stock_get_stock_level_batch_request = linnworks_api.generated.stock.StockGetStockLevelBatchRequest() # StockGetStockLevelBatchRequest | 

    try:
        # GetStockLevel_Batch
        api_response = api_instance.get_stock_level_batch(stock_get_stock_level_batch_request)
        print("The response of StockApi->get_stock_level_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StockApi->get_stock_level_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_get_stock_level_batch_request** | [**StockGetStockLevelBatchRequest**](StockGetStockLevelBatchRequest.md)|  | 

### Return type

[**List[GetStockLevelBatchResponse]**](GetStockLevelBatchResponse.md)

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

# **get_stock_level_by_location**
> GetStockLevelByLocationResponse get_stock_level_by_location(stock_get_stock_level_by_location_request)

GetStockLevelByLocation

Use this call to retrieve report about \"item stock level\" <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>250</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.stock
from linnworks_api.generated.stock.models.get_stock_level_by_location_response import GetStockLevelByLocationResponse
from linnworks_api.generated.stock.models.stock_get_stock_level_by_location_request import StockGetStockLevelByLocationRequest
from linnworks_api.generated.stock.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.stock.Configuration(
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
with linnworks_api.generated.stock.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.stock.StockApi(api_client)
    stock_get_stock_level_by_location_request = linnworks_api.generated.stock.StockGetStockLevelByLocationRequest() # StockGetStockLevelByLocationRequest | 

    try:
        # GetStockLevelByLocation
        api_response = api_instance.get_stock_level_by_location(stock_get_stock_level_by_location_request)
        print("The response of StockApi->get_stock_level_by_location:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StockApi->get_stock_level_by_location: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_get_stock_level_by_location_request** | [**StockGetStockLevelByLocationRequest**](StockGetStockLevelByLocationRequest.md)|  | 

### Return type

[**GetStockLevelByLocationResponse**](GetStockLevelByLocationResponse.md)

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

# **get_stock_sold**
> List[StockItemSold] get_stock_sold(stock_item_id=stock_item_id)

GetStockSold

Use this call to retrieve report about \"item stock sold\" <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.stock
from linnworks_api.generated.stock.models.stock_item_sold import StockItemSold
from linnworks_api.generated.stock.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.stock.Configuration(
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
with linnworks_api.generated.stock.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.stock.StockApi(api_client)
    stock_item_id = 'stock_item_id_example' # str | Used to specify report stock item id (optional)

    try:
        # GetStockSold
        api_response = api_instance.get_stock_sold(stock_item_id=stock_item_id)
        print("The response of StockApi->get_stock_sold:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StockApi->get_stock_sold: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_item_id** | **str**| Used to specify report stock item id | [optional] 

### Return type

[**List[StockItemSold]**](StockItemSold.md)

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

# **get_variation_group_by_name**
> VariationGroup get_variation_group_by_name(variation_name=variation_name)

GetVariationGroupByName

Use this call to search for a variation group by the group name <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.stock
from linnworks_api.generated.stock.models.variation_group import VariationGroup
from linnworks_api.generated.stock.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.stock.Configuration(
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
with linnworks_api.generated.stock.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.stock.StockApi(api_client)
    variation_name = 'variation_name_example' # str | The group name to search by (optional)

    try:
        # GetVariationGroupByName
        api_response = api_instance.get_variation_group_by_name(variation_name=variation_name)
        print("The response of StockApi->get_variation_group_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StockApi->get_variation_group_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variation_name** | **str**| The group name to search by | [optional] 

### Return type

[**VariationGroup**](VariationGroup.md)

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

# **get_variation_group_by_parent_id**
> VariationGroup get_variation_group_by_parent_id(pk_stock_item_id=pk_stock_item_id)

GetVariationGroupByParentId

Use this call to search for a variation group by the parent SKU's stock item id <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.stock
from linnworks_api.generated.stock.models.variation_group import VariationGroup
from linnworks_api.generated.stock.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.stock.Configuration(
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
with linnworks_api.generated.stock.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.stock.StockApi(api_client)
    pk_stock_item_id = 'pk_stock_item_id_example' # str | The stock item id to search by (optional)

    try:
        # GetVariationGroupByParentId
        api_response = api_instance.get_variation_group_by_parent_id(pk_stock_item_id=pk_stock_item_id)
        print("The response of StockApi->get_variation_group_by_parent_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StockApi->get_variation_group_by_parent_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pk_stock_item_id** | **str**| The stock item id to search by | [optional] 

### Return type

[**VariationGroup**](VariationGroup.md)

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

# **get_variation_group_search_types**
> List[GenericEnumDescriptor] get_variation_group_search_types()

GetVariationGroupSearchTypes

Use this call to retrieve a list of the search types for searching for variation groups <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.stock
from linnworks_api.generated.stock.models.generic_enum_descriptor import GenericEnumDescriptor
from linnworks_api.generated.stock.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.stock.Configuration(
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
with linnworks_api.generated.stock.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.stock.StockApi(api_client)

    try:
        # GetVariationGroupSearchTypes
        api_response = api_instance.get_variation_group_search_types()
        print("The response of StockApi->get_variation_group_search_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StockApi->get_variation_group_search_types: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GenericEnumDescriptor]**](GenericEnumDescriptor.md)

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

# **get_variation_items**
> List[VariationItem] get_variation_items(pk_variation_item_id=pk_variation_item_id)

GetVariationItems

Use this call to retrieve the items in this variation <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>250</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.stock
from linnworks_api.generated.stock.models.variation_item import VariationItem
from linnworks_api.generated.stock.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.stock.Configuration(
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
with linnworks_api.generated.stock.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.stock.StockApi(api_client)
    pk_variation_item_id = 'pk_variation_item_id_example' # str | The variation item id (optional)

    try:
        # GetVariationItems
        api_response = api_instance.get_variation_items(pk_variation_item_id=pk_variation_item_id)
        print("The response of StockApi->get_variation_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StockApi->get_variation_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pk_variation_item_id** | **str**| The variation item id | [optional] 

### Return type

[**List[VariationItem]**](VariationItem.md)

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

# **get_warehouse_move**
> GetWarehouseMoveResponse get_warehouse_move(request=request)

GetWarehouseMove

Use this call to get details for a stock move. <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.stock
from linnworks_api.generated.stock.models.get_warehouse_move_request import GetWarehouseMoveRequest
from linnworks_api.generated.stock.models.get_warehouse_move_response import GetWarehouseMoveResponse
from linnworks_api.generated.stock.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.stock.Configuration(
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
with linnworks_api.generated.stock.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.stock.StockApi(api_client)
    request = linnworks_api.generated.stock.GetWarehouseMoveRequest() # GetWarehouseMoveRequest |  (optional)

    try:
        # GetWarehouseMove
        api_response = api_instance.get_warehouse_move(request=request)
        print("The response of StockApi->get_warehouse_move:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StockApi->get_warehouse_move: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**GetWarehouseMoveRequest**](GetWarehouseMoveRequest.md)|  | [optional] 

### Return type

[**GetWarehouseMoveResponse**](GetWarehouseMoveResponse.md)

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

# **get_warehouse_moves_by_binrack**
> GetWarehouseMovesByBinrackResponse get_warehouse_moves_by_binrack(stock_get_warehouse_moves_by_binrack_request)

GetWarehouseMovesByBinrack

Use this call to get details for stock moves within a specific binrack. Returns both incoming and outgoing stock. <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.stock
from linnworks_api.generated.stock.models.get_warehouse_moves_by_binrack_response import GetWarehouseMovesByBinrackResponse
from linnworks_api.generated.stock.models.stock_get_warehouse_moves_by_binrack_request import StockGetWarehouseMovesByBinrackRequest
from linnworks_api.generated.stock.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.stock.Configuration(
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
with linnworks_api.generated.stock.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.stock.StockApi(api_client)
    stock_get_warehouse_moves_by_binrack_request = linnworks_api.generated.stock.StockGetWarehouseMovesByBinrackRequest() # StockGetWarehouseMovesByBinrackRequest | 

    try:
        # GetWarehouseMovesByBinrack
        api_response = api_instance.get_warehouse_moves_by_binrack(stock_get_warehouse_moves_by_binrack_request)
        print("The response of StockApi->get_warehouse_moves_by_binrack:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StockApi->get_warehouse_moves_by_binrack: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_get_warehouse_moves_by_binrack_request** | [**StockGetWarehouseMovesByBinrackRequest**](StockGetWarehouseMovesByBinrackRequest.md)|  | 

### Return type

[**GetWarehouseMovesByBinrackResponse**](GetWarehouseMovesByBinrackResponse.md)

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

# **rename_variation_group**
> rename_variation_group(stock_rename_variation_group_request)

RenameVariationGroup

Use this call to rename a variation group <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.stock
from linnworks_api.generated.stock.models.stock_rename_variation_group_request import StockRenameVariationGroupRequest
from linnworks_api.generated.stock.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.stock.Configuration(
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
with linnworks_api.generated.stock.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.stock.StockApi(api_client)
    stock_rename_variation_group_request = linnworks_api.generated.stock.StockRenameVariationGroupRequest() # StockRenameVariationGroupRequest | 

    try:
        # RenameVariationGroup
        api_instance.rename_variation_group(stock_rename_variation_group_request)
    except Exception as e:
        print("Exception when calling StockApi->rename_variation_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_rename_variation_group_request** | [**StockRenameVariationGroupRequest**](StockRenameVariationGroupRequest.md)|  | 

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

# **s_ku_exists**
> bool s_ku_exists(sku=sku)

SKUExists

Use this call to check if a SKU exists within Linnworks. <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>250</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.stock
from linnworks_api.generated.stock.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.stock.Configuration(
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
with linnworks_api.generated.stock.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.stock.StockApi(api_client)
    sku = 'sku_example' # str | The SKU you want to check exists. (optional)

    try:
        # SKUExists
        api_response = api_instance.s_ku_exists(sku=sku)
        print("The response of StockApi->s_ku_exists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StockApi->s_ku_exists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **str**| The SKU you want to check exists. | [optional] 

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

# **search_binracks**
> BinracksResponse search_binracks(stock_search_binracks_request)

SearchBinracks

Finds all binracks where an item can be placed. Filters out the result by group and binrack restrictions for a particular stock item.  List of BinRack Type Ids which should be searched can be supplied for a particular location, if null all binracktypes will be considered. You can get the list from Get Stock/GetBinrackTypes  The response will be ordered by where the system thinks the item should be moved. The logic is determined by one of the default behaviours of the system or by custom configuration of the warehouse stock flow <b>Permissions Required: </b> GlobalPermissions.Inventory.WarehouseManagementNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.stock
from linnworks_api.generated.stock.models.binracks_response import BinracksResponse
from linnworks_api.generated.stock.models.stock_search_binracks_request import StockSearchBinracksRequest
from linnworks_api.generated.stock.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.stock.Configuration(
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
with linnworks_api.generated.stock.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.stock.StockApi(api_client)
    stock_search_binracks_request = linnworks_api.generated.stock.StockSearchBinracksRequest() # StockSearchBinracksRequest | 

    try:
        # SearchBinracks
        api_response = api_instance.search_binracks(stock_search_binracks_request)
        print("The response of StockApi->search_binracks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StockApi->search_binracks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_search_binracks_request** | [**StockSearchBinracksRequest**](StockSearchBinracksRequest.md)|  | 

### Return type

[**BinracksResponse**](BinracksResponse.md)

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

# **search_variation_groups**
> GenericPagedResultVariationGroup search_variation_groups(search_type=search_type, search_text=search_text, page_number=page_number, entries_per_page=entries_per_page)

SearchVariationGroups

Use this call to search for a variation group <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.stock
from linnworks_api.generated.stock.models.generic_paged_result_variation_group import GenericPagedResultVariationGroup
from linnworks_api.generated.stock.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.stock.Configuration(
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
with linnworks_api.generated.stock.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.stock.StockApi(api_client)
    search_type = 'search_type_example' # str | The search method to use (optional)
    search_text = 'search_text_example' # str | The search term (either in part of full) (optional)
    page_number = 56 # int | The page number (e.g. 1). (optional)
    entries_per_page = 56 # int | The number of entries to return per page. (optional)

    try:
        # SearchVariationGroups
        api_response = api_instance.search_variation_groups(search_type=search_type, search_text=search_text, page_number=page_number, entries_per_page=entries_per_page)
        print("The response of StockApi->search_variation_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StockApi->search_variation_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_type** | **str**| The search method to use | [optional] 
 **search_text** | **str**| The search term (either in part of full) | [optional] 
 **page_number** | **int**| The page number (e.g. 1). | [optional] 
 **entries_per_page** | **int**| The number of entries to return per page. | [optional] 

### Return type

[**GenericPagedResultVariationGroup**](GenericPagedResultVariationGroup.md)

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

# **set_stock_level**
> List[StockItemLevel] set_stock_level(stock_set_stock_level_request)

SetStockLevel

Set the stock level of a list of stock items identified by its SKU to the value provided <b>Permissions Required: </b> GlobalPermissions.Inventory.Stock.StockWrite.ChangeStockLevelsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>250</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.stock
from linnworks_api.generated.stock.models.stock_item_level import StockItemLevel
from linnworks_api.generated.stock.models.stock_set_stock_level_request import StockSetStockLevelRequest
from linnworks_api.generated.stock.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.stock.Configuration(
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
with linnworks_api.generated.stock.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.stock.StockApi(api_client)
    stock_set_stock_level_request = linnworks_api.generated.stock.StockSetStockLevelRequest() # StockSetStockLevelRequest | 

    try:
        # SetStockLevel
        api_response = api_instance.set_stock_level(stock_set_stock_level_request)
        print("The response of StockApi->set_stock_level:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StockApi->set_stock_level: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_set_stock_level_request** | [**StockSetStockLevelRequest**](StockSetStockLevelRequest.md)|  | 

### Return type

[**List[StockItemLevel]**](StockItemLevel.md)

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

# **update_sku_group_identifier**
> object update_sku_group_identifier(request=request)

UpdateSkuGroupIdentifier

 <b>Permissions Required: </b> GlobalPermissions.Inventory.Stock.StockWriteNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.stock
from linnworks_api.generated.stock.models.update_sku_group_identifier_request import UpdateSkuGroupIdentifierRequest
from linnworks_api.generated.stock.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.stock.Configuration(
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
with linnworks_api.generated.stock.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.stock.StockApi(api_client)
    request = linnworks_api.generated.stock.UpdateSkuGroupIdentifierRequest() # UpdateSkuGroupIdentifierRequest |  (optional)

    try:
        # UpdateSkuGroupIdentifier
        api_response = api_instance.update_sku_group_identifier(request=request)
        print("The response of StockApi->update_sku_group_identifier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StockApi->update_sku_group_identifier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**UpdateSkuGroupIdentifierRequest**](UpdateSkuGroupIdentifierRequest.md)|  | [optional] 

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

# **update_stock_levels_bulk**
> UpdateStockLevelsBulkResponse update_stock_levels_bulk(request=request)

UpdateStockLevelsBulk

Allows the change of non batched / composite stock levels in build. Accepts either StockItemId or SKU and Stock location name or id <b>Permissions Required: </b> GlobalPermissions.Inventory.Stock.StockWrite.ChangeStockLevelsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.stock
from linnworks_api.generated.stock.models.update_stock_levels_bulk_request import UpdateStockLevelsBulkRequest
from linnworks_api.generated.stock.models.update_stock_levels_bulk_response import UpdateStockLevelsBulkResponse
from linnworks_api.generated.stock.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.stock.Configuration(
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
with linnworks_api.generated.stock.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.stock.StockApi(api_client)
    request = linnworks_api.generated.stock.UpdateStockLevelsBulkRequest() # UpdateStockLevelsBulkRequest |  (optional)

    try:
        # UpdateStockLevelsBulk
        api_response = api_instance.update_stock_levels_bulk(request=request)
        print("The response of StockApi->update_stock_levels_bulk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StockApi->update_stock_levels_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**UpdateStockLevelsBulkRequest**](UpdateStockLevelsBulkRequest.md)|  | [optional] 

### Return type

[**UpdateStockLevelsBulkResponse**](UpdateStockLevelsBulkResponse.md)

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

# **update_stock_levels_by_sku**
> List[StockItemLevel] update_stock_levels_by_sku(stock_update_stock_levels_by_sku_request)

UpdateStockLevelsBySKU

Change the stock level of a list of stock items by the provided value <b>Permissions Required: </b> GlobalPermissions.Inventory.Stock.StockWrite.ChangeStockLevelsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.stock
from linnworks_api.generated.stock.models.stock_item_level import StockItemLevel
from linnworks_api.generated.stock.models.stock_update_stock_levels_by_sku_request import StockUpdateStockLevelsBySKURequest
from linnworks_api.generated.stock.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.stock.Configuration(
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
with linnworks_api.generated.stock.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.stock.StockApi(api_client)
    stock_update_stock_levels_by_sku_request = linnworks_api.generated.stock.StockUpdateStockLevelsBySKURequest() # StockUpdateStockLevelsBySKURequest | 

    try:
        # UpdateStockLevelsBySKU
        api_response = api_instance.update_stock_levels_by_sku(stock_update_stock_levels_by_sku_request)
        print("The response of StockApi->update_stock_levels_by_sku:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StockApi->update_stock_levels_by_sku: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_update_stock_levels_by_sku_request** | [**StockUpdateStockLevelsBySKURequest**](StockUpdateStockLevelsBySKURequest.md)|  | 

### Return type

[**List[StockItemLevel]**](StockItemLevel.md)

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

# **update_stock_minimum_level**
> update_stock_minimum_level(stock_update_stock_minimum_level_request)

UpdateStockMinimumLevel

Use this call to update stock minimum level <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>250</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.stock
from linnworks_api.generated.stock.models.stock_update_stock_minimum_level_request import StockUpdateStockMinimumLevelRequest
from linnworks_api.generated.stock.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.stock.Configuration(
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
with linnworks_api.generated.stock.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.stock.StockApi(api_client)
    stock_update_stock_minimum_level_request = linnworks_api.generated.stock.StockUpdateStockMinimumLevelRequest() # StockUpdateStockMinimumLevelRequest | 

    try:
        # UpdateStockMinimumLevel
        api_instance.update_stock_minimum_level(stock_update_stock_minimum_level_request)
    except Exception as e:
        print("Exception when calling StockApi->update_stock_minimum_level: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_update_stock_minimum_level_request** | [**StockUpdateStockMinimumLevelRequest**](StockUpdateStockMinimumLevelRequest.md)|  | 

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

# **update_warehouse_move**
> GetWarehouseMoveResponse update_warehouse_move(request=request)

UpdateWarehouseMove

Use this call to update a stock move <b>Permissions Required: </b> GlobalPermissions.Inventory.WarehouseManagement.StockMoveNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.stock
from linnworks_api.generated.stock.models.get_warehouse_move_response import GetWarehouseMoveResponse
from linnworks_api.generated.stock.models.update_warehouse_move_request import UpdateWarehouseMoveRequest
from linnworks_api.generated.stock.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.stock.Configuration(
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
with linnworks_api.generated.stock.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.stock.StockApi(api_client)
    request = linnworks_api.generated.stock.UpdateWarehouseMoveRequest() # UpdateWarehouseMoveRequest |  (optional)

    try:
        # UpdateWarehouseMove
        api_response = api_instance.update_warehouse_move(request=request)
        print("The response of StockApi->update_warehouse_move:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StockApi->update_warehouse_move: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**UpdateWarehouseMoveRequest**](UpdateWarehouseMoveRequest.md)|  | [optional] 

### Return type

[**GetWarehouseMoveResponse**](GetWarehouseMoveResponse.md)

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

