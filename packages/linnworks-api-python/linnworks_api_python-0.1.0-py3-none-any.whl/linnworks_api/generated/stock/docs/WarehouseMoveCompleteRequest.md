# WarehouseMoveCompleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**move_id** | **int** |  | [optional] 
**final_binrack_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.warehouse_move_complete_request import WarehouseMoveCompleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseMoveCompleteRequest from a JSON string
warehouse_move_complete_request_instance = WarehouseMoveCompleteRequest.from_json(json)
# print the JSON string representation of the object
print(WarehouseMoveCompleteRequest.to_json())

# convert the object into a dict
warehouse_move_complete_request_dict = warehouse_move_complete_request_instance.to_dict()
# create an instance of WarehouseMoveCompleteRequest from a dict
warehouse_move_complete_request_from_dict = WarehouseMoveCompleteRequest.from_dict(warehouse_move_complete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


