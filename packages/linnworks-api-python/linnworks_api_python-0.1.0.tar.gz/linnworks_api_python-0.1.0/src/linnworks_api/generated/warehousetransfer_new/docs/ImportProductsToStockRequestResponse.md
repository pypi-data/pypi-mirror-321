# ImportProductsToStockRequestResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inserted_ids** | **List[int]** |  | [optional] 
**updated_ids** | **List[int]** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.import_products_to_stock_request_response import ImportProductsToStockRequestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ImportProductsToStockRequestResponse from a JSON string
import_products_to_stock_request_response_instance = ImportProductsToStockRequestResponse.from_json(json)
# print the JSON string representation of the object
print(ImportProductsToStockRequestResponse.to_json())

# convert the object into a dict
import_products_to_stock_request_response_dict = import_products_to_stock_request_response_instance.to_dict()
# create an instance of ImportProductsToStockRequestResponse from a dict
import_products_to_stock_request_response_from_dict = ImportProductsToStockRequestResponse.from_dict(import_products_to_stock_request_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


