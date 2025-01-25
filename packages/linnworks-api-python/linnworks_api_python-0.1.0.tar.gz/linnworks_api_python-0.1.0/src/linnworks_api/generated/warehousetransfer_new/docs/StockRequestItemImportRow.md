# StockRequestItemImportRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ImportStockRequestColumn**](ImportStockRequestColumn.md) |  | [optional] 
**name** | **str** |  | [optional] 
**sample** | **str** |  | [optional] 
**group** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.stock_request_item_import_row import StockRequestItemImportRow

# TODO update the JSON string below
json = "{}"
# create an instance of StockRequestItemImportRow from a JSON string
stock_request_item_import_row_instance = StockRequestItemImportRow.from_json(json)
# print the JSON string representation of the object
print(StockRequestItemImportRow.to_json())

# convert the object into a dict
stock_request_item_import_row_dict = stock_request_item_import_row_instance.to_dict()
# create an instance of StockRequestItemImportRow from a dict
stock_request_item_import_row_from_dict = StockRequestItemImportRow.from_dict(stock_request_item_import_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


