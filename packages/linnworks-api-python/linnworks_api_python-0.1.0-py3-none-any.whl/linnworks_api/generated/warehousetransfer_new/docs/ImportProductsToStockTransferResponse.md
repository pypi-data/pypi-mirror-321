# ImportProductsToStockTransferResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inserted_ids** | **List[int]** |  | [optional] 
**updated_ids** | **List[int]** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.import_products_to_stock_transfer_response import ImportProductsToStockTransferResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ImportProductsToStockTransferResponse from a JSON string
import_products_to_stock_transfer_response_instance = ImportProductsToStockTransferResponse.from_json(json)
# print the JSON string representation of the object
print(ImportProductsToStockTransferResponse.to_json())

# convert the object into a dict
import_products_to_stock_transfer_response_dict = import_products_to_stock_transfer_response_instance.to_dict()
# create an instance of ImportProductsToStockTransferResponse from a dict
import_products_to_stock_transfer_response_from_dict = ImportProductsToStockTransferResponse.from_dict(import_products_to_stock_transfer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


