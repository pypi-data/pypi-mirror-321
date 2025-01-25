# GetBinrackZonesByBinrackIdOrNameResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zones** | [**List[WarehouseZone]**](WarehouseZone.md) | Warehouse Zones | [optional] 
**binrack_to_zones** | [**List[WarehouseBinrackToZone]**](WarehouseBinrackToZone.md) | Warehosue binrack to zones. | [optional] 

## Example

```python
from linnworks_api.generated.wms.models.get_binrack_zones_by_binrack_id_or_name_response import GetBinrackZonesByBinrackIdOrNameResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetBinrackZonesByBinrackIdOrNameResponse from a JSON string
get_binrack_zones_by_binrack_id_or_name_response_instance = GetBinrackZonesByBinrackIdOrNameResponse.from_json(json)
# print the JSON string representation of the object
print(GetBinrackZonesByBinrackIdOrNameResponse.to_json())

# convert the object into a dict
get_binrack_zones_by_binrack_id_or_name_response_dict = get_binrack_zones_by_binrack_id_or_name_response_instance.to_dict()
# create an instance of GetBinrackZonesByBinrackIdOrNameResponse from a dict
get_binrack_zones_by_binrack_id_or_name_response_from_dict = GetBinrackZonesByBinrackIdOrNameResponse.from_dict(get_binrack_zones_by_binrack_id_or_name_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


