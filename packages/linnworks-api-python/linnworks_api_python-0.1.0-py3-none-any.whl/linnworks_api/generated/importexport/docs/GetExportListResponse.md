# GetExportListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**register** | [**List[ExportRegisterPublicSchedules]**](ExportRegisterPublicSchedules.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.importexport.models.get_export_list_response import GetExportListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetExportListResponse from a JSON string
get_export_list_response_instance = GetExportListResponse.from_json(json)
# print the JSON string representation of the object
print(GetExportListResponse.to_json())

# convert the object into a dict
get_export_list_response_dict = get_export_list_response_instance.to_dict()
# create an instance of GetExportListResponse from a dict
get_export_list_response_from_dict = GetExportListResponse.from_dict(get_export_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


