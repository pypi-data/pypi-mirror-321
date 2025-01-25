# GeneratePickingWaveResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**validation_results** | [**List[PickWaveAllocateCheckResult]**](PickWaveAllocateCheckResult.md) | Validation errors if generate fails. | [optional] 
**picking_waves** | [**List[PickingWaveDetailed]**](PickingWaveDetailed.md) | Pickwaves | [optional] 
**skus** | [**List[StockItemInfo]**](StockItemInfo.md) | List of SKUs. | [optional] 
**bins** | [**List[BinRackStockItem]**](BinRackStockItem.md) | List of bins and batches of items in the bins. | [optional] 

## Example

```python
from linnworks_api.generated.picking.models.generate_picking_wave_response import GeneratePickingWaveResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GeneratePickingWaveResponse from a JSON string
generate_picking_wave_response_instance = GeneratePickingWaveResponse.from_json(json)
# print the JSON string representation of the object
print(GeneratePickingWaveResponse.to_json())

# convert the object into a dict
generate_picking_wave_response_dict = generate_picking_wave_response_instance.to_dict()
# create an instance of GeneratePickingWaveResponse from a dict
generate_picking_wave_response_from_dict = GeneratePickingWaveResponse.from_dict(generate_picking_wave_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


