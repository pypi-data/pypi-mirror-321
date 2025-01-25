# DeleteConfiguratorsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_type** | **str** |  | [optional] 
**channel_name** | **str** |  | [optional] 
**configurator_ids** | **List[int]** |  | [optional] 

## Example

```python
from linnworks_api.generated.genericlistings.models.delete_configurators_request import DeleteConfiguratorsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteConfiguratorsRequest from a JSON string
delete_configurators_request_instance = DeleteConfiguratorsRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteConfiguratorsRequest.to_json())

# convert the object into a dict
delete_configurators_request_dict = delete_configurators_request_instance.to_dict()
# create an instance of DeleteConfiguratorsRequest from a dict
delete_configurators_request_from_dict = DeleteConfiguratorsRequest.from_dict(delete_configurators_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


