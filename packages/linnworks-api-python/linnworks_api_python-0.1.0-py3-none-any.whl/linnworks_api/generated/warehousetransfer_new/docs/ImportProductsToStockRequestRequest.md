# ImportProductsToStockRequestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transfer_id** | **int** |  | [optional] 
**file_id** | **str** |  | [optional] 
**settings** | [**ImportStockRequestSettingModel**](ImportStockRequestSettingModel.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.import_products_to_stock_request_request import ImportProductsToStockRequestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImportProductsToStockRequestRequest from a JSON string
import_products_to_stock_request_request_instance = ImportProductsToStockRequestRequest.from_json(json)
# print the JSON string representation of the object
print(ImportProductsToStockRequestRequest.to_json())

# convert the object into a dict
import_products_to_stock_request_request_dict = import_products_to_stock_request_request_instance.to_dict()
# create an instance of ImportProductsToStockRequestRequest from a dict
import_products_to_stock_request_request_from_dict = ImportProductsToStockRequestRequest.from_dict(import_products_to_stock_request_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


