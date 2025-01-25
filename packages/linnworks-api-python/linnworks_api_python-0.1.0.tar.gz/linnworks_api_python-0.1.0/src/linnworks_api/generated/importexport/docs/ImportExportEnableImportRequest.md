# ImportExportEnableImportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**import_id** | **int** | Import id to enable/disable | [optional] 
**enable** | **bool** | Boolean value to indicate the state | [optional] 

## Example

```python
from linnworks_api.generated.importexport.models.import_export_enable_import_request import ImportExportEnableImportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImportExportEnableImportRequest from a JSON string
import_export_enable_import_request_instance = ImportExportEnableImportRequest.from_json(json)
# print the JSON string representation of the object
print(ImportExportEnableImportRequest.to_json())

# convert the object into a dict
import_export_enable_import_request_dict = import_export_enable_import_request_instance.to_dict()
# create an instance of ImportExportEnableImportRequest from a dict
import_export_enable_import_request_from_dict = ImportExportEnableImportRequest.from_dict(import_export_enable_import_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


