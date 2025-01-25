# PostalServiceWithChannelAndShippingLinks

Class which exposes only those elements required by linnworks.net front end

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Postal service ID | [optional] [readonly] 
**has_mapped_shipping_service** | **bool** | If there is channel linking with shipping service | [optional] 
**channels** | [**List[Channel]**](Channel.md) | Channel information | [optional] 
**shipping_services** | [**List[ShippingService]**](ShippingService.md) | Shipping service information | [optional] 
**postal_service_name** | **str** |  | [optional] 
**postal_service_tag** | **str** |  | [optional] 
**service_country** | **str** |  | [optional] 
**postal_service_code** | **str** |  | [optional] 
**vendor** | **str** |  | [optional] 
**print_module** | **str** |  | [optional] 
**print_module_title** | **str** |  | [optional] 
**pk_postal_service_id** | **str** |  | [optional] 
**tracking_number_required** | **bool** |  | [optional] 
**weight_required** | **bool** |  | [optional] 
**ignore_packaging_group** | **bool** |  | [optional] 
**fk_shipping_api_config_id** | **int** |  | [optional] 
**integrated_service_id** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.postalservices.models.postal_service_with_channel_and_shipping_links import PostalServiceWithChannelAndShippingLinks

# TODO update the JSON string below
json = "{}"
# create an instance of PostalServiceWithChannelAndShippingLinks from a JSON string
postal_service_with_channel_and_shipping_links_instance = PostalServiceWithChannelAndShippingLinks.from_json(json)
# print the JSON string representation of the object
print(PostalServiceWithChannelAndShippingLinks.to_json())

# convert the object into a dict
postal_service_with_channel_and_shipping_links_dict = postal_service_with_channel_and_shipping_links_instance.to_dict()
# create an instance of PostalServiceWithChannelAndShippingLinks from a dict
postal_service_with_channel_and_shipping_links_from_dict = PostalServiceWithChannelAndShippingLinks.from_dict(postal_service_with_channel_and_shipping_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


