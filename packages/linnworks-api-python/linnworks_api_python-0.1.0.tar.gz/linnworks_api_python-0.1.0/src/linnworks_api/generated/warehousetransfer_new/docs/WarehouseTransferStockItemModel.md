# WarehouseTransferStockItemModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_item_id** | **str** | Stock Item Guid | [optional] 
**stock_item_int_id** | **int** | Stock Item integer Id | [optional] 
**item_number** | **str** | SKU | [optional] 
**item_title** | **str** | Item title | [optional] 
**from_available_quantity** | **int** | Available (Ship from) | [optional] 
**destination_available_quantity** | **int** | Available (Destination Warehouse) | [optional] 
**from_due_quantity** | **int** | Due (Ship From Warehouse) | [optional] 
**thumbnail_source** | **str** |  | [optional] 
**rows_count** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.warehouse_transfer_stock_item_model import WarehouseTransferStockItemModel

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseTransferStockItemModel from a JSON string
warehouse_transfer_stock_item_model_instance = WarehouseTransferStockItemModel.from_json(json)
# print the JSON string representation of the object
print(WarehouseTransferStockItemModel.to_json())

# convert the object into a dict
warehouse_transfer_stock_item_model_dict = warehouse_transfer_stock_item_model_instance.to_dict()
# create an instance of WarehouseTransferStockItemModel from a dict
warehouse_transfer_stock_item_model_from_dict = WarehouseTransferStockItemModel.from_dict(warehouse_transfer_stock_item_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


