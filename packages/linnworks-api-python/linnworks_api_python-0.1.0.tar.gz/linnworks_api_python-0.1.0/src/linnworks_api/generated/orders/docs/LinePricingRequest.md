# LinePricingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price_per_unit** | **float** |  | [optional] 
**discount_percentage** | **float** |  | [optional] 
**tax_rate_percentage** | **float** |  | [optional] 
**tax_inclusive** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.line_pricing_request import LinePricingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LinePricingRequest from a JSON string
line_pricing_request_instance = LinePricingRequest.from_json(json)
# print the JSON string representation of the object
print(LinePricingRequest.to_json())

# convert the object into a dict
line_pricing_request_dict = line_pricing_request_instance.to_dict()
# create an instance of LinePricingRequest from a dict
line_pricing_request_from_dict = LinePricingRequest.from_dict(line_pricing_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


