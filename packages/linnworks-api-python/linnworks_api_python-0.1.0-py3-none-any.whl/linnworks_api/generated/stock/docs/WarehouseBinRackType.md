# WarehouseBinRackType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bin_rack_type_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**standard_type** | **int** |  | [optional] 
**location_bound** | **str** |  | [optional] 
**is_volumetric** | **bool** |  | [optional] 
**default_batch_status** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.warehouse_bin_rack_type import WarehouseBinRackType

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseBinRackType from a JSON string
warehouse_bin_rack_type_instance = WarehouseBinRackType.from_json(json)
# print the JSON string representation of the object
print(WarehouseBinRackType.to_json())

# convert the object into a dict
warehouse_bin_rack_type_dict = warehouse_bin_rack_type_instance.to_dict()
# create an instance of WarehouseBinRackType from a dict
warehouse_bin_rack_type_from_dict = WarehouseBinRackType.from_dict(warehouse_bin_rack_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


