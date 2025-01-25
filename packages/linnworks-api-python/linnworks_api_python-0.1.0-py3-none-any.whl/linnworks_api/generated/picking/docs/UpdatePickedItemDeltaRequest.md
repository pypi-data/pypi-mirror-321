# UpdatePickedItemDeltaRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deltas** | [**List[UpdatePickedItemDeltaRequestItem]**](UpdatePickedItemDeltaRequestItem.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.picking.models.update_picked_item_delta_request import UpdatePickedItemDeltaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePickedItemDeltaRequest from a JSON string
update_picked_item_delta_request_instance = UpdatePickedItemDeltaRequest.from_json(json)
# print the JSON string representation of the object
print(UpdatePickedItemDeltaRequest.to_json())

# convert the object into a dict
update_picked_item_delta_request_dict = update_picked_item_delta_request_instance.to_dict()
# create an instance of UpdatePickedItemDeltaRequest from a dict
update_picked_item_delta_request_from_dict = UpdatePickedItemDeltaRequest.from_dict(update_picked_item_delta_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


