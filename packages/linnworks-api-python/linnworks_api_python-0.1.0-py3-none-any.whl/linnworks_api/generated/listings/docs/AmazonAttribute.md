# AmazonAttribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr_name** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**linnworks_property** | **str** |  | [optional] 
**listing_property** | **str** |  | [optional] 
**default_value** | **str** |  | [optional] 
**required** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**real_type** | **str** |  | [optional] 
**valid_values** | [**List[LinnLiveKeyValue]**](LinnLiveKeyValue.md) |  | [optional] 
**path** | **str** |  | [optional] 
**is_variation** | **bool** |  | [optional] 
**is_invalid_value** | **bool** |  | [optional] 
**error_message** | **str** |  | [optional] 
**can_be_variation** | **bool** |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.listings.models.amazon_attribute import AmazonAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of AmazonAttribute from a JSON string
amazon_attribute_instance = AmazonAttribute.from_json(json)
# print the JSON string representation of the object
print(AmazonAttribute.to_json())

# convert the object into a dict
amazon_attribute_dict = amazon_attribute_instance.to_dict()
# create an instance of AmazonAttribute from a dict
amazon_attribute_from_dict = AmazonAttribute.from_dict(amazon_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


