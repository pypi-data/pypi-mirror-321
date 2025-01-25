# Shipping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipping_service** | [**EbayShippingService**](EbayShippingService.md) |  | [optional] 
**price** | **float** |  | [optional] 
**price_extended_property** | **str** |  | [optional] 
**additional_price** | **float** |  | [optional] 
**additional_price_extended_property** | **str** |  | [optional] 
**handling_price** | **float** |  | [optional] 
**shipping_locations** | [**List[KeyValue]**](KeyValue.md) |  | [optional] 
**weight_rules** | [**List[EbayWeightRule]**](EbayWeightRule.md) |  | [optional] 
**price_association_rules** | [**List[EbayPriceRule]**](EbayPriceRule.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.shipping import Shipping

# TODO update the JSON string below
json = "{}"
# create an instance of Shipping from a JSON string
shipping_instance = Shipping.from_json(json)
# print the JSON string representation of the object
print(Shipping.to_json())

# convert the object into a dict
shipping_dict = shipping_instance.to_dict()
# create an instance of Shipping from a dict
shipping_from_dict = Shipping.from_dict(shipping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


