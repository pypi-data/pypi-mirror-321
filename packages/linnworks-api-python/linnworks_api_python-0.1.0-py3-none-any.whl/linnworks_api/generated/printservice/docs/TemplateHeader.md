# TemplateHeader


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_template_row_id** | **int** |  | [optional] 
**template_id** | **str** |  | [optional] 
**template_type** | **str** |  | [optional] 
**template_name** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**is_default** | **bool** |  | [optional] 
**is_email_attachment** | **bool** |  | [optional] 
**visibility_condition** | **str** |  | [optional] 
**b_logical_delete** | **bool** |  | [optional] 
**is_conditional** | **bool** |  | [optional] [readonly] 
**condition_rating** | **int** |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.printservice.models.template_header import TemplateHeader

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateHeader from a JSON string
template_header_instance = TemplateHeader.from_json(json)
# print the JSON string representation of the object
print(TemplateHeader.to_json())

# convert the object into a dict
template_header_dict = template_header_instance.to_dict()
# create an instance of TemplateHeader from a dict
template_header_from_dict = TemplateHeader.from_dict(template_header_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


