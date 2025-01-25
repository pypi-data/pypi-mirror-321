# AmazonShipping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ship_option** | **str** |  | [optional] 
**service_level** | **str** |  | [optional] 
**shipping_cost** | **float** |  | [optional] 
**shipping_cost_extended_property** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**is_shipping_restricted** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.amazon_shipping import AmazonShipping

# TODO update the JSON string below
json = "{}"
# create an instance of AmazonShipping from a JSON string
amazon_shipping_instance = AmazonShipping.from_json(json)
# print the JSON string representation of the object
print(AmazonShipping.to_json())

# convert the object into a dict
amazon_shipping_dict = amazon_shipping_instance.to_dict()
# create an instance of AmazonShipping from a dict
amazon_shipping_from_dict = AmazonShipping.from_dict(amazon_shipping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


