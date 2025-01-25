# ServiceProperty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_name** | **str** |  | [optional] 
**property_value** | **str** |  | [optional] 
**service_id** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.shippingservice.models.service_property import ServiceProperty

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceProperty from a JSON string
service_property_instance = ServiceProperty.from_json(json)
# print the JSON string representation of the object
print(ServiceProperty.to_json())

# convert the object into a dict
service_property_dict = service_property_instance.to_dict()
# create an instance of ServiceProperty from a dict
service_property_from_dict = ServiceProperty.from_dict(service_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


