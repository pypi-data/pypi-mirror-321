# GetImportListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**register** | [**List[ImportRegisterPublicSchedules]**](ImportRegisterPublicSchedules.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.importexport.models.get_import_list_response import GetImportListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetImportListResponse from a JSON string
get_import_list_response_instance = GetImportListResponse.from_json(json)
# print the JSON string representation of the object
print(GetImportListResponse.to_json())

# convert the object into a dict
get_import_list_response_dict = get_import_list_response_instance.to_dict()
# create an instance of GetImportListResponse from a dict
get_import_list_response_from_dict = GetImportListResponse.from_dict(get_import_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


