# GetWarehouseMoveRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**move_id** | **int** | Id of the stock move | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.get_warehouse_move_request import GetWarehouseMoveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetWarehouseMoveRequest from a JSON string
get_warehouse_move_request_instance = GetWarehouseMoveRequest.from_json(json)
# print the JSON string representation of the object
print(GetWarehouseMoveRequest.to_json())

# convert the object into a dict
get_warehouse_move_request_dict = get_warehouse_move_request_instance.to_dict()
# create an instance of GetWarehouseMoveRequest from a dict
get_warehouse_move_request_from_dict = GetWarehouseMoveRequest.from_dict(get_warehouse_move_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


