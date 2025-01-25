# linnworks_api.generated.listings.ListingsApi

All URIs are relative to *https://eu-ext.linnworks.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_listing_bulk_operation**](ListingsApi.md#cancel_listing_bulk_operation) | **POST** /api/Listings/CancelListingBulkOperation | CancelListingBulkOperation
[**create_amazon_configurators**](ListingsApi.md#create_amazon_configurators) | **POST** /api/Listings/CreateAmazonConfigurators | CreateAmazonConfigurators
[**create_amazon_templates**](ListingsApi.md#create_amazon_templates) | **POST** /api/Listings/CreateAmazonTemplates | CreateAmazonTemplates
[**create_bigcommerce_configurators**](ListingsApi.md#create_bigcommerce_configurators) | **POST** /api/Listings/CreateBigcommerceConfigurators | CreateBigcommerceConfigurators
[**create_bigcommerce_templates**](ListingsApi.md#create_bigcommerce_templates) | **POST** /api/Listings/CreateBigcommerceTemplates | CreateBigcommerceTemplates
[**create_ebay_templates**](ListingsApi.md#create_ebay_templates) | **POST** /api/Listings/CreateEbayTemplates | CreateEbayTemplates
[**create_magento_configurators**](ListingsApi.md#create_magento_configurators) | **POST** /api/Listings/CreateMagentoConfigurators | CreateMagentoConfigurators
[**create_magento_templates**](ListingsApi.md#create_magento_templates) | **POST** /api/Listings/CreateMagentoTemplates | CreateMagentoTemplates
[**create_templates_from_view_in_bulk**](ListingsApi.md#create_templates_from_view_in_bulk) | **POST** /api/Listings/CreateTemplatesFromViewInBulk | CreateTemplatesFromViewInBulk
[**createe_bay_configurators**](ListingsApi.md#createe_bay_configurators) | **POST** /api/Listings/CreateeBayConfigurators | CreateeBayConfigurators
[**delete_amazon_configurators**](ListingsApi.md#delete_amazon_configurators) | **POST** /api/Listings/DeleteAmazonConfigurators | DeleteAmazonConfigurators
[**delete_amazon_templates**](ListingsApi.md#delete_amazon_templates) | **POST** /api/Listings/DeleteAmazonTemplates | DeleteAmazonTemplates
[**delete_bigcommerce_configurators**](ListingsApi.md#delete_bigcommerce_configurators) | **POST** /api/Listings/DeleteBigcommerceConfigurators | DeleteBigcommerceConfigurators
[**delete_bigcommerce_templates**](ListingsApi.md#delete_bigcommerce_templates) | **POST** /api/Listings/DeleteBigcommerceTemplates | DeleteBigcommerceTemplates
[**delete_ebay_templates**](ListingsApi.md#delete_ebay_templates) | **POST** /api/Listings/DeleteEbayTemplates | DeleteEbayTemplates
[**delete_magento_configurators**](ListingsApi.md#delete_magento_configurators) | **POST** /api/Listings/DeleteMagentoConfigurators | DeleteMagentoConfigurators
[**delete_magento_templates**](ListingsApi.md#delete_magento_templates) | **POST** /api/Listings/DeleteMagentoTemplates | DeleteMagentoTemplates
[**deletee_bay_configurators**](ListingsApi.md#deletee_bay_configurators) | **POST** /api/Listings/DeleteeBayConfigurators | DeleteeBayConfigurators
[**end_listings_pending_relist**](ListingsApi.md#end_listings_pending_relist) | **POST** /api/Listings/EndListingsPendingRelist | EndListingsPendingRelist
[**get_amazon_configurators**](ListingsApi.md#get_amazon_configurators) | **GET** /api/Listings/GetAmazonConfigurators | GetAmazonConfigurators
[**get_amazon_templates**](ListingsApi.md#get_amazon_templates) | **POST** /api/Listings/GetAmazonTemplates | GetAmazonTemplates
[**get_big_commerce_templates**](ListingsApi.md#get_big_commerce_templates) | **POST** /api/Listings/GetBigCommerceTemplates | GetBigCommerceTemplates
[**get_bigcommerce_configurators**](ListingsApi.md#get_bigcommerce_configurators) | **GET** /api/Listings/GetBigcommerceConfigurators | GetBigcommerceConfigurators
[**get_ebay_listing_operations**](ListingsApi.md#get_ebay_listing_operations) | **GET** /api/Listings/GetEbayListingOperations | GetEbayListingOperations
[**get_magento_configurators**](ListingsApi.md#get_magento_configurators) | **GET** /api/Listings/GetMagentoConfigurators | GetMagentoConfigurators
[**get_magento_templates**](ListingsApi.md#get_magento_templates) | **POST** /api/Listings/GetMagentoTemplates | GetMagentoTemplates
[**gete_bay_configurators**](ListingsApi.md#gete_bay_configurators) | **GET** /api/Listings/GeteBayConfigurators | GeteBayConfigurators
[**gete_bay_templates**](ListingsApi.md#gete_bay_templates) | **POST** /api/Listings/GeteBayTemplates | GeteBayTemplates
[**process_amazon_listings**](ListingsApi.md#process_amazon_listings) | **POST** /api/Listings/ProcessAmazonListings | ProcessAmazonListings
[**process_bigcommerce_listings**](ListingsApi.md#process_bigcommerce_listings) | **POST** /api/Listings/ProcessBigcommerceListings | ProcessBigcommerceListings
[**process_magento_listings**](ListingsApi.md#process_magento_listings) | **POST** /api/Listings/ProcessMagentoListings | ProcessMagentoListings
[**processe_bay_listings**](ListingsApi.md#processe_bay_listings) | **POST** /api/Listings/ProcesseBayListings | ProcesseBayListings
[**set_listing_strike_off_state**](ListingsApi.md#set_listing_strike_off_state) | **POST** /api/Listings/SetListingStrikeOffState | SetListingStrikeOffState
[**update_amazon_configurators**](ListingsApi.md#update_amazon_configurators) | **POST** /api/Listings/UpdateAmazonConfigurators | UpdateAmazonConfigurators
[**update_bigcommerce_configurators**](ListingsApi.md#update_bigcommerce_configurators) | **POST** /api/Listings/UpdateBigcommerceConfigurators | UpdateBigcommerceConfigurators
[**update_magento_configurators**](ListingsApi.md#update_magento_configurators) | **POST** /api/Listings/UpdateMagentoConfigurators | UpdateMagentoConfigurators
[**updatee_bay_configurators**](ListingsApi.md#updatee_bay_configurators) | **POST** /api/Listings/UpdateeBayConfigurators | UpdateeBayConfigurators


# **cancel_listing_bulk_operation**
> object cancel_listing_bulk_operation(listings_cancel_listing_bulk_operation_request)

CancelListingBulkOperation

Use this call to cancel ebay listing bulk creation operations <b>Permissions Required: </b> GlobalPermissions.Settings.ListingConfigurators.GetListingConfiguratorsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.listings
from linnworks_api.generated.listings.models.listings_cancel_listing_bulk_operation_request import ListingsCancelListingBulkOperationRequest
from linnworks_api.generated.listings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.listings.Configuration(
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
with linnworks_api.generated.listings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.listings.ListingsApi(api_client)
    listings_cancel_listing_bulk_operation_request = linnworks_api.generated.listings.ListingsCancelListingBulkOperationRequest() # ListingsCancelListingBulkOperationRequest | 

    try:
        # CancelListingBulkOperation
        api_response = api_instance.cancel_listing_bulk_operation(listings_cancel_listing_bulk_operation_request)
        print("The response of ListingsApi->cancel_listing_bulk_operation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListingsApi->cancel_listing_bulk_operation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listings_cancel_listing_bulk_operation_request** | [**ListingsCancelListingBulkOperationRequest**](ListingsCancelListingBulkOperationRequest.md)|  | 

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

# **create_amazon_configurators**
> create_amazon_configurators(listings_create_amazon_configurators_request)

CreateAmazonConfigurators

Use this call to create Amazon configurators.                A configurator hosts common details for listings such as listing type, return policy, payment methods, shipping info, attributes, listing categories, etc. Configurators offer an efficient way of creating listings in bulk that follow a common theme. The same configurator can be used to list multiple items that share common details. To find out more about configurators you can visit our [documentation](https://docs.linnworks.com/articles/#!documentation/configurators) <b>Permissions Required: </b> GlobalPermissions.Settings.ListingConfigurators.EditListingConfiguratorsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.listings
from linnworks_api.generated.listings.models.listings_create_amazon_configurators_request import ListingsCreateAmazonConfiguratorsRequest
from linnworks_api.generated.listings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.listings.Configuration(
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
with linnworks_api.generated.listings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.listings.ListingsApi(api_client)
    listings_create_amazon_configurators_request = linnworks_api.generated.listings.ListingsCreateAmazonConfiguratorsRequest() # ListingsCreateAmazonConfiguratorsRequest | 

    try:
        # CreateAmazonConfigurators
        api_instance.create_amazon_configurators(listings_create_amazon_configurators_request)
    except Exception as e:
        print("Exception when calling ListingsApi->create_amazon_configurators: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listings_create_amazon_configurators_request** | [**ListingsCreateAmazonConfiguratorsRequest**](ListingsCreateAmazonConfiguratorsRequest.md)|  | 

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

# **create_amazon_templates**
> PagedResultAmazonListing create_amazon_templates(listings_create_amazon_templates_request)

CreateAmazonTemplates

Use this call to return a template based on the configurator setting you have requested. This allows you to see the template which can then be  retuned to the ProcessAmazonListing endpoint which will build the listing. <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.listings
from linnworks_api.generated.listings.models.listings_create_amazon_templates_request import ListingsCreateAmazonTemplatesRequest
from linnworks_api.generated.listings.models.paged_result_amazon_listing import PagedResultAmazonListing
from linnworks_api.generated.listings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.listings.Configuration(
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
with linnworks_api.generated.listings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.listings.ListingsApi(api_client)
    listings_create_amazon_templates_request = linnworks_api.generated.listings.ListingsCreateAmazonTemplatesRequest() # ListingsCreateAmazonTemplatesRequest | 

    try:
        # CreateAmazonTemplates
        api_response = api_instance.create_amazon_templates(listings_create_amazon_templates_request)
        print("The response of ListingsApi->create_amazon_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListingsApi->create_amazon_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listings_create_amazon_templates_request** | [**ListingsCreateAmazonTemplatesRequest**](ListingsCreateAmazonTemplatesRequest.md)|  | 

### Return type

[**PagedResultAmazonListing**](PagedResultAmazonListing.md)

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

# **create_bigcommerce_configurators**
> create_bigcommerce_configurators(listings_create_bigcommerce_configurators_request)

CreateBigcommerceConfigurators

Use this call to create BigCommerce configurators.                A configurator hosts common details for listings such as listing type, return policy, payment methods, shipping info, attributes, listing categories, etc. Configurators offer an efficient way of creating listings in bulk that follow a common theme. The same configurator can be used to list multiple items that share common details. To find out more about configurators you can visit our [documentation](https://docs.linnworks.com/articles/#!documentation/configurators) <b>Permissions Required: </b> GlobalPermissions.Settings.ListingConfigurators.EditListingConfiguratorsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.listings
from linnworks_api.generated.listings.models.listings_create_bigcommerce_configurators_request import ListingsCreateBigcommerceConfiguratorsRequest
from linnworks_api.generated.listings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.listings.Configuration(
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
with linnworks_api.generated.listings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.listings.ListingsApi(api_client)
    listings_create_bigcommerce_configurators_request = linnworks_api.generated.listings.ListingsCreateBigcommerceConfiguratorsRequest() # ListingsCreateBigcommerceConfiguratorsRequest | 

    try:
        # CreateBigcommerceConfigurators
        api_instance.create_bigcommerce_configurators(listings_create_bigcommerce_configurators_request)
    except Exception as e:
        print("Exception when calling ListingsApi->create_bigcommerce_configurators: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listings_create_bigcommerce_configurators_request** | [**ListingsCreateBigcommerceConfiguratorsRequest**](ListingsCreateBigcommerceConfiguratorsRequest.md)|  | 

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

# **create_bigcommerce_templates**
> PagedResultBigCommerceListing create_bigcommerce_templates(listings_create_bigcommerce_templates_request)

CreateBigcommerceTemplates

Use this call to return a template based on the configurator setting you have requested. This allows you to see the template which can then be  retuned to the ProcessBigCommerceListing endpoint which will build the listing. <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.listings
from linnworks_api.generated.listings.models.listings_create_bigcommerce_templates_request import ListingsCreateBigcommerceTemplatesRequest
from linnworks_api.generated.listings.models.paged_result_big_commerce_listing import PagedResultBigCommerceListing
from linnworks_api.generated.listings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.listings.Configuration(
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
with linnworks_api.generated.listings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.listings.ListingsApi(api_client)
    listings_create_bigcommerce_templates_request = linnworks_api.generated.listings.ListingsCreateBigcommerceTemplatesRequest() # ListingsCreateBigcommerceTemplatesRequest | 

    try:
        # CreateBigcommerceTemplates
        api_response = api_instance.create_bigcommerce_templates(listings_create_bigcommerce_templates_request)
        print("The response of ListingsApi->create_bigcommerce_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListingsApi->create_bigcommerce_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listings_create_bigcommerce_templates_request** | [**ListingsCreateBigcommerceTemplatesRequest**](ListingsCreateBigcommerceTemplatesRequest.md)|  | 

### Return type

[**PagedResultBigCommerceListing**](PagedResultBigCommerceListing.md)

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

# **create_ebay_templates**
> PagedResultEbayListing create_ebay_templates(listings_create_ebay_templates_request)

CreateEbayTemplates

Use this call to return a template based on the configurator setting you have requested. This allows you to see the template which can then be  retuned to the ProcessEbayListing endpoint which will build the listing. <b>Permissions Required: </b> GlobalPermissions.Settings.ListingConfigurators.GetListingConfiguratorsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.listings
from linnworks_api.generated.listings.models.listings_create_ebay_templates_request import ListingsCreateEbayTemplatesRequest
from linnworks_api.generated.listings.models.paged_result_ebay_listing import PagedResultEbayListing
from linnworks_api.generated.listings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.listings.Configuration(
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
with linnworks_api.generated.listings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.listings.ListingsApi(api_client)
    listings_create_ebay_templates_request = linnworks_api.generated.listings.ListingsCreateEbayTemplatesRequest() # ListingsCreateEbayTemplatesRequest | 

    try:
        # CreateEbayTemplates
        api_response = api_instance.create_ebay_templates(listings_create_ebay_templates_request)
        print("The response of ListingsApi->create_ebay_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListingsApi->create_ebay_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listings_create_ebay_templates_request** | [**ListingsCreateEbayTemplatesRequest**](ListingsCreateEbayTemplatesRequest.md)|  | 

### Return type

[**PagedResultEbayListing**](PagedResultEbayListing.md)

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

# **create_magento_configurators**
> create_magento_configurators(listings_create_magento_configurators_request)

CreateMagentoConfigurators

Use this call to create Magento configurators.                A configurator hosts common details for listings such as listing type, return policy, payment methods, shipping info, attributes, listing categories, etc. Configurators offer an efficient way of creating listings in bulk that follow a common theme. The same configurator can be used to list multiple items that share common details. To find out more about configurators you can visit our [documentation](https://docs.linnworks.com/articles/#!documentation/configurators) <b>Permissions Required: </b> GlobalPermissions.Settings.ListingConfigurators.EditListingConfiguratorsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.listings
from linnworks_api.generated.listings.models.listings_create_magento_configurators_request import ListingsCreateMagentoConfiguratorsRequest
from linnworks_api.generated.listings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.listings.Configuration(
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
with linnworks_api.generated.listings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.listings.ListingsApi(api_client)
    listings_create_magento_configurators_request = linnworks_api.generated.listings.ListingsCreateMagentoConfiguratorsRequest() # ListingsCreateMagentoConfiguratorsRequest | 

    try:
        # CreateMagentoConfigurators
        api_instance.create_magento_configurators(listings_create_magento_configurators_request)
    except Exception as e:
        print("Exception when calling ListingsApi->create_magento_configurators: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listings_create_magento_configurators_request** | [**ListingsCreateMagentoConfiguratorsRequest**](ListingsCreateMagentoConfiguratorsRequest.md)|  | 

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

# **create_magento_templates**
> PagedResultMagentoListing create_magento_templates(listings_create_magento_templates_request)

CreateMagentoTemplates

Use this call to return a template based on the configurator setting you have requested. This allows you to see the template which can then be  retuned to the ProcessMagentoListing endpoint which will build the listing. <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.listings
from linnworks_api.generated.listings.models.listings_create_magento_templates_request import ListingsCreateMagentoTemplatesRequest
from linnworks_api.generated.listings.models.paged_result_magento_listing import PagedResultMagentoListing
from linnworks_api.generated.listings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.listings.Configuration(
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
with linnworks_api.generated.listings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.listings.ListingsApi(api_client)
    listings_create_magento_templates_request = linnworks_api.generated.listings.ListingsCreateMagentoTemplatesRequest() # ListingsCreateMagentoTemplatesRequest | 

    try:
        # CreateMagentoTemplates
        api_response = api_instance.create_magento_templates(listings_create_magento_templates_request)
        print("The response of ListingsApi->create_magento_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListingsApi->create_magento_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listings_create_magento_templates_request** | [**ListingsCreateMagentoTemplatesRequest**](ListingsCreateMagentoTemplatesRequest.md)|  | 

### Return type

[**PagedResultMagentoListing**](PagedResultMagentoListing.md)

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

# **create_templates_from_view_in_bulk**
> object create_templates_from_view_in_bulk(listings_create_templates_from_view_in_bulk_request)

CreateTemplatesFromViewInBulk

Use this call to create wireup to create templates in bulk <b>Permissions Required: </b> GlobalPermissions.Settings.ListingConfigurators.GetListingConfiguratorsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.listings
from linnworks_api.generated.listings.models.listings_create_templates_from_view_in_bulk_request import ListingsCreateTemplatesFromViewInBulkRequest
from linnworks_api.generated.listings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.listings.Configuration(
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
with linnworks_api.generated.listings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.listings.ListingsApi(api_client)
    listings_create_templates_from_view_in_bulk_request = linnworks_api.generated.listings.ListingsCreateTemplatesFromViewInBulkRequest() # ListingsCreateTemplatesFromViewInBulkRequest | 

    try:
        # CreateTemplatesFromViewInBulk
        api_response = api_instance.create_templates_from_view_in_bulk(listings_create_templates_from_view_in_bulk_request)
        print("The response of ListingsApi->create_templates_from_view_in_bulk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListingsApi->create_templates_from_view_in_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listings_create_templates_from_view_in_bulk_request** | [**ListingsCreateTemplatesFromViewInBulkRequest**](ListingsCreateTemplatesFromViewInBulkRequest.md)|  | 

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

# **createe_bay_configurators**
> createe_bay_configurators(listings_createe_bay_configurators_request)

CreateeBayConfigurators

Use this call to create eBay configurators.                A configurator hosts common details for listings such as listing type, return policy, payment methods, shipping info, attributes, listing categories, etc. Configurators offer an efficient way of creating listings in bulk that follow a common theme.The same configurator can be used to list multiple items that share common details.To find out more about configurators you can visit our [documentation](https://docs.linnworks.com/articles/#!documentation/configurators) <b>Permissions Required: </b> GlobalPermissions.Settings.ListingConfigurators.EditListingConfiguratorsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.listings
from linnworks_api.generated.listings.models.listings_createe_bay_configurators_request import ListingsCreateeBayConfiguratorsRequest
from linnworks_api.generated.listings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.listings.Configuration(
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
with linnworks_api.generated.listings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.listings.ListingsApi(api_client)
    listings_createe_bay_configurators_request = linnworks_api.generated.listings.ListingsCreateeBayConfiguratorsRequest() # ListingsCreateeBayConfiguratorsRequest | 

    try:
        # CreateeBayConfigurators
        api_instance.createe_bay_configurators(listings_createe_bay_configurators_request)
    except Exception as e:
        print("Exception when calling ListingsApi->createe_bay_configurators: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listings_createe_bay_configurators_request** | [**ListingsCreateeBayConfiguratorsRequest**](ListingsCreateeBayConfiguratorsRequest.md)|  | 

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

# **delete_amazon_configurators**
> delete_amazon_configurators(listings_delete_amazon_configurators_request)

DeleteAmazonConfigurators

Use this call to delete Amazon configurators.                A configurator hosts common details for listings such as listing type, return policy, payment methods, shipping info, attributes, listing categories, etc. Configurators offer an efficient way of creating listings in bulk that follow a common theme. The same configurator can be used to list multiple items that share common details. To find out more about configurators you can visit our [documentation](https://docs.linnworks.com/articles/#!documentation/configurators) <b>Permissions Required: </b> GlobalPermissions.Settings.ListingConfigurators.EditListingConfiguratorsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.listings
from linnworks_api.generated.listings.models.listings_delete_amazon_configurators_request import ListingsDeleteAmazonConfiguratorsRequest
from linnworks_api.generated.listings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.listings.Configuration(
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
with linnworks_api.generated.listings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.listings.ListingsApi(api_client)
    listings_delete_amazon_configurators_request = linnworks_api.generated.listings.ListingsDeleteAmazonConfiguratorsRequest() # ListingsDeleteAmazonConfiguratorsRequest | 

    try:
        # DeleteAmazonConfigurators
        api_instance.delete_amazon_configurators(listings_delete_amazon_configurators_request)
    except Exception as e:
        print("Exception when calling ListingsApi->delete_amazon_configurators: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listings_delete_amazon_configurators_request** | [**ListingsDeleteAmazonConfiguratorsRequest**](ListingsDeleteAmazonConfiguratorsRequest.md)|  | 

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

# **delete_amazon_templates**
> delete_amazon_templates(listings_delete_amazon_templates_request)

DeleteAmazonTemplates

Use this call to delete a Amazon template. <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.listings
from linnworks_api.generated.listings.models.listings_delete_amazon_templates_request import ListingsDeleteAmazonTemplatesRequest
from linnworks_api.generated.listings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.listings.Configuration(
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
with linnworks_api.generated.listings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.listings.ListingsApi(api_client)
    listings_delete_amazon_templates_request = linnworks_api.generated.listings.ListingsDeleteAmazonTemplatesRequest() # ListingsDeleteAmazonTemplatesRequest | 

    try:
        # DeleteAmazonTemplates
        api_instance.delete_amazon_templates(listings_delete_amazon_templates_request)
    except Exception as e:
        print("Exception when calling ListingsApi->delete_amazon_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listings_delete_amazon_templates_request** | [**ListingsDeleteAmazonTemplatesRequest**](ListingsDeleteAmazonTemplatesRequest.md)|  | 

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

# **delete_bigcommerce_configurators**
> delete_bigcommerce_configurators(listings_delete_bigcommerce_configurators_request)

DeleteBigcommerceConfigurators

Use this call to delete BigCommerce configurators.                A configurator hosts common details for listings such as listing type, return policy, payment methods, shipping info, attributes, listing categories, etc. Configurators offer an efficient way of creating listings in bulk that follow a common theme. The same configurator can be used to list multiple items that share common details. To find out more about configurators you can visit our [documentation](https://docs.linnworks.com/articles/#!documentation/configurators) <b>Permissions Required: </b> GlobalPermissions.Settings.ListingConfigurators.EditListingConfiguratorsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.listings
from linnworks_api.generated.listings.models.listings_delete_bigcommerce_configurators_request import ListingsDeleteBigcommerceConfiguratorsRequest
from linnworks_api.generated.listings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.listings.Configuration(
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
with linnworks_api.generated.listings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.listings.ListingsApi(api_client)
    listings_delete_bigcommerce_configurators_request = linnworks_api.generated.listings.ListingsDeleteBigcommerceConfiguratorsRequest() # ListingsDeleteBigcommerceConfiguratorsRequest | 

    try:
        # DeleteBigcommerceConfigurators
        api_instance.delete_bigcommerce_configurators(listings_delete_bigcommerce_configurators_request)
    except Exception as e:
        print("Exception when calling ListingsApi->delete_bigcommerce_configurators: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listings_delete_bigcommerce_configurators_request** | [**ListingsDeleteBigcommerceConfiguratorsRequest**](ListingsDeleteBigcommerceConfiguratorsRequest.md)|  | 

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

# **delete_bigcommerce_templates**
> delete_bigcommerce_templates(listings_delete_bigcommerce_templates_request)

DeleteBigcommerceTemplates

Use this call to delete a Big Commerce template. <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.listings
from linnworks_api.generated.listings.models.listings_delete_bigcommerce_templates_request import ListingsDeleteBigcommerceTemplatesRequest
from linnworks_api.generated.listings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.listings.Configuration(
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
with linnworks_api.generated.listings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.listings.ListingsApi(api_client)
    listings_delete_bigcommerce_templates_request = linnworks_api.generated.listings.ListingsDeleteBigcommerceTemplatesRequest() # ListingsDeleteBigcommerceTemplatesRequest | 

    try:
        # DeleteBigcommerceTemplates
        api_instance.delete_bigcommerce_templates(listings_delete_bigcommerce_templates_request)
    except Exception as e:
        print("Exception when calling ListingsApi->delete_bigcommerce_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listings_delete_bigcommerce_templates_request** | [**ListingsDeleteBigcommerceTemplatesRequest**](ListingsDeleteBigcommerceTemplatesRequest.md)|  | 

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

# **delete_ebay_templates**
> delete_ebay_templates(listings_delete_ebay_templates_request)

DeleteEbayTemplates

Use this call to delete a Ebay template. <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.listings
from linnworks_api.generated.listings.models.listings_delete_ebay_templates_request import ListingsDeleteEbayTemplatesRequest
from linnworks_api.generated.listings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.listings.Configuration(
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
with linnworks_api.generated.listings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.listings.ListingsApi(api_client)
    listings_delete_ebay_templates_request = linnworks_api.generated.listings.ListingsDeleteEbayTemplatesRequest() # ListingsDeleteEbayTemplatesRequest | 

    try:
        # DeleteEbayTemplates
        api_instance.delete_ebay_templates(listings_delete_ebay_templates_request)
    except Exception as e:
        print("Exception when calling ListingsApi->delete_ebay_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listings_delete_ebay_templates_request** | [**ListingsDeleteEbayTemplatesRequest**](ListingsDeleteEbayTemplatesRequest.md)|  | 

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

# **delete_magento_configurators**
> delete_magento_configurators(listings_delete_magento_configurators_request)

DeleteMagentoConfigurators

Use this call to delete Magento configurators.                A configurator hosts common details for listings such as listing type, return policy, payment methods, shipping info, attributes, listing categories, etc. Configurators offer an efficient way of creating listings in bulk that follow a common theme. The same configurator can be used to list multiple items that share common details. To find out more about configurators you can visit our [documentation](https://docs.linnworks.com/articles/#!documentation/configurators) <b>Permissions Required: </b> GlobalPermissions.Settings.ListingConfigurators.EditListingConfiguratorsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.listings
from linnworks_api.generated.listings.models.listings_delete_magento_configurators_request import ListingsDeleteMagentoConfiguratorsRequest
from linnworks_api.generated.listings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.listings.Configuration(
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
with linnworks_api.generated.listings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.listings.ListingsApi(api_client)
    listings_delete_magento_configurators_request = linnworks_api.generated.listings.ListingsDeleteMagentoConfiguratorsRequest() # ListingsDeleteMagentoConfiguratorsRequest | 

    try:
        # DeleteMagentoConfigurators
        api_instance.delete_magento_configurators(listings_delete_magento_configurators_request)
    except Exception as e:
        print("Exception when calling ListingsApi->delete_magento_configurators: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listings_delete_magento_configurators_request** | [**ListingsDeleteMagentoConfiguratorsRequest**](ListingsDeleteMagentoConfiguratorsRequest.md)|  | 

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

# **delete_magento_templates**
> delete_magento_templates(listings_delete_magento_templates_request)

DeleteMagentoTemplates

Use this call to delete a Magento template. <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.listings
from linnworks_api.generated.listings.models.listings_delete_magento_templates_request import ListingsDeleteMagentoTemplatesRequest
from linnworks_api.generated.listings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.listings.Configuration(
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
with linnworks_api.generated.listings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.listings.ListingsApi(api_client)
    listings_delete_magento_templates_request = linnworks_api.generated.listings.ListingsDeleteMagentoTemplatesRequest() # ListingsDeleteMagentoTemplatesRequest | 

    try:
        # DeleteMagentoTemplates
        api_instance.delete_magento_templates(listings_delete_magento_templates_request)
    except Exception as e:
        print("Exception when calling ListingsApi->delete_magento_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listings_delete_magento_templates_request** | [**ListingsDeleteMagentoTemplatesRequest**](ListingsDeleteMagentoTemplatesRequest.md)|  | 

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

# **deletee_bay_configurators**
> deletee_bay_configurators(listings_deletee_bay_configurators_request)

DeleteeBayConfigurators

Use this call to delete eBay configurators.                A configurator hosts common details for listings such as listing type, return policy, payment methods, shipping info, attributes, listing categories, etc. Configurators offer an efficient way of creating listings in bulk that follow a common theme. The same configurator can be used to list multiple items that share common details. To find out more about configurators you can visit our [documentation](https://docs.linnworks.com/articles/#!documentation/configurators) <b>Permissions Required: </b> GlobalPermissions.Settings.ListingConfigurators.EditListingConfiguratorsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.listings
from linnworks_api.generated.listings.models.listings_deletee_bay_configurators_request import ListingsDeleteeBayConfiguratorsRequest
from linnworks_api.generated.listings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.listings.Configuration(
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
with linnworks_api.generated.listings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.listings.ListingsApi(api_client)
    listings_deletee_bay_configurators_request = linnworks_api.generated.listings.ListingsDeleteeBayConfiguratorsRequest() # ListingsDeleteeBayConfiguratorsRequest | 

    try:
        # DeleteeBayConfigurators
        api_instance.deletee_bay_configurators(listings_deletee_bay_configurators_request)
    except Exception as e:
        print("Exception when calling ListingsApi->deletee_bay_configurators: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listings_deletee_bay_configurators_request** | [**ListingsDeleteeBayConfiguratorsRequest**](ListingsDeleteeBayConfiguratorsRequest.md)|  | 

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

# **end_listings_pending_relist**
> end_listings_pending_relist(listings_end_listings_pending_relist_request)

EndListingsPendingRelist

End eBay listings pending relist <b>Permissions Required: </b> GlobalPermissions.Settings.ListingConfiguratorsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.listings
from linnworks_api.generated.listings.models.listings_end_listings_pending_relist_request import ListingsEndListingsPendingRelistRequest
from linnworks_api.generated.listings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.listings.Configuration(
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
with linnworks_api.generated.listings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.listings.ListingsApi(api_client)
    listings_end_listings_pending_relist_request = linnworks_api.generated.listings.ListingsEndListingsPendingRelistRequest() # ListingsEndListingsPendingRelistRequest | 

    try:
        # EndListingsPendingRelist
        api_instance.end_listings_pending_relist(listings_end_listings_pending_relist_request)
    except Exception as e:
        print("Exception when calling ListingsApi->end_listings_pending_relist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listings_end_listings_pending_relist_request** | [**ListingsEndListingsPendingRelistRequest**](ListingsEndListingsPendingRelistRequest.md)|  | 

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

# **get_amazon_configurators**
> List[AmazonConfig] get_amazon_configurators()

GetAmazonConfigurators

Use this call to get Amazon configurators.                A configurator hosts common details for listings such as listing type, return policy, payment methods, shipping info, attributes, listing categories, etc. Configurators offer an efficient way of creating listings in bulk that follow a common theme. The same configurator can be used to list multiple items that share common details. To find out more about configurators you can visit our [documentation](https://docs.linnworks.com/articles/#!documentation/configurators) <b>Permissions Required: </b> GlobalPermissions.Settings.ListingConfigurators.GetListingConfiguratorsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.listings
from linnworks_api.generated.listings.models.amazon_config import AmazonConfig
from linnworks_api.generated.listings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.listings.Configuration(
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
with linnworks_api.generated.listings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.listings.ListingsApi(api_client)

    try:
        # GetAmazonConfigurators
        api_response = api_instance.get_amazon_configurators()
        print("The response of ListingsApi->get_amazon_configurators:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListingsApi->get_amazon_configurators: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[AmazonConfig]**](AmazonConfig.md)

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

# **get_amazon_templates**
> PagedResultAmazonListing get_amazon_templates(listings_get_amazon_templates_request)

GetAmazonTemplates

Use this call to return all created Amazon templates. <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>250</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.listings
from linnworks_api.generated.listings.models.listings_get_amazon_templates_request import ListingsGetAmazonTemplatesRequest
from linnworks_api.generated.listings.models.paged_result_amazon_listing import PagedResultAmazonListing
from linnworks_api.generated.listings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.listings.Configuration(
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
with linnworks_api.generated.listings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.listings.ListingsApi(api_client)
    listings_get_amazon_templates_request = linnworks_api.generated.listings.ListingsGetAmazonTemplatesRequest() # ListingsGetAmazonTemplatesRequest | 

    try:
        # GetAmazonTemplates
        api_response = api_instance.get_amazon_templates(listings_get_amazon_templates_request)
        print("The response of ListingsApi->get_amazon_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListingsApi->get_amazon_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listings_get_amazon_templates_request** | [**ListingsGetAmazonTemplatesRequest**](ListingsGetAmazonTemplatesRequest.md)|  | 

### Return type

[**PagedResultAmazonListing**](PagedResultAmazonListing.md)

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

# **get_big_commerce_templates**
> PagedResultBigCommerceListing get_big_commerce_templates(listings_get_big_commerce_templates_request)

GetBigCommerceTemplates

Use this call to return all created Big Commerce templates. <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.listings
from linnworks_api.generated.listings.models.listings_get_big_commerce_templates_request import ListingsGetBigCommerceTemplatesRequest
from linnworks_api.generated.listings.models.paged_result_big_commerce_listing import PagedResultBigCommerceListing
from linnworks_api.generated.listings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.listings.Configuration(
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
with linnworks_api.generated.listings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.listings.ListingsApi(api_client)
    listings_get_big_commerce_templates_request = linnworks_api.generated.listings.ListingsGetBigCommerceTemplatesRequest() # ListingsGetBigCommerceTemplatesRequest | 

    try:
        # GetBigCommerceTemplates
        api_response = api_instance.get_big_commerce_templates(listings_get_big_commerce_templates_request)
        print("The response of ListingsApi->get_big_commerce_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListingsApi->get_big_commerce_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listings_get_big_commerce_templates_request** | [**ListingsGetBigCommerceTemplatesRequest**](ListingsGetBigCommerceTemplatesRequest.md)|  | 

### Return type

[**PagedResultBigCommerceListing**](PagedResultBigCommerceListing.md)

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

# **get_bigcommerce_configurators**
> List[BigCommerceConfigurator] get_bigcommerce_configurators()

GetBigcommerceConfigurators

Use this call to get all Bigcommerce configurators.                A configurator hosts common details for listings such as listing type, return policy, payment methods, shipping info, attributes, listing categories, etc. Configurators offer an efficient way of creating listings in bulk that follow a common theme. The same configurator can be used to list multiple items that share common details. To find out more about configurators you can visit our [documentation](https://docs.linnworks.com/articles/#!documentation/configurators) <b>Permissions Required: </b> GlobalPermissions.Settings.ListingConfigurators.GetListingConfiguratorsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.listings
from linnworks_api.generated.listings.models.big_commerce_configurator import BigCommerceConfigurator
from linnworks_api.generated.listings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.listings.Configuration(
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
with linnworks_api.generated.listings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.listings.ListingsApi(api_client)

    try:
        # GetBigcommerceConfigurators
        api_response = api_instance.get_bigcommerce_configurators()
        print("The response of ListingsApi->get_bigcommerce_configurators:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListingsApi->get_bigcommerce_configurators: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[BigCommerceConfigurator]**](BigCommerceConfigurator.md)

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

# **get_ebay_listing_operations**
> object get_ebay_listing_operations(request_location_id=request_location_id, request_page_number=request_page_number, request_entries_per_page=request_entries_per_page, request_channel_ids=request_channel_ids)

GetEbayListingOperations

Use this call to get ebay listing bulk creation operations <b>Permissions Required: </b> GlobalPermissions.Settings.ListingConfigurators.GetListingConfiguratorsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.listings
from linnworks_api.generated.listings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.listings.Configuration(
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
with linnworks_api.generated.listings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.listings.ListingsApi(api_client)
    request_location_id = 'request_location_id_example' # str |  (optional)
    request_page_number = 56 # int |  (optional)
    request_entries_per_page = 56 # int |  (optional)
    request_channel_ids = [56] # List[int] |  (optional)

    try:
        # GetEbayListingOperations
        api_response = api_instance.get_ebay_listing_operations(request_location_id=request_location_id, request_page_number=request_page_number, request_entries_per_page=request_entries_per_page, request_channel_ids=request_channel_ids)
        print("The response of ListingsApi->get_ebay_listing_operations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListingsApi->get_ebay_listing_operations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_location_id** | **str**|  | [optional] 
 **request_page_number** | **int**|  | [optional] 
 **request_entries_per_page** | **int**|  | [optional] 
 **request_channel_ids** | [**List[int]**](int.md)|  | [optional] 

### Return type

**object**

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

# **get_magento_configurators**
> List[MagentoConfig] get_magento_configurators()

GetMagentoConfigurators

Use this call to get all Magento configurators.                A configurator hosts common details for listings such as listing type, return policy, payment methods, shipping info, attributes, listing categories, etc. Configurators offer an efficient way of creating listings in bulk that follow a common theme. The same configurator can be used to list multiple items that share common details. To find out more about configurators you can visit our [documentation](https://docs.linnworks.com/articles/#!documentation/configurators) <b>Permissions Required: </b> GlobalPermissions.Settings.ListingConfigurators.GetListingConfiguratorsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.listings
from linnworks_api.generated.listings.models.magento_config import MagentoConfig
from linnworks_api.generated.listings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.listings.Configuration(
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
with linnworks_api.generated.listings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.listings.ListingsApi(api_client)

    try:
        # GetMagentoConfigurators
        api_response = api_instance.get_magento_configurators()
        print("The response of ListingsApi->get_magento_configurators:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListingsApi->get_magento_configurators: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[MagentoConfig]**](MagentoConfig.md)

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

# **get_magento_templates**
> PagedResultMagentoListing get_magento_templates(listings_get_magento_templates_request)

GetMagentoTemplates

Use this call to return all created Magento templates. <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.listings
from linnworks_api.generated.listings.models.listings_get_magento_templates_request import ListingsGetMagentoTemplatesRequest
from linnworks_api.generated.listings.models.paged_result_magento_listing import PagedResultMagentoListing
from linnworks_api.generated.listings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.listings.Configuration(
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
with linnworks_api.generated.listings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.listings.ListingsApi(api_client)
    listings_get_magento_templates_request = linnworks_api.generated.listings.ListingsGetMagentoTemplatesRequest() # ListingsGetMagentoTemplatesRequest | 

    try:
        # GetMagentoTemplates
        api_response = api_instance.get_magento_templates(listings_get_magento_templates_request)
        print("The response of ListingsApi->get_magento_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListingsApi->get_magento_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listings_get_magento_templates_request** | [**ListingsGetMagentoTemplatesRequest**](ListingsGetMagentoTemplatesRequest.md)|  | 

### Return type

[**PagedResultMagentoListing**](PagedResultMagentoListing.md)

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

# **gete_bay_configurators**
> List[EbayConfig] gete_bay_configurators()

GeteBayConfigurators

Use this call to get eBay configurators.                A configurator hosts common details for listings such as listing type, return policy, payment methods, shipping info, attributes, listing categories, etc. Configurators offer an efficient way of creating listings in bulk that follow a common theme.The same configurator can be used to list multiple items that share common details.To find out more about configurators you can visit our [documentation](https://docs.linnworks.com/articles/#!documentation/configurators) <b>Permissions Required: </b> GlobalPermissions.Settings.ListingConfigurators.GetListingConfiguratorsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.listings
from linnworks_api.generated.listings.models.ebay_config import EbayConfig
from linnworks_api.generated.listings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.listings.Configuration(
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
with linnworks_api.generated.listings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.listings.ListingsApi(api_client)

    try:
        # GeteBayConfigurators
        api_response = api_instance.gete_bay_configurators()
        print("The response of ListingsApi->gete_bay_configurators:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListingsApi->gete_bay_configurators: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[EbayConfig]**](EbayConfig.md)

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

# **gete_bay_templates**
> PagedResultEbayListing gete_bay_templates(listings_gete_bay_templates_request)

GeteBayTemplates

Use this call to return all created Ebay templates. <b>Permissions Required: </b> GlobalPermissions.Settings.ListingConfigurators.GetListingConfiguratorsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.listings
from linnworks_api.generated.listings.models.listings_gete_bay_templates_request import ListingsGeteBayTemplatesRequest
from linnworks_api.generated.listings.models.paged_result_ebay_listing import PagedResultEbayListing
from linnworks_api.generated.listings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.listings.Configuration(
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
with linnworks_api.generated.listings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.listings.ListingsApi(api_client)
    listings_gete_bay_templates_request = linnworks_api.generated.listings.ListingsGeteBayTemplatesRequest() # ListingsGeteBayTemplatesRequest | 

    try:
        # GeteBayTemplates
        api_response = api_instance.gete_bay_templates(listings_gete_bay_templates_request)
        print("The response of ListingsApi->gete_bay_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListingsApi->gete_bay_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listings_gete_bay_templates_request** | [**ListingsGeteBayTemplatesRequest**](ListingsGeteBayTemplatesRequest.md)|  | 

### Return type

[**PagedResultEbayListing**](PagedResultEbayListing.md)

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

# **process_amazon_listings**
> process_amazon_listings(listings_process_amazon_listings_request)

ProcessAmazonListings

Use this call to create templates in Linnworks and can also be used to push the template to a channel. This will create the template even if it returns null. This will also push the template to the channel depending on what the status is set as.  Amazon Listing Statuses:  NOT_LISTED,  OK,  CREATING(push to channel),  UPDATING,  UPDATING_PRICE,  UPDATING_QUANTITY,  UPDATING_IMAGES,  CREATING_VARIATION,  DELETING,  SEARCHING_FOR_MATCHES,  UPDATING_SHIPPING <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.listings
from linnworks_api.generated.listings.models.listings_process_amazon_listings_request import ListingsProcessAmazonListingsRequest
from linnworks_api.generated.listings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.listings.Configuration(
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
with linnworks_api.generated.listings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.listings.ListingsApi(api_client)
    listings_process_amazon_listings_request = linnworks_api.generated.listings.ListingsProcessAmazonListingsRequest() # ListingsProcessAmazonListingsRequest | 

    try:
        # ProcessAmazonListings
        api_instance.process_amazon_listings(listings_process_amazon_listings_request)
    except Exception as e:
        print("Exception when calling ListingsApi->process_amazon_listings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listings_process_amazon_listings_request** | [**ListingsProcessAmazonListingsRequest**](ListingsProcessAmazonListingsRequest.md)|  | 

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

# **process_bigcommerce_listings**
> process_bigcommerce_listings(listings_process_bigcommerce_listings_request)

ProcessBigcommerceListings

Use this call to create templates in Linnworks and can also be used to push the template to a channel. This will create the template even if it returns null. This will also push the template to the channel depending on what the status is set as. <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.listings
from linnworks_api.generated.listings.models.listings_process_bigcommerce_listings_request import ListingsProcessBigcommerceListingsRequest
from linnworks_api.generated.listings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.listings.Configuration(
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
with linnworks_api.generated.listings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.listings.ListingsApi(api_client)
    listings_process_bigcommerce_listings_request = linnworks_api.generated.listings.ListingsProcessBigcommerceListingsRequest() # ListingsProcessBigcommerceListingsRequest | 

    try:
        # ProcessBigcommerceListings
        api_instance.process_bigcommerce_listings(listings_process_bigcommerce_listings_request)
    except Exception as e:
        print("Exception when calling ListingsApi->process_bigcommerce_listings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listings_process_bigcommerce_listings_request** | [**ListingsProcessBigcommerceListingsRequest**](ListingsProcessBigcommerceListingsRequest.md)|  | 

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

# **process_magento_listings**
> process_magento_listings(listings_process_magento_listings_request)

ProcessMagentoListings

Use this call to create templates in Linnworks and can also be used to push the template to a channel. This will create the template even if it returns null. This will also push the template to the channel depending on what the status is set as. <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.listings
from linnworks_api.generated.listings.models.listings_process_magento_listings_request import ListingsProcessMagentoListingsRequest
from linnworks_api.generated.listings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.listings.Configuration(
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
with linnworks_api.generated.listings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.listings.ListingsApi(api_client)
    listings_process_magento_listings_request = linnworks_api.generated.listings.ListingsProcessMagentoListingsRequest() # ListingsProcessMagentoListingsRequest | 

    try:
        # ProcessMagentoListings
        api_instance.process_magento_listings(listings_process_magento_listings_request)
    except Exception as e:
        print("Exception when calling ListingsApi->process_magento_listings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listings_process_magento_listings_request** | [**ListingsProcessMagentoListingsRequest**](ListingsProcessMagentoListingsRequest.md)|  | 

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

# **processe_bay_listings**
> processe_bay_listings(listings_processe_bay_listings_request)

ProcesseBayListings

Use this call to create templates in Linnworks and can also be used to push the template to a channel. This will create the template even if it returns null. This will also push the template to the channel depending on what the status is set as. <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.listings
from linnworks_api.generated.listings.models.listings_processe_bay_listings_request import ListingsProcesseBayListingsRequest
from linnworks_api.generated.listings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.listings.Configuration(
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
with linnworks_api.generated.listings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.listings.ListingsApi(api_client)
    listings_processe_bay_listings_request = linnworks_api.generated.listings.ListingsProcesseBayListingsRequest() # ListingsProcesseBayListingsRequest | 

    try:
        # ProcesseBayListings
        api_instance.processe_bay_listings(listings_processe_bay_listings_request)
    except Exception as e:
        print("Exception when calling ListingsApi->processe_bay_listings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listings_processe_bay_listings_request** | [**ListingsProcesseBayListingsRequest**](ListingsProcesseBayListingsRequest.md)|  | 

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

# **set_listing_strike_off_state**
> set_listing_strike_off_state(listings_set_listing_strike_off_state_request)

SetListingStrikeOffState

Set eBay Listing Strike State <b>Permissions Required: </b> GlobalPermissions.Settings.ListingConfiguratorsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.listings
from linnworks_api.generated.listings.models.listings_set_listing_strike_off_state_request import ListingsSetListingStrikeOffStateRequest
from linnworks_api.generated.listings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.listings.Configuration(
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
with linnworks_api.generated.listings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.listings.ListingsApi(api_client)
    listings_set_listing_strike_off_state_request = linnworks_api.generated.listings.ListingsSetListingStrikeOffStateRequest() # ListingsSetListingStrikeOffStateRequest | 

    try:
        # SetListingStrikeOffState
        api_instance.set_listing_strike_off_state(listings_set_listing_strike_off_state_request)
    except Exception as e:
        print("Exception when calling ListingsApi->set_listing_strike_off_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listings_set_listing_strike_off_state_request** | [**ListingsSetListingStrikeOffStateRequest**](ListingsSetListingStrikeOffStateRequest.md)|  | 

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

# **update_amazon_configurators**
> update_amazon_configurators(listings_update_amazon_configurators_request)

UpdateAmazonConfigurators

Use this call to update Amazon configurators.                A configurator hosts common details for listings such as listing type, return policy, payment methods, shipping info, attributes, listing categories, etc. Configurators offer an efficient way of creating listings in bulk that follow a common theme. The same configurator can be used to list multiple items that share common details. To find out more about configurators you can visit our [documentation](https://docs.linnworks.com/articles/#!documentation/configurators) <b>Permissions Required: </b> GlobalPermissions.Settings.ListingConfigurators.EditListingConfiguratorsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.listings
from linnworks_api.generated.listings.models.listings_update_amazon_configurators_request import ListingsUpdateAmazonConfiguratorsRequest
from linnworks_api.generated.listings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.listings.Configuration(
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
with linnworks_api.generated.listings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.listings.ListingsApi(api_client)
    listings_update_amazon_configurators_request = linnworks_api.generated.listings.ListingsUpdateAmazonConfiguratorsRequest() # ListingsUpdateAmazonConfiguratorsRequest | 

    try:
        # UpdateAmazonConfigurators
        api_instance.update_amazon_configurators(listings_update_amazon_configurators_request)
    except Exception as e:
        print("Exception when calling ListingsApi->update_amazon_configurators: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listings_update_amazon_configurators_request** | [**ListingsUpdateAmazonConfiguratorsRequest**](ListingsUpdateAmazonConfiguratorsRequest.md)|  | 

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

# **update_bigcommerce_configurators**
> update_bigcommerce_configurators(listings_update_bigcommerce_configurators_request)

UpdateBigcommerceConfigurators

Use this call to update BigCommerce configurators.                A configurator hosts common details for listings such as listing type, return policy, payment methods, shipping info, attributes, listing categories, etc. Configurators offer an efficient way of creating listings in bulk that follow a common theme. The same configurator can be used to list multiple items that share common details. To find out more about configurators you can visit our [documentation](https://docs.linnworks.com/articles/#!documentation/configurators) <b>Permissions Required: </b> GlobalPermissions.Settings.ListingConfigurators.EditListingConfiguratorsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.listings
from linnworks_api.generated.listings.models.listings_update_bigcommerce_configurators_request import ListingsUpdateBigcommerceConfiguratorsRequest
from linnworks_api.generated.listings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.listings.Configuration(
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
with linnworks_api.generated.listings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.listings.ListingsApi(api_client)
    listings_update_bigcommerce_configurators_request = linnworks_api.generated.listings.ListingsUpdateBigcommerceConfiguratorsRequest() # ListingsUpdateBigcommerceConfiguratorsRequest | 

    try:
        # UpdateBigcommerceConfigurators
        api_instance.update_bigcommerce_configurators(listings_update_bigcommerce_configurators_request)
    except Exception as e:
        print("Exception when calling ListingsApi->update_bigcommerce_configurators: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listings_update_bigcommerce_configurators_request** | [**ListingsUpdateBigcommerceConfiguratorsRequest**](ListingsUpdateBigcommerceConfiguratorsRequest.md)|  | 

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

# **update_magento_configurators**
> update_magento_configurators(listings_update_magento_configurators_request)

UpdateMagentoConfigurators

Use this call to update Magento configurators.                A configurator hosts common details for listings such as listing type, return policy, payment methods, shipping info, attributes, listing categories, etc. Configurators offer an efficient way of creating listings in bulk that follow a common theme. The same configurator can be used to list multiple items that share common details. To find out more about configurators you can visit our [documentation](https://docs.linnworks.com/articles/#!documentation/configurators) <b>Permissions Required: </b> GlobalPermissions.Settings.ListingConfigurators.EditListingConfiguratorsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.listings
from linnworks_api.generated.listings.models.listings_update_magento_configurators_request import ListingsUpdateMagentoConfiguratorsRequest
from linnworks_api.generated.listings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.listings.Configuration(
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
with linnworks_api.generated.listings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.listings.ListingsApi(api_client)
    listings_update_magento_configurators_request = linnworks_api.generated.listings.ListingsUpdateMagentoConfiguratorsRequest() # ListingsUpdateMagentoConfiguratorsRequest | 

    try:
        # UpdateMagentoConfigurators
        api_instance.update_magento_configurators(listings_update_magento_configurators_request)
    except Exception as e:
        print("Exception when calling ListingsApi->update_magento_configurators: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listings_update_magento_configurators_request** | [**ListingsUpdateMagentoConfiguratorsRequest**](ListingsUpdateMagentoConfiguratorsRequest.md)|  | 

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

# **updatee_bay_configurators**
> updatee_bay_configurators(listings_updatee_bay_configurators_request)

UpdateeBayConfigurators

Use this call to update eBay configurators.                A configurator hosts common details for listings such as listing type, return policy, payment methods, shipping info, attributes, listing categories, etc. Configurators offer an efficient way of creating listings in bulk that follow a common theme. The same configurator can be used to list multiple items that share common details. To find out more about configurators you can visit our [documentation](https://docs.linnworks.com/articles/#!documentation/configurators) <b>Permissions Required: </b> GlobalPermissions.Settings.ListingConfigurators.EditListingConfiguratorsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.listings
from linnworks_api.generated.listings.models.listings_updatee_bay_configurators_request import ListingsUpdateeBayConfiguratorsRequest
from linnworks_api.generated.listings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.listings.Configuration(
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
with linnworks_api.generated.listings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.listings.ListingsApi(api_client)
    listings_updatee_bay_configurators_request = linnworks_api.generated.listings.ListingsUpdateeBayConfiguratorsRequest() # ListingsUpdateeBayConfiguratorsRequest | 

    try:
        # UpdateeBayConfigurators
        api_instance.updatee_bay_configurators(listings_updatee_bay_configurators_request)
    except Exception as e:
        print("Exception when calling ListingsApi->updatee_bay_configurators: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listings_updatee_bay_configurators_request** | [**ListingsUpdateeBayConfiguratorsRequest**](ListingsUpdateeBayConfiguratorsRequest.md)|  | 

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

