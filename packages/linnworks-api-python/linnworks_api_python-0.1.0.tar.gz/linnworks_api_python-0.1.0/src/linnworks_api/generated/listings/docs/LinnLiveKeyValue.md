# LinnLiveKeyValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.linn_live_key_value import LinnLiveKeyValue

# TODO update the JSON string below
json = "{}"
# create an instance of LinnLiveKeyValue from a JSON string
linn_live_key_value_instance = LinnLiveKeyValue.from_json(json)
# print the JSON string representation of the object
print(LinnLiveKeyValue.to_json())

# convert the object into a dict
linn_live_key_value_dict = linn_live_key_value_instance.to_dict()
# create an instance of LinnLiveKeyValue from a dict
linn_live_key_value_from_dict = LinnLiveKeyValue.from_dict(linn_live_key_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


