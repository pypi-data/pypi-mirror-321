# ProcessTemplatesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_type** | **str** |  | [optional] 
**channel_name** | **str** |  | [optional] 
**template_requests** | [**List[TemplateToProcess]**](TemplateToProcess.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.genericlistings.models.process_templates_request import ProcessTemplatesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessTemplatesRequest from a JSON string
process_templates_request_instance = ProcessTemplatesRequest.from_json(json)
# print the JSON string representation of the object
print(ProcessTemplatesRequest.to_json())

# convert the object into a dict
process_templates_request_dict = process_templates_request_instance.to_dict()
# create an instance of ProcessTemplatesRequest from a dict
process_templates_request_from_dict = ProcessTemplatesRequest.from_dict(process_templates_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


