# ExportColumn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | **int** |  | [optional] 
**filters** | [**Filters**](Filters.md) |  | [optional] 
**export_to_file** | **bool** |  | [optional] 
**sub_query_selection** | [**List[SubQueryOutputMappingSelectionField]**](SubQueryOutputMappingSelectionField.md) |  | [optional] 
**file_column** | **str** |  | [optional] 
**column** | **str** |  | [optional] 
**expression** | **str** |  | [optional] 
**default_value** | **str** |  | [optional] 
**visible** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.importexport.models.export_column import ExportColumn

# TODO update the JSON string below
json = "{}"
# create an instance of ExportColumn from a JSON string
export_column_instance = ExportColumn.from_json(json)
# print the JSON string representation of the object
print(ExportColumn.to_json())

# convert the object into a dict
export_column_dict = export_column_instance.to_dict()
# create an instance of ExportColumn from a dict
export_column_from_dict = ExportColumn.from_dict(export_column_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


