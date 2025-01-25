# TemplateToProcess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **int** |  | [optional] 
**action** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.genericlistings.models.template_to_process import TemplateToProcess

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateToProcess from a JSON string
template_to_process_instance = TemplateToProcess.from_json(json)
# print the JSON string representation of the object
print(TemplateToProcess.to_json())

# convert the object into a dict
template_to_process_dict = template_to_process_instance.to_dict()
# create an instance of TemplateToProcess from a dict
template_to_process_from_dict = TemplateToProcess.from_dict(template_to_process_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


