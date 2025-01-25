# EbayShippingService


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** |  | [optional] 
**service_name** | **str** |  | [optional] 
**is_international_service** | **bool** |  | [optional] 
**is_expedited_service** | **bool** |  | [optional] 
**service_type** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.ebay_shipping_service import EbayShippingService

# TODO update the JSON string below
json = "{}"
# create an instance of EbayShippingService from a JSON string
ebay_shipping_service_instance = EbayShippingService.from_json(json)
# print the JSON string representation of the object
print(EbayShippingService.to_json())

# convert the object into a dict
ebay_shipping_service_dict = ebay_shipping_service_instance.to_dict()
# create an instance of EbayShippingService from a dict
ebay_shipping_service_from_dict = EbayShippingService.from_dict(ebay_shipping_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


