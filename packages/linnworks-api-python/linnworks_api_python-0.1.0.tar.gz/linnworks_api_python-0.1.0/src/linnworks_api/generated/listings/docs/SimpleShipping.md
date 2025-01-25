# SimpleShipping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expedited_shipping** | [**LinnLiveKeyValue**](LinnLiveKeyValue.md) |  | [optional] 
**will_ship_internationally** | [**LinnLiveKeyValue**](LinnLiveKeyValue.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.simple_shipping import SimpleShipping

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleShipping from a JSON string
simple_shipping_instance = SimpleShipping.from_json(json)
# print the JSON string representation of the object
print(SimpleShipping.to_json())

# convert the object into a dict
simple_shipping_dict = simple_shipping_instance.to_dict()
# create an instance of SimpleShipping from a dict
simple_shipping_from_dict = SimpleShipping.from_dict(simple_shipping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


