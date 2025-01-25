# ProcessTemplatesParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | [optional] 
**sub_source** | **str** |  | [optional] 
**config_id** | **str** |  | [optional] 
**inventory_item_ids** | **List[str]** |  | [optional] 
**selected_regions** | [**List[TupleInt32Int32]**](TupleInt32Int32.md) |  | [optional] 
**token** | **str** |  | [optional] 
**templates_type** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.process_templates_parameters import ProcessTemplatesParameters

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessTemplatesParameters from a JSON string
process_templates_parameters_instance = ProcessTemplatesParameters.from_json(json)
# print the JSON string representation of the object
print(ProcessTemplatesParameters.to_json())

# convert the object into a dict
process_templates_parameters_dict = process_templates_parameters_instance.to_dict()
# create an instance of ProcessTemplatesParameters from a dict
process_templates_parameters_from_dict = ProcessTemplatesParameters.from_dict(process_templates_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


