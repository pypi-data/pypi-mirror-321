# linnworks_api.generated.warehousetransfer_new.FbaShipmentItemBatchApi

All URIs are relative to *https://eu-api.linnworks.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipmentitems_batches_post**](FbaShipmentItemBatchApi.md#warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipmentitems_batches_post) | **POST** /warehousetransfer/fbainbound/shippingplans/{shippingPlanId}/shipments/shipmentitems/batches | AddItemBatch


# **warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipmentitems_batches_post**
> bool warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipmentitems_batches_post(shipping_plan_id, add_shipment_item_batches_request=add_shipment_item_batches_request)

AddItemBatch

Deprecated - please use v2 - [API Docs v2](https://apidocs.linnworks.net/v2/)

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_new
from linnworks_api.generated.warehousetransfer_new.models.add_shipment_item_batches_request import AddShipmentItemBatchesRequest
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
    api_instance = linnworks_api.generated.warehousetransfer_new.FbaShipmentItemBatchApi(api_client)
    shipping_plan_id = 56 # int | 
    add_shipment_item_batches_request = linnworks_api.generated.warehousetransfer_new.AddShipmentItemBatchesRequest() # AddShipmentItemBatchesRequest |  (optional)

    try:
        # AddItemBatch
        api_response = api_instance.warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipmentitems_batches_post(shipping_plan_id, add_shipment_item_batches_request=add_shipment_item_batches_request)
        print("The response of FbaShipmentItemBatchApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipmentitems_batches_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FbaShipmentItemBatchApi->warehousetransfer_fbainbound_shippingplans_shipping_plan_id_shipments_shipmentitems_batches_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_plan_id** | **int**|  | 
 **add_shipment_item_batches_request** | [**AddShipmentItemBatchesRequest**](AddShipmentItemBatchesRequest.md)|  | [optional] 

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
**201** | Success |  -  |
**204** | Success |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

