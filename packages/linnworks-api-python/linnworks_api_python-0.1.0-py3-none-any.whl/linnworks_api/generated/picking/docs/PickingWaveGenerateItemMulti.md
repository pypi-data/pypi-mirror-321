# PickingWaveGenerateItemMulti


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_item_row_id** | **str** | Order item row id | [optional] 
**batch_inventory_id** | **int** | Batch inventory id, if the item is batched or location is warehouse managed and id is not supplied then the whole order item will be added to the pickwave. | [optional] 

## Example

```python
from linnworks_api.generated.picking.models.picking_wave_generate_item_multi import PickingWaveGenerateItemMulti

# TODO update the JSON string below
json = "{}"
# create an instance of PickingWaveGenerateItemMulti from a JSON string
picking_wave_generate_item_multi_instance = PickingWaveGenerateItemMulti.from_json(json)
# print the JSON string representation of the object
print(PickingWaveGenerateItemMulti.to_json())

# convert the object into a dict
picking_wave_generate_item_multi_dict = picking_wave_generate_item_multi_instance.to_dict()
# create an instance of PickingWaveGenerateItemMulti from a dict
picking_wave_generate_item_multi_from_dict = PickingWaveGenerateItemMulti.from_dict(picking_wave_generate_item_multi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


