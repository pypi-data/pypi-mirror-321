# DeleteConfiguratorsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted_ids** | **List[int]** |  | [optional] 

## Example

```python
from linnworks_api.generated.genericlistings.models.delete_configurators_response import DeleteConfiguratorsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteConfiguratorsResponse from a JSON string
delete_configurators_response_instance = DeleteConfiguratorsResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteConfiguratorsResponse.to_json())

# convert the object into a dict
delete_configurators_response_dict = delete_configurators_response_instance.to_dict()
# create an instance of DeleteConfiguratorsResponse from a dict
delete_configurators_response_from_dict = DeleteConfiguratorsResponse.from_dict(delete_configurators_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


