# ImportSettingModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**separator_type** | [**CsvSeparatorType**](CsvSeparatorType.md) |  | [optional] 
**contains_columns** | **bool** |  | [optional] 
**column_mappings** | [**List[ImportColumnMappingModel]**](ImportColumnMappingModel.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.import_setting_model import ImportSettingModel

# TODO update the JSON string below
json = "{}"
# create an instance of ImportSettingModel from a JSON string
import_setting_model_instance = ImportSettingModel.from_json(json)
# print the JSON string representation of the object
print(ImportSettingModel.to_json())

# convert the object into a dict
import_setting_model_dict = import_setting_model_instance.to_dict()
# create an instance of ImportSettingModel from a dict
import_setting_model_from_dict = ImportSettingModel.from_dict(import_setting_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


