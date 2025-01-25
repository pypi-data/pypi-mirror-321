# OrderExtendedProperty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rowid** | **str** |  | [optional] 
**property_name** | **str** |  | [optional] 
**property_value** | **str** |  | [optional] 
**property_type** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.processedorders.models.order_extended_property import OrderExtendedProperty

# TODO update the JSON string below
json = "{}"
# create an instance of OrderExtendedProperty from a JSON string
order_extended_property_instance = OrderExtendedProperty.from_json(json)
# print the JSON string representation of the object
print(OrderExtendedProperty.to_json())

# convert the object into a dict
order_extended_property_dict = order_extended_property_instance.to_dict()
# create an instance of OrderExtendedProperty from a dict
order_extended_property_from_dict = OrderExtendedProperty.from_dict(order_extended_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


