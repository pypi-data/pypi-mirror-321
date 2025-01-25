# DeleteOrdersFromPickingWavesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_ids** | **List[int]** | List of Linnworks OrderIds | [optional] 

## Example

```python
from linnworks_api.generated.picking.models.delete_orders_from_picking_waves_request import DeleteOrdersFromPickingWavesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteOrdersFromPickingWavesRequest from a JSON string
delete_orders_from_picking_waves_request_instance = DeleteOrdersFromPickingWavesRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteOrdersFromPickingWavesRequest.to_json())

# convert the object into a dict
delete_orders_from_picking_waves_request_dict = delete_orders_from_picking_waves_request_instance.to_dict()
# create an instance of DeleteOrdersFromPickingWavesRequest from a dict
delete_orders_from_picking_waves_request_from_dict = DeleteOrdersFromPickingWavesRequest.from_dict(delete_orders_from_picking_waves_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


