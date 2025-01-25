# BasicExtendedProperty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.basic_extended_property import BasicExtendedProperty

# TODO update the JSON string below
json = "{}"
# create an instance of BasicExtendedProperty from a JSON string
basic_extended_property_instance = BasicExtendedProperty.from_json(json)
# print the JSON string representation of the object
print(BasicExtendedProperty.to_json())

# convert the object into a dict
basic_extended_property_dict = basic_extended_property_instance.to_dict()
# create an instance of BasicExtendedProperty from a dict
basic_extended_property_from_dict = BasicExtendedProperty.from_dict(basic_extended_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


