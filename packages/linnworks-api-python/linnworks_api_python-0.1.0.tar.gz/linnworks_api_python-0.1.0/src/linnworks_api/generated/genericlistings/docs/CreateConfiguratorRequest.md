# CreateConfiguratorRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_type** | **str** |  | [optional] 
**configurator_name** | **str** |  | [optional] 
**channel_id** | **int** |  | [optional] 
**channel_name** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.genericlistings.models.create_configurator_request import CreateConfiguratorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConfiguratorRequest from a JSON string
create_configurator_request_instance = CreateConfiguratorRequest.from_json(json)
# print the JSON string representation of the object
print(CreateConfiguratorRequest.to_json())

# convert the object into a dict
create_configurator_request_dict = create_configurator_request_instance.to_dict()
# create an instance of CreateConfiguratorRequest from a dict
create_configurator_request_from_dict = CreateConfiguratorRequest.from_dict(create_configurator_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


