# ImportExportEnableExportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**export_id** | **int** | Export id to enable/disable | [optional] 
**enable** | **bool** | Boolean value to indicate the state | [optional] 

## Example

```python
from linnworks_api.generated.importexport.models.import_export_enable_export_request import ImportExportEnableExportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImportExportEnableExportRequest from a JSON string
import_export_enable_export_request_instance = ImportExportEnableExportRequest.from_json(json)
# print the JSON string representation of the object
print(ImportExportEnableExportRequest.to_json())

# convert the object into a dict
import_export_enable_export_request_dict = import_export_enable_export_request_instance.to_dict()
# create an instance of ImportExportEnableExportRequest from a dict
import_export_enable_export_request_from_dict = ImportExportEnableExportRequest.from_dict(import_export_enable_export_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


