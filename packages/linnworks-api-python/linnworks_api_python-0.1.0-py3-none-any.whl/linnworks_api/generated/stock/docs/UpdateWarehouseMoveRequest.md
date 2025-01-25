# UpdateWarehouseMoveRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**move_id** | **int** | The Id of the stock move to update | [optional] 
**batch_inventory_id** | **int** | Batch Inventory Id of the stock item you are moving | [optional] 
**quantity** | **int** | Quantity of items being moved | [optional] 
**binrack_id_destination** | **int** | Destination if known, can be null | [optional] 
**job_id** | **int** | If the move is part of a specific job, specify job id so it can be marked off from the job | [optional] 
**tot_id** | **int** | (Optional) Move to TOT id, create or retrive tot scan barcode first. To unassign from Tot send 0 | [optional] 
**tx_type** | **str** | Type of the move. Open means its an instruction to move, In Transit actually marks the item as unavilable and physically being moved | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.update_warehouse_move_request import UpdateWarehouseMoveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWarehouseMoveRequest from a JSON string
update_warehouse_move_request_instance = UpdateWarehouseMoveRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateWarehouseMoveRequest.to_json())

# convert the object into a dict
update_warehouse_move_request_dict = update_warehouse_move_request_instance.to_dict()
# create an instance of UpdateWarehouseMoveRequest from a dict
update_warehouse_move_request_from_dict = UpdateWarehouseMoveRequest.from_dict(update_warehouse_move_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


