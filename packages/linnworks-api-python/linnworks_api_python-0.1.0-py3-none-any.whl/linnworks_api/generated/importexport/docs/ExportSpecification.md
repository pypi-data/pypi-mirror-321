# ExportSpecification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**export_column_names** | **bool** |  | [optional] 
**delimiter** | **str** |  | [optional] 
**escape** | **str** |  | [optional] 
**custom_script** | **str** |  | [optional] 
**export_time_zone** | **str** |  | [optional] 
**feed** | [**ExportGenericFeed**](ExportGenericFeed.md) |  | [optional] 
**column_mappings** | [**List[ExportColumn]**](ExportColumn.md) |  | [optional] 
**execution_options** | [**List[ExecutionOption]**](ExecutionOption.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.importexport.models.export_specification import ExportSpecification

# TODO update the JSON string below
json = "{}"
# create an instance of ExportSpecification from a JSON string
export_specification_instance = ExportSpecification.from_json(json)
# print the JSON string representation of the object
print(ExportSpecification.to_json())

# convert the object into a dict
export_specification_dict = export_specification_instance.to_dict()
# create an instance of ExportSpecification from a dict
export_specification_from_dict = ExportSpecification.from_dict(export_specification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


