# ImportColumnStockTransferMappingModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_column_type** | [**ImportStockTransferColumn**](ImportStockTransferColumn.md) |  | [optional] 
**user_defined_column** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.import_column_stock_transfer_mapping_model import ImportColumnStockTransferMappingModel

# TODO update the JSON string below
json = "{}"
# create an instance of ImportColumnStockTransferMappingModel from a JSON string
import_column_stock_transfer_mapping_model_instance = ImportColumnStockTransferMappingModel.from_json(json)
# print the JSON string representation of the object
print(ImportColumnStockTransferMappingModel.to_json())

# convert the object into a dict
import_column_stock_transfer_mapping_model_dict = import_column_stock_transfer_mapping_model_instance.to_dict()
# create an instance of ImportColumnStockTransferMappingModel from a dict
import_column_stock_transfer_mapping_model_from_dict = ImportColumnStockTransferMappingModel.from_dict(import_column_stock_transfer_mapping_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


