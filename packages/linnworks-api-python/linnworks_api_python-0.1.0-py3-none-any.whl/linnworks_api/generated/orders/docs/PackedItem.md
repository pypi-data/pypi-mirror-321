# PackedItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**pk_stock_item_id** | **str** |  | [optional] 
**sku** | **str** |  | [optional] 
**width** | **float** |  | [optional] 
**height** | **float** |  | [optional] 
**depth** | **float** |  | [optional] 
**weight** | **float** |  | [optional] 
**x** | **float** |  | [optional] 
**y** | **float** |  | [optional] 
**z** | **float** |  | [optional] 
**layer** | **int** |  | [optional] 
**faces** | [**List[Face]**](Face.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.packed_item import PackedItem

# TODO update the JSON string below
json = "{}"
# create an instance of PackedItem from a JSON string
packed_item_instance = PackedItem.from_json(json)
# print the JSON string representation of the object
print(PackedItem.to_json())

# convert the object into a dict
packed_item_dict = packed_item_instance.to_dict()
# create an instance of PackedItem from a dict
packed_item_from_dict = PackedItem.from_dict(packed_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


