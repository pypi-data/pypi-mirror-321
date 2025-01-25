# ImportStockRequestSettingModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**separator_type** | [**CsvSeparatorType**](CsvSeparatorType.md) |  | [optional] 
**contains_columns** | **bool** |  | [optional] 
**column_mappings** | [**List[ImportColumnStockRequestMappingModel]**](ImportColumnStockRequestMappingModel.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.import_stock_request_setting_model import ImportStockRequestSettingModel

# TODO update the JSON string below
json = "{}"
# create an instance of ImportStockRequestSettingModel from a JSON string
import_stock_request_setting_model_instance = ImportStockRequestSettingModel.from_json(json)
# print the JSON string representation of the object
print(ImportStockRequestSettingModel.to_json())

# convert the object into a dict
import_stock_request_setting_model_dict = import_stock_request_setting_model_instance.to_dict()
# create an instance of ImportStockRequestSettingModel from a dict
import_stock_request_setting_model_from_dict = ImportStockRequestSettingModel.from_dict(import_stock_request_setting_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


