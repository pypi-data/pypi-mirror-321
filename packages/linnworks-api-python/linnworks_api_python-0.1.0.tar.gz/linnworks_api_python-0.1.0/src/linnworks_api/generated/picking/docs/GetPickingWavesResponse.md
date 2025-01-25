# GetPickingWavesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**picking_waves** | [**List[PickingWaveDetailed]**](PickingWaveDetailed.md) | Pickwaves | [optional] 
**skus** | [**List[StockItemInfo]**](StockItemInfo.md) | List of SKUs. | [optional] 
**bins** | [**List[BinRackStockItem]**](BinRackStockItem.md) | List of bins and batches of items in the bins. | [optional] 

## Example

```python
from linnworks_api.generated.picking.models.get_picking_waves_response import GetPickingWavesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetPickingWavesResponse from a JSON string
get_picking_waves_response_instance = GetPickingWavesResponse.from_json(json)
# print the JSON string representation of the object
print(GetPickingWavesResponse.to_json())

# convert the object into a dict
get_picking_waves_response_dict = get_picking_waves_response_instance.to_dict()
# create an instance of GetPickingWavesResponse from a dict
get_picking_waves_response_from_dict = GetPickingWavesResponse.from_dict(get_picking_waves_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


