# Export


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**specification** | [**ExportSpecification**](ExportSpecification.md) |  | [optional] 
**register** | [**ExportRegister**](ExportRegister.md) |  | [optional] 
**schedules** | [**List[Schedule]**](Schedule.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.importexport.models.export import Export

# TODO update the JSON string below
json = "{}"
# create an instance of Export from a JSON string
export_instance = Export.from_json(json)
# print the JSON string representation of the object
print(Export.to_json())

# convert the object into a dict
export_dict = export_instance.to_dict()
# create an instance of Export from a dict
export_from_dict = Export.from_dict(export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


