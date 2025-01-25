# ImportExportDeleteImportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Id of the import to delete | [optional] 

## Example

```python
from linnworks_api.generated.importexport.models.import_export_delete_import_request import ImportExportDeleteImportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImportExportDeleteImportRequest from a JSON string
import_export_delete_import_request_instance = ImportExportDeleteImportRequest.from_json(json)
# print the JSON string representation of the object
print(ImportExportDeleteImportRequest.to_json())

# convert the object into a dict
import_export_delete_import_request_dict = import_export_delete_import_request_instance.to_dict()
# create an instance of ImportExportDeleteImportRequest from a dict
import_export_delete_import_request_from_dict = ImportExportDeleteImportRequest.from_dict(import_export_delete_import_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


