# InventoryChannel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | [optional] 
**sub_source** | **str** |  | [optional] 
**source_version** | **str** |  | [optional] 
**source_type** | **str** |  | [optional] 
**width** | **float** |  | [optional] 
**channel_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_channel import InventoryChannel

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryChannel from a JSON string
inventory_channel_instance = InventoryChannel.from_json(json)
# print the JSON string representation of the object
print(InventoryChannel.to_json())

# convert the object into a dict
inventory_channel_dict = inventory_channel_instance.to_dict()
# create an instance of InventoryChannel from a dict
inventory_channel_from_dict = InventoryChannel.from_dict(inventory_channel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


