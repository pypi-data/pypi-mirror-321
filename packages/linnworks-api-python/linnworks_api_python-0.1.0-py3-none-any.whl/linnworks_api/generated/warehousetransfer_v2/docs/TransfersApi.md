# linnworks_api.generated.warehousetransfer_v2.TransfersApi

All URIs are relative to *https://eu-api.linnworks.net/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**warehousetransfer_transfers_id_get**](TransfersApi.md#warehousetransfer_transfers_id_get) | **GET** /warehousetransfer/transfers/{id} | GetTransferById


# **warehousetransfer_transfers_id_get**
> WarehouseTransferModel warehousetransfer_transfers_id_get(id)

GetTransferById

Retrieves a specific transfer by unique id

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_v2
from linnworks_api.generated.warehousetransfer_v2.models.warehouse_transfer_model import WarehouseTransferModel
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
    api_instance = linnworks_api.generated.warehousetransfer_v2.TransfersApi(api_client)
    id = 56 # int | Transfer unique id

    try:
        # GetTransferById
        api_response = api_instance.warehousetransfer_transfers_id_get(id)
        print("The response of TransfersApi->warehousetransfer_transfers_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransfersApi->warehousetransfer_transfers_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Transfer unique id | 

### Return type

[**WarehouseTransferModel**](WarehouseTransferModel.md)

### Authorization

[Linnworks](../README.md#Linnworks)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal server error |  -  |
**404** | Transfer not found |  -  |
**200** | Transfer retrieved |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

