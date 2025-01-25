# linnworks_api.generated.dashboards.DashboardsApi

All URIs are relative to *https://eu-ext.linnworks.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_inventory_location_categories_data**](DashboardsApi.md#get_inventory_location_categories_data) | **GET** /api/Dashboards/GetInventoryLocationCategoriesData | GetInventoryLocationCategoriesData
[**get_inventory_location_data**](DashboardsApi.md#get_inventory_location_data) | **GET** /api/Dashboards/GetInventoryLocationData | GetInventoryLocationData
[**get_inventory_location_products_data**](DashboardsApi.md#get_inventory_location_products_data) | **GET** /api/Dashboards/GetInventoryLocationProductsData | GetInventoryLocationProductsData
[**get_low_stock_level**](DashboardsApi.md#get_low_stock_level) | **GET** /api/Dashboards/GetLowStockLevel | GetLowStockLevel
[**get_performance_detail**](DashboardsApi.md#get_performance_detail) | **GET** /api/Dashboards/GetPerformanceDetail | GetPerformanceDetail
[**get_performance_table_data**](DashboardsApi.md#get_performance_table_data) | **GET** /api/Dashboards/GetPerformanceTableData | GetPerformanceTableData
[**get_top_products**](DashboardsApi.md#get_top_products) | **GET** /api/Dashboards/GetTopProducts | GetTopProducts


# **get_inventory_location_categories_data**
> List[StockCategoryLocation] get_inventory_location_categories_data(var_date=var_date, location_id=location_id)

GetInventoryLocationCategoriesData

Use this call to retrieve report about \"Stock info for categories in a specific location\" <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.dashboards
from linnworks_api.generated.dashboards.models.stock_category_location import StockCategoryLocation
from linnworks_api.generated.dashboards.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.dashboards.Configuration(
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
with linnworks_api.generated.dashboards.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.dashboards.DashboardsApi(api_client)
    var_date = '2013-10-20T19:20:30+01:00' # datetime | Used to specify report date or null for current period (optional)
    location_id = 'location_id_example' # str | Used to specify report location id (optional)

    try:
        # GetInventoryLocationCategoriesData
        api_response = api_instance.get_inventory_location_categories_data(var_date=var_date, location_id=location_id)
        print("The response of DashboardsApi->get_inventory_location_categories_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardsApi->get_inventory_location_categories_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_date** | **datetime**| Used to specify report date or null for current period | [optional] 
 **location_id** | **str**| Used to specify report location id | [optional] 

### Return type

[**List[StockCategoryLocation]**](StockCategoryLocation.md)

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

# **get_inventory_location_data**
> List[StatsStockItemLocation] get_inventory_location_data(var_date=var_date)

GetInventoryLocationData

Use this call to retrieve report about \"Stock info for locations\" <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.dashboards
from linnworks_api.generated.dashboards.models.stats_stock_item_location import StatsStockItemLocation
from linnworks_api.generated.dashboards.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.dashboards.Configuration(
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
with linnworks_api.generated.dashboards.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.dashboards.DashboardsApi(api_client)
    var_date = '2013-10-20T19:20:30+01:00' # datetime | Used to specify report date or null for current period (optional)

    try:
        # GetInventoryLocationData
        api_response = api_instance.get_inventory_location_data(var_date=var_date)
        print("The response of DashboardsApi->get_inventory_location_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardsApi->get_inventory_location_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_date** | **datetime**| Used to specify report date or null for current period | [optional] 

### Return type

[**List[StatsStockItemLocation]**](StatsStockItemLocation.md)

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

# **get_inventory_location_products_data**
> PagedStockCategoryLocationProductResult get_inventory_location_products_data(var_date=var_date, location_id=location_id, category_id=category_id, page_number=page_number, entries_per_page=entries_per_page)

GetInventoryLocationProductsData

Use this call to retrieve report about \"Stock info for products in a specific category and location\" <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>250</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.dashboards
from linnworks_api.generated.dashboards.models.paged_stock_category_location_product_result import PagedStockCategoryLocationProductResult
from linnworks_api.generated.dashboards.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.dashboards.Configuration(
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
with linnworks_api.generated.dashboards.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.dashboards.DashboardsApi(api_client)
    var_date = '2013-10-20T19:20:30+01:00' # datetime | Used to specify report date or null for current period (optional)
    location_id = 'location_id_example' # str | Used to specify report location id (optional)
    category_id = 'category_id_example' # str | Used to specify report category id (optional)
    page_number = 56 # int | Used to specify report page number (optional)
    entries_per_page = 56 # int | Used to specify number of entries per page in report (optional)

    try:
        # GetInventoryLocationProductsData
        api_response = api_instance.get_inventory_location_products_data(var_date=var_date, location_id=location_id, category_id=category_id, page_number=page_number, entries_per_page=entries_per_page)
        print("The response of DashboardsApi->get_inventory_location_products_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardsApi->get_inventory_location_products_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_date** | **datetime**| Used to specify report date or null for current period | [optional] 
 **location_id** | **str**| Used to specify report location id | [optional] 
 **category_id** | **str**| Used to specify report category id | [optional] 
 **page_number** | **int**| Used to specify report page number | [optional] 
 **entries_per_page** | **int**| Used to specify number of entries per page in report | [optional] 

### Return type

[**PagedStockCategoryLocationProductResult**](PagedStockCategoryLocationProductResult.md)

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

# **get_low_stock_level**
> List[LowStockLevel] get_low_stock_level(location_id=location_id, num_rows=num_rows)

GetLowStockLevel

Use this call to retrieve report about \"Low stock in location\" <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.dashboards
from linnworks_api.generated.dashboards.models.low_stock_level import LowStockLevel
from linnworks_api.generated.dashboards.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.dashboards.Configuration(
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
with linnworks_api.generated.dashboards.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.dashboards.DashboardsApi(api_client)
    location_id = 'location_id_example' # str | Used to specify report location id or null for combined (optional)
    num_rows = 56 # int | Used to specify number of returned rows (optional)

    try:
        # GetLowStockLevel
        api_response = api_instance.get_low_stock_level(location_id=location_id, num_rows=num_rows)
        print("The response of DashboardsApi->get_low_stock_level:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardsApi->get_low_stock_level: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| Used to specify report location id or null for combined | [optional] 
 **num_rows** | **int**| Used to specify number of returned rows | [optional] 

### Return type

[**List[LowStockLevel]**](LowStockLevel.md)

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

# **get_performance_detail**
> Dict[str, List[PerfomanceDetail]] get_performance_detail(period=period, time_scale=time_scale)

GetPerformanceDetail

Use this call to retrieve report about \"Performance through time chart\" <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.dashboards
from linnworks_api.generated.dashboards.models.perfomance_detail import PerfomanceDetail
from linnworks_api.generated.dashboards.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.dashboards.Configuration(
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
with linnworks_api.generated.dashboards.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.dashboards.DashboardsApi(api_client)
    period = 56 # int | Used to specify report number of months (optional)
    time_scale = 56 # int | time scale (optional)

    try:
        # GetPerformanceDetail
        api_response = api_instance.get_performance_detail(period=period, time_scale=time_scale)
        print("The response of DashboardsApi->get_performance_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardsApi->get_performance_detail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **period** | **int**| Used to specify report number of months | [optional] 
 **time_scale** | **int**| time scale | [optional] 

### Return type

**Dict[str, List[PerfomanceDetail]]**

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

# **get_performance_table_data**
> List[PerfomanceData] get_performance_table_data(period=period)

GetPerformanceTableData

Use this call to retrieve report about \"Performance table\" <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.dashboards
from linnworks_api.generated.dashboards.models.perfomance_data import PerfomanceData
from linnworks_api.generated.dashboards.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.dashboards.Configuration(
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
with linnworks_api.generated.dashboards.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.dashboards.DashboardsApi(api_client)
    period = 56 # int | Used to specify report number of months (optional)

    try:
        # GetPerformanceTableData
        api_response = api_instance.get_performance_table_data(period=period)
        print("The response of DashboardsApi->get_performance_table_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardsApi->get_performance_table_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **period** | **int**| Used to specify report number of months | [optional] 

### Return type

[**List[PerfomanceData]**](PerfomanceData.md)

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

# **get_top_products**
> List[TopProductData] get_top_products(type=type, period=period, num_rows=num_rows, order_status=order_status)

GetTopProducts

Use this call to retrieve report about \"Top ordered products\" for top \"10\" products <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.dashboards
from linnworks_api.generated.dashboards.models.top_product_data import TopProductData
from linnworks_api.generated.dashboards.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.dashboards.Configuration(
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
with linnworks_api.generated.dashboards.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.dashboards.DashboardsApi(api_client)
    type = 'type_example' # str | Used to specify type of report: 1 - group result by quantity, 2 - group result by turnover (optional)
    period = 56 # int | Used to specify report number of months (optional)
    num_rows = 56 # int | Number of rows required (optional)
    order_status = 56 # int | Order status (optional)

    try:
        # GetTopProducts
        api_response = api_instance.get_top_products(type=type, period=period, num_rows=num_rows, order_status=order_status)
        print("The response of DashboardsApi->get_top_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardsApi->get_top_products: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Used to specify type of report: 1 - group result by quantity, 2 - group result by turnover | [optional] 
 **period** | **int**| Used to specify report number of months | [optional] 
 **num_rows** | **int**| Number of rows required | [optional] 
 **order_status** | **int**| Order status | [optional] 

### Return type

[**List[TopProductData]**](TopProductData.md)

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

