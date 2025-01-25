# GetWarehouseMovesByBinrackRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binrack_id** | **int** | The Id of the binrack to get stock moves for | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.get_warehouse_moves_by_binrack_request import GetWarehouseMovesByBinrackRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetWarehouseMovesByBinrackRequest from a JSON string
get_warehouse_moves_by_binrack_request_instance = GetWarehouseMovesByBinrackRequest.from_json(json)
# print the JSON string representation of the object
print(GetWarehouseMovesByBinrackRequest.to_json())

# convert the object into a dict
get_warehouse_moves_by_binrack_request_dict = get_warehouse_moves_by_binrack_request_instance.to_dict()
# create an instance of GetWarehouseMovesByBinrackRequest from a dict
get_warehouse_moves_by_binrack_request_from_dict = GetWarehouseMovesByBinrackRequest.from_dict(get_warehouse_moves_by_binrack_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


