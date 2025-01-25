# GetWarehouseMoveResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**warehouse_move** | [**WarehouseMoveDetailed**](WarehouseMoveDetailed.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.get_warehouse_move_response import GetWarehouseMoveResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetWarehouseMoveResponse from a JSON string
get_warehouse_move_response_instance = GetWarehouseMoveResponse.from_json(json)
# print the JSON string representation of the object
print(GetWarehouseMoveResponse.to_json())

# convert the object into a dict
get_warehouse_move_response_dict = get_warehouse_move_response_instance.to_dict()
# create an instance of GetWarehouseMoveResponse from a dict
get_warehouse_move_response_from_dict = GetWarehouseMoveResponse.from_dict(get_warehouse_move_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


