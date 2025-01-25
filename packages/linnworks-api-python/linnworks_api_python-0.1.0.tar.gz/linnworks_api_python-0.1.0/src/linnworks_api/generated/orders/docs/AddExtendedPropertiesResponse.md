# AddExtendedPropertiesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extended_properties_inserted** | **int** | The number of extended properties that were added | [optional] 
**errors** | **List[str]** | An array of errors created when attempting to add | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.add_extended_properties_response import AddExtendedPropertiesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddExtendedPropertiesResponse from a JSON string
add_extended_properties_response_instance = AddExtendedPropertiesResponse.from_json(json)
# print the JSON string representation of the object
print(AddExtendedPropertiesResponse.to_json())

# convert the object into a dict
add_extended_properties_response_dict = add_extended_properties_response_instance.to_dict()
# create an instance of AddExtendedPropertiesResponse from a dict
add_extended_properties_response_from_dict = AddExtendedPropertiesResponse.from_dict(add_extended_properties_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


