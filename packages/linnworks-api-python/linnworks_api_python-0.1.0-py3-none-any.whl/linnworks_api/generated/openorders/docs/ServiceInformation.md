# ServiceInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**identifier** | **str** |  | [optional] 
**logo** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.openorders.models.service_information import ServiceInformation

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceInformation from a JSON string
service_information_instance = ServiceInformation.from_json(json)
# print the JSON string representation of the object
print(ServiceInformation.to_json())

# convert the object into a dict
service_information_dict = service_information_instance.to_dict()
# create an instance of ServiceInformation from a dict
service_information_from_dict = ServiceInformation.from_dict(service_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


