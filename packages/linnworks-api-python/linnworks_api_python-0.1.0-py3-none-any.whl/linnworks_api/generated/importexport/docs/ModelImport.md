# ModelImport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**specification** | [**SpecificationImportGenericFeedImportColumn**](SpecificationImportGenericFeedImportColumn.md) |  | [optional] 
**register** | [**ImportRegister**](ImportRegister.md) |  | [optional] 
**schedules** | [**List[Schedule]**](Schedule.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.importexport.models.model_import import ModelImport

# TODO update the JSON string below
json = "{}"
# create an instance of ModelImport from a JSON string
model_import_instance = ModelImport.from_json(json)
# print the JSON string representation of the object
print(ModelImport.to_json())

# convert the object into a dict
model_import_dict = model_import_instance.to_dict()
# create an instance of ModelImport from a dict
model_import_from_dict = ModelImport.from_dict(model_import_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


