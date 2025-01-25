# WarehouseBinrackToZoneRequestItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**row_index** | **int** |  | [optional] 
**zone_id** | **int** |  | [optional] 
**binrack_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.wms.models.warehouse_binrack_to_zone_request_item import WarehouseBinrackToZoneRequestItem

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseBinrackToZoneRequestItem from a JSON string
warehouse_binrack_to_zone_request_item_instance = WarehouseBinrackToZoneRequestItem.from_json(json)
# print the JSON string representation of the object
print(WarehouseBinrackToZoneRequestItem.to_json())

# convert the object into a dict
warehouse_binrack_to_zone_request_item_dict = warehouse_binrack_to_zone_request_item_instance.to_dict()
# create an instance of WarehouseBinrackToZoneRequestItem from a dict
warehouse_binrack_to_zone_request_item_from_dict = WarehouseBinrackToZoneRequestItem.from_dict(warehouse_binrack_to_zone_request_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


