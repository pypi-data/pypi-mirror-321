# ImportColumnStockRequestMappingModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_column_type** | [**ImportStockRequestColumn**](ImportStockRequestColumn.md) |  | [optional] 
**user_defined_column** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.import_column_stock_request_mapping_model import ImportColumnStockRequestMappingModel

# TODO update the JSON string below
json = "{}"
# create an instance of ImportColumnStockRequestMappingModel from a JSON string
import_column_stock_request_mapping_model_instance = ImportColumnStockRequestMappingModel.from_json(json)
# print the JSON string representation of the object
print(ImportColumnStockRequestMappingModel.to_json())

# convert the object into a dict
import_column_stock_request_mapping_model_dict = import_column_stock_request_mapping_model_instance.to_dict()
# create an instance of ImportColumnStockRequestMappingModel from a dict
import_column_stock_request_mapping_model_from_dict = ImportColumnStockRequestMappingModel.from_dict(import_column_stock_request_mapping_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


