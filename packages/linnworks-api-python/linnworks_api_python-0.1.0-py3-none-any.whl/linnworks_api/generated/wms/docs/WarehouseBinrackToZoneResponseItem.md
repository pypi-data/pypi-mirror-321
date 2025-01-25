# WarehouseBinrackToZoneResponseItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **List[str]** |  | [optional] 
**row_index** | **int** |  | [optional] 
**zone_id** | **int** |  | [optional] 
**binrack_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.wms.models.warehouse_binrack_to_zone_response_item import WarehouseBinrackToZoneResponseItem

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseBinrackToZoneResponseItem from a JSON string
warehouse_binrack_to_zone_response_item_instance = WarehouseBinrackToZoneResponseItem.from_json(json)
# print the JSON string representation of the object
print(WarehouseBinrackToZoneResponseItem.to_json())

# convert the object into a dict
warehouse_binrack_to_zone_response_item_dict = warehouse_binrack_to_zone_response_item_instance.to_dict()
# create an instance of WarehouseBinrackToZoneResponseItem from a dict
warehouse_binrack_to_zone_response_item_from_dict = WarehouseBinrackToZoneResponseItem.from_dict(warehouse_binrack_to_zone_response_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


