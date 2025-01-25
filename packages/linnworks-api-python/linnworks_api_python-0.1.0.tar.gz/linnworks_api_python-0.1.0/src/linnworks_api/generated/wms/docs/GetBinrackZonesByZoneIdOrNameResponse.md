# GetBinrackZonesByZoneIdOrNameResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**warehouse_zones** | [**List[WarehouseZone]**](WarehouseZone.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.wms.models.get_binrack_zones_by_zone_id_or_name_response import GetBinrackZonesByZoneIdOrNameResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetBinrackZonesByZoneIdOrNameResponse from a JSON string
get_binrack_zones_by_zone_id_or_name_response_instance = GetBinrackZonesByZoneIdOrNameResponse.from_json(json)
# print the JSON string representation of the object
print(GetBinrackZonesByZoneIdOrNameResponse.to_json())

# convert the object into a dict
get_binrack_zones_by_zone_id_or_name_response_dict = get_binrack_zones_by_zone_id_or_name_response_instance.to_dict()
# create an instance of GetBinrackZonesByZoneIdOrNameResponse from a dict
get_binrack_zones_by_zone_id_or_name_response_from_dict = GetBinrackZonesByZoneIdOrNameResponse.from_dict(get_binrack_zones_by_zone_id_or_name_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


