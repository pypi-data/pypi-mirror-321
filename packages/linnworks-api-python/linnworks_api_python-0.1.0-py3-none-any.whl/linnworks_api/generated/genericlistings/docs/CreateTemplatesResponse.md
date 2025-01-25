# CreateTemplatesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**templates_info** | **List[object]** |  | [optional] 
**all_created_ids** | **List[int]** |  | [optional] 

## Example

```python
from linnworks_api.generated.genericlistings.models.create_templates_response import CreateTemplatesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTemplatesResponse from a JSON string
create_templates_response_instance = CreateTemplatesResponse.from_json(json)
# print the JSON string representation of the object
print(CreateTemplatesResponse.to_json())

# convert the object into a dict
create_templates_response_dict = create_templates_response_instance.to_dict()
# create an instance of CreateTemplatesResponse from a dict
create_templates_response_from_dict = CreateTemplatesResponse.from_dict(create_templates_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


