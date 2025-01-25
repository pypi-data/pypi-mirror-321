# PickWaveAllocateCheckResultOrderDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_id** | **str** |  | [optional] 
**order_item_row_id** | **str** |  | [optional] 
**batch_inventory_id** | **int** |  | [optional] 
**stock_item_id** | **str** |  | [optional] 
**sku** | **str** |  | [optional] 
**item_title** | **str** |  | [optional] 
**binrack** | **str** |  | [optional] 
**batch_number** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**routing_sequence** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.picking.models.pick_wave_allocate_check_result_order_details import PickWaveAllocateCheckResultOrderDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PickWaveAllocateCheckResultOrderDetails from a JSON string
pick_wave_allocate_check_result_order_details_instance = PickWaveAllocateCheckResultOrderDetails.from_json(json)
# print the JSON string representation of the object
print(PickWaveAllocateCheckResultOrderDetails.to_json())

# convert the object into a dict
pick_wave_allocate_check_result_order_details_dict = pick_wave_allocate_check_result_order_details_instance.to_dict()
# create an instance of PickWaveAllocateCheckResultOrderDetails from a dict
pick_wave_allocate_check_result_order_details_from_dict = PickWaveAllocateCheckResultOrderDetails.from_dict(pick_wave_allocate_check_result_order_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


