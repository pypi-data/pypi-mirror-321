# AssociatedTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **str** |  | [optional] 
**used_config_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**site** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.associated_template import AssociatedTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of AssociatedTemplate from a JSON string
associated_template_instance = AssociatedTemplate.from_json(json)
# print the JSON string representation of the object
print(AssociatedTemplate.to_json())

# convert the object into a dict
associated_template_dict = associated_template_instance.to_dict()
# create an instance of AssociatedTemplate from a dict
associated_template_from_dict = AssociatedTemplate.from_dict(associated_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


