# SaveTemplateFieldsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_type** | **str** |  | [optional] 
**channel_name** | **str** |  | [optional] 
**template_id** | **int** |  | [optional] 
**fields_to_save** | **Dict[str, object]** | info key : value | [optional] 

## Example

```python
from linnworks_api.generated.genericlistings.models.save_template_fields_request import SaveTemplateFieldsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SaveTemplateFieldsRequest from a JSON string
save_template_fields_request_instance = SaveTemplateFieldsRequest.from_json(json)
# print the JSON string representation of the object
print(SaveTemplateFieldsRequest.to_json())

# convert the object into a dict
save_template_fields_request_dict = save_template_fields_request_instance.to_dict()
# create an instance of SaveTemplateFieldsRequest from a dict
save_template_fields_request_from_dict = SaveTemplateFieldsRequest.from_dict(save_template_fields_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


