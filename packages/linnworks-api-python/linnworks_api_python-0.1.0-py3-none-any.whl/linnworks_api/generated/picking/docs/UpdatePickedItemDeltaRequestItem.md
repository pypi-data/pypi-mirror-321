# UpdatePickedItemDeltaRequestItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**picking_wave_items_row_id** | **int** | Picking wave row id | [optional] 
**tote_id** | **int** | Tote id | [optional] 
**tray_tag** | **str** | Tray tag (optional) | [optional] 
**picked_quantity_delta** | **int** | Picked quantity delta | [optional] 

## Example

```python
from linnworks_api.generated.picking.models.update_picked_item_delta_request_item import UpdatePickedItemDeltaRequestItem

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePickedItemDeltaRequestItem from a JSON string
update_picked_item_delta_request_item_instance = UpdatePickedItemDeltaRequestItem.from_json(json)
# print the JSON string representation of the object
print(UpdatePickedItemDeltaRequestItem.to_json())

# convert the object into a dict
update_picked_item_delta_request_item_dict = update_picked_item_delta_request_item_instance.to_dict()
# create an instance of UpdatePickedItemDeltaRequestItem from a dict
update_picked_item_delta_request_item_from_dict = UpdatePickedItemDeltaRequestItem.from_dict(update_picked_item_delta_request_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


