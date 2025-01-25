# ImportStockTransferSettingModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**separator_type** | [**CsvSeparatorType**](CsvSeparatorType.md) |  | [optional] 
**contains_columns** | **bool** |  | [optional] 
**column_mappings** | [**List[ImportColumnStockTransferMappingModel]**](ImportColumnStockTransferMappingModel.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.import_stock_transfer_setting_model import ImportStockTransferSettingModel

# TODO update the JSON string below
json = "{}"
# create an instance of ImportStockTransferSettingModel from a JSON string
import_stock_transfer_setting_model_instance = ImportStockTransferSettingModel.from_json(json)
# print the JSON string representation of the object
print(ImportStockTransferSettingModel.to_json())

# convert the object into a dict
import_stock_transfer_setting_model_dict = import_stock_transfer_setting_model_instance.to_dict()
# create an instance of ImportStockTransferSettingModel from a dict
import_stock_transfer_setting_model_from_dict = ImportStockTransferSettingModel.from_dict(import_stock_transfer_setting_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


