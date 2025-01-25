# CreateConfiguratorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_configurator_info** | **object** |  | [optional] 
**created_configurator_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.genericlistings.models.create_configurator_response import CreateConfiguratorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConfiguratorResponse from a JSON string
create_configurator_response_instance = CreateConfiguratorResponse.from_json(json)
# print the JSON string representation of the object
print(CreateConfiguratorResponse.to_json())

# convert the object into a dict
create_configurator_response_dict = create_configurator_response_instance.to_dict()
# create an instance of CreateConfiguratorResponse from a dict
create_configurator_response_from_dict = CreateConfiguratorResponse.from_dict(create_configurator_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


