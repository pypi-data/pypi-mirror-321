# ImportExportRunNowExportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**export_id** | **int** | Export id to execute | [optional] 

## Example

```python
from linnworks_api.generated.importexport.models.import_export_run_now_export_request import ImportExportRunNowExportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImportExportRunNowExportRequest from a JSON string
import_export_run_now_export_request_instance = ImportExportRunNowExportRequest.from_json(json)
# print the JSON string representation of the object
print(ImportExportRunNowExportRequest.to_json())

# convert the object into a dict
import_export_run_now_export_request_dict = import_export_run_now_export_request_instance.to_dict()
# create an instance of ImportExportRunNowExportRequest from a dict
import_export_run_now_export_request_from_dict = ImportExportRunNowExportRequest.from_dict(import_export_run_now_export_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


