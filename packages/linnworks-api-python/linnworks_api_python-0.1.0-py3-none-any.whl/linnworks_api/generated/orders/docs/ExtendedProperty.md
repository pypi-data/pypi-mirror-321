# ExtendedProperty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**row_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.extended_property import ExtendedProperty

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendedProperty from a JSON string
extended_property_instance = ExtendedProperty.from_json(json)
# print the JSON string representation of the object
print(ExtendedProperty.to_json())

# convert the object into a dict
extended_property_dict = extended_property_instance.to_dict()
# create an instance of ExtendedProperty from a dict
extended_property_from_dict = ExtendedProperty.from_dict(extended_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


