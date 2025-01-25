# linnworks_api.generated.warehousetransfer_new.FbaTransferCardsApi

All URIs are relative to *https://eu-api.linnworks.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**warehousetransfer_fbainbound_fbatransfercards_archived_shipments_put**](FbaTransferCardsApi.md#warehousetransfer_fbainbound_fbatransfercards_archived_shipments_put) | **PUT** /warehousetransfer/fbainbound/fbatransfercards/archivedShipments | ArchiveClosedShipments
[**warehousetransfer_fbainbound_fbatransfercards_metadata_get**](FbaTransferCardsApi.md#warehousetransfer_fbainbound_fbatransfercards_metadata_get) | **GET** /warehousetransfer/fbainbound/fbatransfercards/metadata | GetMetaData
[**warehousetransfer_fbainbound_fbatransfercards_request_updates_put**](FbaTransferCardsApi.md#warehousetransfer_fbainbound_fbatransfercards_request_updates_put) | **PUT** /warehousetransfer/fbainbound/fbatransfercards/requestUpdates | RequestShipmentCardsUpdate
[**warehousetransfer_fbainbound_fbatransfercards_shipmentcards_get**](FbaTransferCardsApi.md#warehousetransfer_fbainbound_fbatransfercards_shipmentcards_get) | **GET** /warehousetransfer/fbainbound/fbatransfercards/shipmentcards | GetShipmentCards
[**warehousetransfer_fbainbound_fbatransfercards_shippingplancards_get**](FbaTransferCardsApi.md#warehousetransfer_fbainbound_fbatransfercards_shippingplancards_get) | **GET** /warehousetransfer/fbainbound/fbatransfercards/shippingplancards | GetShippingPlanCards


# **warehousetransfer_fbainbound_fbatransfercards_archived_shipments_put**
> warehousetransfer_fbainbound_fbatransfercards_archived_shipments_put(archive_closed_shipments_request=archive_closed_shipments_request)

ArchiveClosedShipments

Deprecated - please use v2 - [API Docs v2](https://apidocs.linnworks.net/v2/)

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.archive_closed_shipments_request import ArchiveClosedShipmentsRequest
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
    api_instance = linnworks_api.generated.warehousetransfer_new.FbaTransferCardsApi(api_client)
    archive_closed_shipments_request = linnworks_api.generated.warehousetransfer_new.ArchiveClosedShipmentsRequest() # ArchiveClosedShipmentsRequest |  (optional)

    try:
        # ArchiveClosedShipments
        api_instance.warehousetransfer_fbainbound_fbatransfercards_archived_shipments_put(archive_closed_shipments_request=archive_closed_shipments_request)
    except Exception as e:
        print("Exception when calling FbaTransferCardsApi->warehousetransfer_fbainbound_fbatransfercards_archived_shipments_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **archive_closed_shipments_request** | [**ArchiveClosedShipmentsRequest**](ArchiveClosedShipmentsRequest.md)|  | [optional] 

### Return type

void (empty response body)

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

# **warehousetransfer_fbainbound_fbatransfercards_metadata_get**
> GetViewMetaDataResponse warehousetransfer_fbainbound_fbatransfercards_metadata_get()

GetMetaData

Deprecated - please use v2 - [API Docs v2](https://apidocs.linnworks.net/v2/)

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.get_view_meta_data_response import GetViewMetaDataResponse
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
    api_instance = linnworks_api.generated.warehousetransfer_new.FbaTransferCardsApi(api_client)

    try:
        # GetMetaData
        api_response = api_instance.warehousetransfer_fbainbound_fbatransfercards_metadata_get()
        print("The response of FbaTransferCardsApi->warehousetransfer_fbainbound_fbatransfercards_metadata_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FbaTransferCardsApi->warehousetransfer_fbainbound_fbatransfercards_metadata_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetViewMetaDataResponse**](GetViewMetaDataResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehousetransfer_fbainbound_fbatransfercards_request_updates_put**
> warehousetransfer_fbainbound_fbatransfercards_request_updates_put()

RequestShipmentCardsUpdate

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
    api_instance = linnworks_api.generated.warehousetransfer_new.FbaTransferCardsApi(api_client)

    try:
        # RequestShipmentCardsUpdate
        api_instance.warehousetransfer_fbainbound_fbatransfercards_request_updates_put()
    except Exception as e:
        print("Exception when calling FbaTransferCardsApi->warehousetransfer_fbainbound_fbatransfercards_request_updates_put: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**201** | Success |  -  |
**204** | Success |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehousetransfer_fbainbound_fbatransfercards_shipmentcards_get**
> warehousetransfer_fbainbound_fbatransfercards_shipmentcards_get()

GetShipmentCards

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
    api_instance = linnworks_api.generated.warehousetransfer_new.FbaTransferCardsApi(api_client)

    try:
        # GetShipmentCards
        api_instance.warehousetransfer_fbainbound_fbatransfercards_shipmentcards_get()
    except Exception as e:
        print("Exception when calling FbaTransferCardsApi->warehousetransfer_fbainbound_fbatransfercards_shipmentcards_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**201** | Success |  -  |
**204** | Success |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehousetransfer_fbainbound_fbatransfercards_shippingplancards_get**
> List[GetShippingPlanCardsResponse] warehousetransfer_fbainbound_fbatransfercards_shippingplancards_get()

GetShippingPlanCards

Deprecated - please use v2 - [API Docs v2](https://apidocs.linnworks.net/v2/)

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.get_shipping_plan_cards_response import GetShippingPlanCardsResponse
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
    api_instance = linnworks_api.generated.warehousetransfer_new.FbaTransferCardsApi(api_client)

    try:
        # GetShippingPlanCards
        api_response = api_instance.warehousetransfer_fbainbound_fbatransfercards_shippingplancards_get()
        print("The response of FbaTransferCardsApi->warehousetransfer_fbainbound_fbatransfercards_shippingplancards_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FbaTransferCardsApi->warehousetransfer_fbainbound_fbatransfercards_shippingplancards_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GetShippingPlanCardsResponse]**](GetShippingPlanCardsResponse.md)

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

