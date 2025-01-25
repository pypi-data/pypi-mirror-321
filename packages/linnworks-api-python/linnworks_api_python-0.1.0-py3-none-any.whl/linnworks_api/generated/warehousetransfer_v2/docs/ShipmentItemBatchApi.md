# linnworks_api.generated.warehousetransfer_v2.ShipmentItemBatchApi

All URIs are relative to *https://eu-api.linnworks.net/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_batches_post**](ShipmentItemBatchApi.md#warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_batches_post) | **POST** /warehousetransfer/fba-inbound/shipping-plans/{shippingPlanId}/shipments/items/batches | AddFbaItemBatch


# **warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_batches_post**
> bool warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_batches_post(shipping_plan_id, add_fba_item_batch_request_input)

AddFbaItemBatch

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_v2
from linnworks_api.generated.warehousetransfer_v2.models.add_fba_item_batch_request_input import AddFbaItemBatchRequestInput
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
    api_instance = linnworks_api.generated.warehousetransfer_v2.ShipmentItemBatchApi(api_client)
    shipping_plan_id = 56 # int | 
    add_fba_item_batch_request_input = linnworks_api.generated.warehousetransfer_v2.AddFbaItemBatchRequestInput() # AddFbaItemBatchRequestInput | 

    try:
        # AddFbaItemBatch
        api_response = api_instance.warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_batches_post(shipping_plan_id, add_fba_item_batch_request_input)
        print("The response of ShipmentItemBatchApi->warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_batches_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentItemBatchApi->warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_batches_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_plan_id** | **int**|  | 
 **add_fba_item_batch_request_input** | [**AddFbaItemBatchRequestInput**](AddFbaItemBatchRequestInput.md)|  | 

### Return type

**bool**

### Authorization

[Linnworks](../README.md#Linnworks)

### HTTP request headers

 - **Content-Type**: application/json-patch+json; x-api-version=2.0, application/json; x-api-version=2.0, text/json; x-api-version=2.0, application/*+json; x-api-version=2.0
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**201** | Success |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

