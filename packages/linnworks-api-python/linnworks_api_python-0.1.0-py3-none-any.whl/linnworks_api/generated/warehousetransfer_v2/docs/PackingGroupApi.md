# linnworks_api.generated.warehousetransfer_v2.PackingGroupApi

All URIs are relative to *https://eu-api.linnworks.net/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_packing_groups_get**](PackingGroupApi.md#warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_packing_groups_get) | **GET** /warehousetransfer/fba-inbound/shipping-plans/{shippingPlanId}/packing-groups | Get


# **warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_packing_groups_get**
> List[GetPackingGroupModel] warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_packing_groups_get(shipping_plan_id)

Get

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_v2
from linnworks_api.generated.warehousetransfer_v2.models.get_packing_group_model import GetPackingGroupModel
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
    api_instance = linnworks_api.generated.warehousetransfer_v2.PackingGroupApi(api_client)
    shipping_plan_id = 56 # int | 

    try:
        # Get
        api_response = api_instance.warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_packing_groups_get(shipping_plan_id)
        print("The response of PackingGroupApi->warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_packing_groups_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PackingGroupApi->warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_packing_groups_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_plan_id** | **int**|  | 

### Return type

[**List[GetPackingGroupModel]**](GetPackingGroupModel.md)

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
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Server Error |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

