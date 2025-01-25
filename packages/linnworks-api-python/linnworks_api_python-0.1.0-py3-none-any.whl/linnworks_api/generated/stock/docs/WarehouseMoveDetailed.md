# WarehouseMoveDetailed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binrack_from** | [**WarehouseBinRack**](WarehouseBinRack.md) |  | [optional] 
**binrack_destination** | [**WarehouseBinRack**](WarehouseBinRack.md) |  | [optional] 
**batch** | [**StockItemBatch**](StockItemBatch.md) |  | [optional] 
**move_id** | **int** |  | [optional] 
**batch_inventory_id** | **int** |  | [optional] 
**quantity** | **int** |  | [optional] 
**user_id** | **str** |  | [optional] 
**user_name** | **str** |  | [optional] 
**binrack_id_from** | **int** |  | [optional] 
**binrack_id_destination** | **int** |  | [optional] 
**tx_type** | **str** |  | [optional] 
**job_id** | **int** |  | [optional] 
**create_date** | **datetime** |  | [optional] 
**batch_id** | **int** |  | [optional] 
**stock_location_id** | **str** |  | [optional] 
**tot_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.warehouse_move_detailed import WarehouseMoveDetailed

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseMoveDetailed from a JSON string
warehouse_move_detailed_instance = WarehouseMoveDetailed.from_json(json)
# print the JSON string representation of the object
print(WarehouseMoveDetailed.to_json())

# convert the object into a dict
warehouse_move_detailed_dict = warehouse_move_detailed_instance.to_dict()
# create an instance of WarehouseMoveDetailed from a dict
warehouse_move_detailed_from_dict = WarehouseMoveDetailed.from_dict(warehouse_move_detailed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


