# WarehouseTransferStockItemModelGenericPagedResult

Order item object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_number** | **int** | Result page number | [optional] 
**entries_per_page** | **int** | Result page size, quantity of records per page | [optional] 
**total_entries** | **int** | Total records | [optional] 
**total_pages** | **int** | Total pages | [optional] [readonly] 
**data** | [**List[WarehouseTransferStockItemModel]**](WarehouseTransferStockItemModel.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.warehouse_transfer_stock_item_model_generic_paged_result import WarehouseTransferStockItemModelGenericPagedResult

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseTransferStockItemModelGenericPagedResult from a JSON string
warehouse_transfer_stock_item_model_generic_paged_result_instance = WarehouseTransferStockItemModelGenericPagedResult.from_json(json)
# print the JSON string representation of the object
print(WarehouseTransferStockItemModelGenericPagedResult.to_json())

# convert the object into a dict
warehouse_transfer_stock_item_model_generic_paged_result_dict = warehouse_transfer_stock_item_model_generic_paged_result_instance.to_dict()
# create an instance of WarehouseTransferStockItemModelGenericPagedResult from a dict
warehouse_transfer_stock_item_model_generic_paged_result_from_dict = WarehouseTransferStockItemModelGenericPagedResult.from_dict(warehouse_transfer_stock_item_model_generic_paged_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


