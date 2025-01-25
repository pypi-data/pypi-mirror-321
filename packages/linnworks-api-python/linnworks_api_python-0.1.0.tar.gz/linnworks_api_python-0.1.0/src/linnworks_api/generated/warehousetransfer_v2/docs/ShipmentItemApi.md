# linnworks_api.generated.warehousetransfer_v2.ShipmentItemApi

All URIs are relative to *https://eu-api.linnworks.net/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_delete**](ShipmentItemApi.md#warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_delete) | **DELETE** /warehousetransfer/fba-inbound/shipping-plans/{shippingPlanId}/shipments/items | DeleteShipmentItem
[**warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_get**](ShipmentItemApi.md#warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_get) | **GET** /warehousetransfer/fba-inbound/shipping-plans/{shippingPlanId}/shipments/items | GetShipmentItems
[**warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_post**](ShipmentItemApi.md#warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_post) | **POST** /warehousetransfer/fba-inbound/shipping-plans/{shippingPlanId}/shipments/items | CreateShipmentItemBatch
[**warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_prep_instructions_label_owner_put**](ShipmentItemApi.md#warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_prep_instructions_label_owner_put) | **PUT** /warehousetransfer/fba-inbound/shipping-plans/{shippingPlanId}/shipments/items/prep-instructions/label-owner | UpdateShippingItemLabelOwner
[**warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_prep_instructions_prep_owner_put**](ShipmentItemApi.md#warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_prep_instructions_prep_owner_put) | **PUT** /warehousetransfer/fba-inbound/shipping-plans/{shippingPlanId}/shipments/items/prep-instructions/prep-owner | UpdateShippingItemWhoLabelPrep
[**warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_prep_instructions_put**](ShipmentItemApi.md#warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_prep_instructions_put) | **PUT** /warehousetransfer/fba-inbound/shipping-plans/{shippingPlanId}/shipments/items/prep-instructions | UpdateShipmentItemPrepInstruction
[**warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_shipment_item_id_put**](ShipmentItemApi.md#warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_shipment_item_id_put) | **PUT** /warehousetransfer/fba-inbound/shipping-plans/{shippingPlanId}/shipments/items/{shipmentItemId} | UpdateShipmentItem
[**warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_shipment_item_id_quantity_patch**](ShipmentItemApi.md#warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_shipment_item_id_quantity_patch) | **PATCH** /warehousetransfer/fba-inbound/shipping-plans/{shippingPlanId}/shipments/items/{shipmentItemId}/quantity | UpdateQuantity


# **warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_delete**
> warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_delete(shipping_plan_id, delete_shipment_item_request)

DeleteShipmentItem

Used to delete shipment items in batch

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_v2
from linnworks_api.generated.warehousetransfer_v2.models.delete_shipment_item_request import DeleteShipmentItemRequest
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
    api_instance = linnworks_api.generated.warehousetransfer_v2.ShipmentItemApi(api_client)
    shipping_plan_id = 'shipping_plan_id_example' # str | 
    delete_shipment_item_request = linnworks_api.generated.warehousetransfer_v2.DeleteShipmentItemRequest() # DeleteShipmentItemRequest | 

    try:
        # DeleteShipmentItem
        api_instance.warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_delete(shipping_plan_id, delete_shipment_item_request)
    except Exception as e:
        print("Exception when calling ShipmentItemApi->warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_plan_id** | **str**|  | 
 **delete_shipment_item_request** | [**DeleteShipmentItemRequest**](DeleteShipmentItemRequest.md)|  | 

### Return type

void (empty response body)

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
**204** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_get**
> List[ShipmentItemResponse] warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_get(shipping_plan_id, shipment_item_id=shipment_item_id)

GetShipmentItems

Used to get shipment items by shipping plan id

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_v2
from linnworks_api.generated.warehousetransfer_v2.models.shipment_item_response import ShipmentItemResponse
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
    api_instance = linnworks_api.generated.warehousetransfer_v2.ShipmentItemApi(api_client)
    shipping_plan_id = 56 # int | 
    shipment_item_id = [56] # List[int] |  (optional)

    try:
        # GetShipmentItems
        api_response = api_instance.warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_get(shipping_plan_id, shipment_item_id=shipment_item_id)
        print("The response of ShipmentItemApi->warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentItemApi->warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_plan_id** | **int**|  | 
 **shipment_item_id** | [**List[int]**](int.md)|  | [optional] 

### Return type

[**List[ShipmentItemResponse]**](ShipmentItemResponse.md)

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
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_post**
> List[ShipmentItemResponse] warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_post(shipping_plan_id, create_shipment_item_in_bulk_request)

CreateShipmentItemBatch

Used to create shipment items in batch

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_v2
from linnworks_api.generated.warehousetransfer_v2.models.create_shipment_item_in_bulk_request import CreateShipmentItemInBulkRequest
from linnworks_api.generated.warehousetransfer_v2.models.shipment_item_response import ShipmentItemResponse
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
    api_instance = linnworks_api.generated.warehousetransfer_v2.ShipmentItemApi(api_client)
    shipping_plan_id = 56 # int | 
    create_shipment_item_in_bulk_request = linnworks_api.generated.warehousetransfer_v2.CreateShipmentItemInBulkRequest() # CreateShipmentItemInBulkRequest | 

    try:
        # CreateShipmentItemBatch
        api_response = api_instance.warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_post(shipping_plan_id, create_shipment_item_in_bulk_request)
        print("The response of ShipmentItemApi->warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentItemApi->warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_plan_id** | **int**|  | 
 **create_shipment_item_in_bulk_request** | [**CreateShipmentItemInBulkRequest**](CreateShipmentItemInBulkRequest.md)|  | 

### Return type

[**List[ShipmentItemResponse]**](ShipmentItemResponse.md)

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

# **warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_prep_instructions_label_owner_put**
> ShipmentItemResponse warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_prep_instructions_label_owner_put(shipping_plan_id, update_shipment_item_label_owner_request=update_shipment_item_label_owner_request)

UpdateShippingItemLabelOwner

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_v2
from linnworks_api.generated.warehousetransfer_v2.models.shipment_item_response import ShipmentItemResponse
from linnworks_api.generated.warehousetransfer_v2.models.update_shipment_item_label_owner_request import UpdateShipmentItemLabelOwnerRequest
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
    api_instance = linnworks_api.generated.warehousetransfer_v2.ShipmentItemApi(api_client)
    shipping_plan_id = 56 # int | 
    update_shipment_item_label_owner_request = linnworks_api.generated.warehousetransfer_v2.UpdateShipmentItemLabelOwnerRequest() # UpdateShipmentItemLabelOwnerRequest |  (optional)

    try:
        # UpdateShippingItemLabelOwner
        api_response = api_instance.warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_prep_instructions_label_owner_put(shipping_plan_id, update_shipment_item_label_owner_request=update_shipment_item_label_owner_request)
        print("The response of ShipmentItemApi->warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_prep_instructions_label_owner_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentItemApi->warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_prep_instructions_label_owner_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_plan_id** | **int**|  | 
 **update_shipment_item_label_owner_request** | [**UpdateShipmentItemLabelOwnerRequest**](UpdateShipmentItemLabelOwnerRequest.md)|  | [optional] 

### Return type

[**ShipmentItemResponse**](ShipmentItemResponse.md)

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
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_prep_instructions_prep_owner_put**
> warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_prep_instructions_prep_owner_put(shipping_plan_id, update_shipment_item_prep_instruction_owner_request)

UpdateShippingItemWhoLabelPrep

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_v2
from linnworks_api.generated.warehousetransfer_v2.models.update_shipment_item_prep_instruction_owner_request import UpdateShipmentItemPrepInstructionOwnerRequest
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
    api_instance = linnworks_api.generated.warehousetransfer_v2.ShipmentItemApi(api_client)
    shipping_plan_id = 'shipping_plan_id_example' # str | 
    update_shipment_item_prep_instruction_owner_request = linnworks_api.generated.warehousetransfer_v2.UpdateShipmentItemPrepInstructionOwnerRequest() # UpdateShipmentItemPrepInstructionOwnerRequest | 

    try:
        # UpdateShippingItemWhoLabelPrep
        api_instance.warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_prep_instructions_prep_owner_put(shipping_plan_id, update_shipment_item_prep_instruction_owner_request)
    except Exception as e:
        print("Exception when calling ShipmentItemApi->warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_prep_instructions_prep_owner_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_plan_id** | **str**|  | 
 **update_shipment_item_prep_instruction_owner_request** | [**UpdateShipmentItemPrepInstructionOwnerRequest**](UpdateShipmentItemPrepInstructionOwnerRequest.md)|  | 

### Return type

void (empty response body)

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
**204** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_prep_instructions_put**
> List[ShipmentItemPrepInstructionModel] warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_prep_instructions_put(shipping_plan_id, update_shipment_item_prep_instruction_request)

UpdateShipmentItemPrepInstruction

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_v2
from linnworks_api.generated.warehousetransfer_v2.models.shipment_item_prep_instruction_model import ShipmentItemPrepInstructionModel
from linnworks_api.generated.warehousetransfer_v2.models.update_shipment_item_prep_instruction_request import UpdateShipmentItemPrepInstructionRequest
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
    api_instance = linnworks_api.generated.warehousetransfer_v2.ShipmentItemApi(api_client)
    shipping_plan_id = 'shipping_plan_id_example' # str | 
    update_shipment_item_prep_instruction_request = linnworks_api.generated.warehousetransfer_v2.UpdateShipmentItemPrepInstructionRequest() # UpdateShipmentItemPrepInstructionRequest | 

    try:
        # UpdateShipmentItemPrepInstruction
        api_response = api_instance.warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_prep_instructions_put(shipping_plan_id, update_shipment_item_prep_instruction_request)
        print("The response of ShipmentItemApi->warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_prep_instructions_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentItemApi->warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_prep_instructions_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_plan_id** | **str**|  | 
 **update_shipment_item_prep_instruction_request** | [**UpdateShipmentItemPrepInstructionRequest**](UpdateShipmentItemPrepInstructionRequest.md)|  | 

### Return type

[**List[ShipmentItemPrepInstructionModel]**](ShipmentItemPrepInstructionModel.md)

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

# **warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_shipment_item_id_put**
> warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_shipment_item_id_put(shipping_plan_id, shipment_item_id, update_shipment_item_request_input)

UpdateShipmentItem

Used to update shipment item

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_v2
from linnworks_api.generated.warehousetransfer_v2.models.update_shipment_item_request_input import UpdateShipmentItemRequestInput
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
    api_instance = linnworks_api.generated.warehousetransfer_v2.ShipmentItemApi(api_client)
    shipping_plan_id = 56 # int | 
    shipment_item_id = 56 # int | 
    update_shipment_item_request_input = linnworks_api.generated.warehousetransfer_v2.UpdateShipmentItemRequestInput() # UpdateShipmentItemRequestInput | 

    try:
        # UpdateShipmentItem
        api_instance.warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_shipment_item_id_put(shipping_plan_id, shipment_item_id, update_shipment_item_request_input)
    except Exception as e:
        print("Exception when calling ShipmentItemApi->warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_shipment_item_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_plan_id** | **int**|  | 
 **shipment_item_id** | **int**|  | 
 **update_shipment_item_request_input** | [**UpdateShipmentItemRequestInput**](UpdateShipmentItemRequestInput.md)|  | 

### Return type

void (empty response body)

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
**204** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_shipment_item_id_quantity_patch**
> ShipmentItemResponse warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_shipment_item_id_quantity_patch(shipping_plan_id, shipment_item_id, body=body)

UpdateQuantity

### Example

* Api Key Authentication (Linnworks):

```python
import linnworks_api.generated.warehousetransfer_v2
from linnworks_api.generated.warehousetransfer_v2.models.shipment_item_response import ShipmentItemResponse
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
    api_instance = linnworks_api.generated.warehousetransfer_v2.ShipmentItemApi(api_client)
    shipping_plan_id = 56 # int | 
    shipment_item_id = 56 # int | 
    body = 56 # int |  (optional)

    try:
        # UpdateQuantity
        api_response = api_instance.warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_shipment_item_id_quantity_patch(shipping_plan_id, shipment_item_id, body=body)
        print("The response of ShipmentItemApi->warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_shipment_item_id_quantity_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentItemApi->warehousetransfer_fba_inbound_shipping_plans_shipping_plan_id_shipments_items_shipment_item_id_quantity_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_plan_id** | **int**|  | 
 **shipment_item_id** | **int**|  | 
 **body** | **int**|  | [optional] 

### Return type

[**ShipmentItemResponse**](ShipmentItemResponse.md)

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

