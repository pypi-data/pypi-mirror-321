# WarehouseBinRack


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bin_rack_id** | **int** |  | [optional] 
**bin_rack_type_id** | **int** |  | [optional] 
**bin_rack** | **str** |  | [optional] 
**geo_position** | [**GeoPosition**](GeoPosition.md) |  | [optional] 
**dimension** | [**Dimension**](Dimension.md) |  | [optional] 
**routing_sequence** | **int** |  | [optional] 
**max_capacity_volumetric** | **float** |  | [optional] 
**current_full_percentage** | **float** |  | [optional] 
**max_quantity_capacity** | **int** |  | [optional] 
**current_quantity** | **int** |  | [optional] 
**current_volumetric** | **float** |  | [optional] 
**optimal_replenish_full_percentage** | **float** |  | [optional] 
**critical_replenish_full_percentage** | **float** |  | [optional] 
**item_restriction** | **bool** |  | [optional] 
**group_restriction** | **bool** |  | [optional] 
**location_id** | **str** |  | [optional] 
**type_name** | **str** |  | [optional] 
**standard_type** | **int** |  | [optional] 
**is_volumetric** | **bool** |  | [optional] 
**access_orientation** | **str** |  | [optional] 
**storage_groups** | **List[str]** |  | [optional] 
**unique_skus** | **int** |  | [optional] 
**items_info** | [**WarehouseBinRackItemsInfo**](WarehouseBinRackItemsInfo.md) |  | [optional] 
**binrack_type** | [**WarehouseBinRackType**](WarehouseBinRackType.md) |  | [optional] 
**is_valid_for_stock_item** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.warehouse_bin_rack import WarehouseBinRack

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseBinRack from a JSON string
warehouse_bin_rack_instance = WarehouseBinRack.from_json(json)
# print the JSON string representation of the object
print(WarehouseBinRack.to_json())

# convert the object into a dict
warehouse_bin_rack_dict = warehouse_bin_rack_instance.to_dict()
# create an instance of WarehouseBinRack from a dict
warehouse_bin_rack_from_dict = WarehouseBinRack.from_dict(warehouse_bin_rack_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


