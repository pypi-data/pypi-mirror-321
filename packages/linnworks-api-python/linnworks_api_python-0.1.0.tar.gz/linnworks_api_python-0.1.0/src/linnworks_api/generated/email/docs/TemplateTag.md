# TemplateTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**selection_path** | **str** |  | [optional] 
**is_list** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.email.models.template_tag import TemplateTag

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateTag from a JSON string
template_tag_instance = TemplateTag.from_json(json)
# print the JSON string representation of the object
print(TemplateTag.to_json())

# convert the object into a dict
template_tag_dict = template_tag_instance.to_dict()
# create an instance of TemplateTag from a dict
template_tag_from_dict = TemplateTag.from_dict(template_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


