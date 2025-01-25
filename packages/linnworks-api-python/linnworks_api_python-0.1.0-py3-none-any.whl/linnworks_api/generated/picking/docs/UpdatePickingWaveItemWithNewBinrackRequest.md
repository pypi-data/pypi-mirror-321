# UpdatePickingWaveItemWithNewBinrackRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**picking_wave_id** | **int** | Pickwave id | [optional] 
**picking_wave_item_row_ids** | **List[int]** | List of pickwave item row ids to replace with the new location | [optional] 
**new_batch_inventory_id** | **int** | The new batch inventory to pick | [optional] 
**sort_type** | **str** | Dictates how the returned pickwave should be sorted | [optional] 

## Example

```python
from linnworks_api.generated.picking.models.update_picking_wave_item_with_new_binrack_request import UpdatePickingWaveItemWithNewBinrackRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePickingWaveItemWithNewBinrackRequest from a JSON string
update_picking_wave_item_with_new_binrack_request_instance = UpdatePickingWaveItemWithNewBinrackRequest.from_json(json)
# print the JSON string representation of the object
print(UpdatePickingWaveItemWithNewBinrackRequest.to_json())

# convert the object into a dict
update_picking_wave_item_with_new_binrack_request_dict = update_picking_wave_item_with_new_binrack_request_instance.to_dict()
# create an instance of UpdatePickingWaveItemWithNewBinrackRequest from a dict
update_picking_wave_item_with_new_binrack_request_from_dict = UpdatePickingWaveItemWithNewBinrackRequest.from_dict(update_picking_wave_item_with_new_binrack_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


