# InventoryView


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**mode** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**sub_source** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**country_name** | **str** |  | [optional] 
**listing** | **str** |  | [optional] 
**show_only_changed** | **bool** |  | [optional] 
**include_products** | **str** |  | [optional] 
**filters** | [**List[Filter]**](Filter.md) |  | [optional] 
**columns** | [**List[Column]**](Column.md) |  | [optional] 
**channels** | [**List[InventoryChannel]**](InventoryChannel.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_view import InventoryView

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryView from a JSON string
inventory_view_instance = InventoryView.from_json(json)
# print the JSON string representation of the object
print(InventoryView.to_json())

# convert the object into a dict
inventory_view_dict = inventory_view_instance.to_dict()
# create an instance of InventoryView from a dict
inventory_view_from_dict = InventoryView.from_dict(inventory_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


