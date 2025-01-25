# linnworks_api.generated.postsale.PostSaleApi

All URIs are relative to *https://eu-ext.linnworks.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cancellation**](PostSaleApi.md#create_cancellation) | **POST** /api/PostSale/CreateCancellation | CreateCancellation
[**get_cancellation_options**](PostSaleApi.md#get_cancellation_options) | **GET** /api/PostSale/GetCancellationOptions | GetCancellationOptions


# **create_cancellation**
> ValidatedCancellation create_cancellation(post_sale_create_cancellation_request)

CreateCancellation

This method is used to further validate and create a cancellation in Linnworks, as well as submit it to the channel where this is requested <b>Permissions Required: </b> GlobalPermissions.OrderBook.OpenOrders.CancellationsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.postsale
from linnworks_api.generated.postsale.models.post_sale_create_cancellation_request import PostSaleCreateCancellationRequest
from linnworks_api.generated.postsale.models.validated_cancellation import ValidatedCancellation
from linnworks_api.generated.postsale.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.postsale.Configuration(
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
with linnworks_api.generated.postsale.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.postsale.PostSaleApi(api_client)
    post_sale_create_cancellation_request = linnworks_api.generated.postsale.PostSaleCreateCancellationRequest() # PostSaleCreateCancellationRequest | 

    try:
        # CreateCancellation
        api_response = api_instance.create_cancellation(post_sale_create_cancellation_request)
        print("The response of PostSaleApi->create_cancellation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostSaleApi->create_cancellation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_sale_create_cancellation_request** | [**PostSaleCreateCancellationRequest**](PostSaleCreateCancellationRequest.md)|  | 

### Return type

[**ValidatedCancellation**](ValidatedCancellation.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cancellation_options**
> CancellationOptions get_cancellation_options(order_id=order_id)

GetCancellationOptions

This method is used to validate whether a channel cancellation can be submitted for a given order <b>Permissions Required: </b> GlobalPermissions.OrderBook.OpenOrders.CancellationsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.postsale
from linnworks_api.generated.postsale.models.cancellation_options import CancellationOptions
from linnworks_api.generated.postsale.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.postsale.Configuration(
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
with linnworks_api.generated.postsale.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.postsale.PostSaleApi(api_client)
    order_id = 'order_id_example' # str | The relevant order ID (optional)

    try:
        # GetCancellationOptions
        api_response = api_instance.get_cancellation_options(order_id=order_id)
        print("The response of PostSaleApi->get_cancellation_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostSaleApi->get_cancellation_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| The relevant order ID | [optional] 

### Return type

[**CancellationOptions**](CancellationOptions.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

