# DeleteOrdersFromPickingWavesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**processed_order_ids** | **List[int]** | Order Ids that had pickwaves deleted from them | [optional] 
**no_pickwaves** | **List[int]** | OrderIds where there was no pickwave found against them | [optional] 

## Example

```python
from linnworks_api.generated.picking.models.delete_orders_from_picking_waves_response import DeleteOrdersFromPickingWavesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteOrdersFromPickingWavesResponse from a JSON string
delete_orders_from_picking_waves_response_instance = DeleteOrdersFromPickingWavesResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteOrdersFromPickingWavesResponse.to_json())

# convert the object into a dict
delete_orders_from_picking_waves_response_dict = delete_orders_from_picking_waves_response_instance.to_dict()
# create an instance of DeleteOrdersFromPickingWavesResponse from a dict
delete_orders_from_picking_waves_response_from_dict = DeleteOrdersFromPickingWavesResponse.from_dict(delete_orders_from_picking_waves_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


