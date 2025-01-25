# GetWarehouseMovesByBinrackResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**warehouse_moves** | [**WarehouseMoveCollection**](WarehouseMoveCollection.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.get_warehouse_moves_by_binrack_response import GetWarehouseMovesByBinrackResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetWarehouseMovesByBinrackResponse from a JSON string
get_warehouse_moves_by_binrack_response_instance = GetWarehouseMovesByBinrackResponse.from_json(json)
# print the JSON string representation of the object
print(GetWarehouseMovesByBinrackResponse.to_json())

# convert the object into a dict
get_warehouse_moves_by_binrack_response_dict = get_warehouse_moves_by_binrack_response_instance.to_dict()
# create an instance of GetWarehouseMovesByBinrackResponse from a dict
get_warehouse_moves_by_binrack_response_from_dict = GetWarehouseMovesByBinrackResponse.from_dict(get_warehouse_moves_by_binrack_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


