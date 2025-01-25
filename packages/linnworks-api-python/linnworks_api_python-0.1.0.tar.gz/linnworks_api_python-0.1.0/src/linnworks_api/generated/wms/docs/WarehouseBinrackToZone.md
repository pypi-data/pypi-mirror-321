# WarehouseBinrackToZone


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zone_id** | **int** |  | [optional] 
**binrack_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.wms.models.warehouse_binrack_to_zone import WarehouseBinrackToZone

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseBinrackToZone from a JSON string
warehouse_binrack_to_zone_instance = WarehouseBinrackToZone.from_json(json)
# print the JSON string representation of the object
print(WarehouseBinrackToZone.to_json())

# convert the object into a dict
warehouse_binrack_to_zone_dict = warehouse_binrack_to_zone_instance.to_dict()
# create an instance of WarehouseBinrackToZone from a dict
warehouse_binrack_to_zone_from_dict = WarehouseBinrackToZone.from_dict(warehouse_binrack_to_zone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


