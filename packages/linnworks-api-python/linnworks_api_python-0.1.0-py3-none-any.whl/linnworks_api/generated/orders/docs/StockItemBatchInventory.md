# StockItemBatchInventory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_inventory_id** | **int** |  | [optional] 
**batch_id** | **int** |  | [optional] 
**stock_location_id** | **str** |  | [optional] 
**bin_rack** | **str** |  | [optional] 
**priority_sequence** | **int** |  | [optional] 
**quantity** | **int** |  | [optional] 
**stock_value** | **float** |  | [optional] 
**start_quantity** | **int** |  | [optional] [readonly] 
**picked_quantity** | **int** |  | [optional] 
**batch_status** | **str** |  | [optional] 
**is_deleted** | **bool** |  | [optional] 
**warehouse_binrack_standard_type** | **int** |  | [optional] 
**warehouse_binrack_type_name** | **str** |  | [optional] 
**in_transfer** | **int** |  | [optional] 
**bin_rack_id** | **int** |  | [optional] 
**warehouse_binrack_type_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.stock_item_batch_inventory import StockItemBatchInventory

# TODO update the JSON string below
json = "{}"
# create an instance of StockItemBatchInventory from a JSON string
stock_item_batch_inventory_instance = StockItemBatchInventory.from_json(json)
# print the JSON string representation of the object
print(StockItemBatchInventory.to_json())

# convert the object into a dict
stock_item_batch_inventory_dict = stock_item_batch_inventory_instance.to_dict()
# create an instance of StockItemBatchInventory from a dict
stock_item_batch_inventory_from_dict = StockItemBatchInventory.from_dict(stock_item_batch_inventory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


