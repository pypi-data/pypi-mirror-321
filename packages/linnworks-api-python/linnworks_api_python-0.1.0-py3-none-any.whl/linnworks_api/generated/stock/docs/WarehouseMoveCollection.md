# WarehouseMoveCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**incoming** | [**List[WarehouseMoveDetailed]**](WarehouseMoveDetailed.md) |  | [optional] 
**outgoing** | [**List[WarehouseMoveDetailed]**](WarehouseMoveDetailed.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.warehouse_move_collection import WarehouseMoveCollection

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseMoveCollection from a JSON string
warehouse_move_collection_instance = WarehouseMoveCollection.from_json(json)
# print the JSON string representation of the object
print(WarehouseMoveCollection.to_json())

# convert the object into a dict
warehouse_move_collection_dict = warehouse_move_collection_instance.to_dict()
# create an instance of WarehouseMoveCollection from a dict
warehouse_move_collection_from_dict = WarehouseMoveCollection.from_dict(warehouse_move_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


