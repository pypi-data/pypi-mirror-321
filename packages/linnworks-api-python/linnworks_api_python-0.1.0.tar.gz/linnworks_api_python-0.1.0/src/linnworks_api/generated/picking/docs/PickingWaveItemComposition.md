# PickingWaveItemComposition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_item_id** | **str** | Stock item id | [optional] 
**order_item_row_id** | **str** | Composite parent order item row id | [optional] 
**quantity** | **int** | Quantity of composite. | [optional] 
**children** | [**List[PickingWaveItemComposition]**](PickingWaveItemComposition.md) | Child row relationships to parent | [optional] 

## Example

```python
from linnworks_api.generated.picking.models.picking_wave_item_composition import PickingWaveItemComposition

# TODO update the JSON string below
json = "{}"
# create an instance of PickingWaveItemComposition from a JSON string
picking_wave_item_composition_instance = PickingWaveItemComposition.from_json(json)
# print the JSON string representation of the object
print(PickingWaveItemComposition.to_json())

# convert the object into a dict
picking_wave_item_composition_dict = picking_wave_item_composition_instance.to_dict()
# create an instance of PickingWaveItemComposition from a dict
picking_wave_item_composition_from_dict = PickingWaveItemComposition.from_dict(picking_wave_item_composition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


