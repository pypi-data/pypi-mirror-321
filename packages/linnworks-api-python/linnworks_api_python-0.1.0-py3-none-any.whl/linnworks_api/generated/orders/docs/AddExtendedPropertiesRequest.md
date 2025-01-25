# AddExtendedPropertiesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | Order id of the order to append extended properties to | [optional] 
**extended_properties** | [**List[BasicExtendedProperty]**](BasicExtendedProperty.md) | Array of basic extended properties to be added | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.add_extended_properties_request import AddExtendedPropertiesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddExtendedPropertiesRequest from a JSON string
add_extended_properties_request_instance = AddExtendedPropertiesRequest.from_json(json)
# print the JSON string representation of the object
print(AddExtendedPropertiesRequest.to_json())

# convert the object into a dict
add_extended_properties_request_dict = add_extended_properties_request_instance.to_dict()
# create an instance of AddExtendedPropertiesRequest from a dict
add_extended_properties_request_from_dict = AddExtendedPropertiesRequest.from_dict(add_extended_properties_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


