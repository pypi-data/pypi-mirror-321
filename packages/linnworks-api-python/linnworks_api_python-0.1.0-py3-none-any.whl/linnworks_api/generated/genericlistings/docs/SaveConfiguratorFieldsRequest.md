# SaveConfiguratorFieldsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_type** | **str** |  | [optional] 
**channel_name** | **str** |  | [optional] 
**configurator_id** | **int** |  | [optional] 
**fields_to_save** | **Dict[str, object]** | info key : value | [optional] 

## Example

```python
from linnworks_api.generated.genericlistings.models.save_configurator_fields_request import SaveConfiguratorFieldsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SaveConfiguratorFieldsRequest from a JSON string
save_configurator_fields_request_instance = SaveConfiguratorFieldsRequest.from_json(json)
# print the JSON string representation of the object
print(SaveConfiguratorFieldsRequest.to_json())

# convert the object into a dict
save_configurator_fields_request_dict = save_configurator_fields_request_instance.to_dict()
# create an instance of SaveConfiguratorFieldsRequest from a dict
save_configurator_fields_request_from_dict = SaveConfiguratorFieldsRequest.from_dict(save_configurator_fields_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


