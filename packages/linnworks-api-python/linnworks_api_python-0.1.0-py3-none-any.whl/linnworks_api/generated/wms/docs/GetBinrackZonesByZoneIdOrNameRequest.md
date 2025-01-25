# GetBinrackZonesByZoneIdOrNameRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_location_int_id** | **int** |  | [optional] 
**zone_names** | **List[str]** |  | [optional] 
**zone_ids** | **List[int]** |  | [optional] 

## Example

```python
from linnworks_api.generated.wms.models.get_binrack_zones_by_zone_id_or_name_request import GetBinrackZonesByZoneIdOrNameRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetBinrackZonesByZoneIdOrNameRequest from a JSON string
get_binrack_zones_by_zone_id_or_name_request_instance = GetBinrackZonesByZoneIdOrNameRequest.from_json(json)
# print the JSON string representation of the object
print(GetBinrackZonesByZoneIdOrNameRequest.to_json())

# convert the object into a dict
get_binrack_zones_by_zone_id_or_name_request_dict = get_binrack_zones_by_zone_id_or_name_request_instance.to_dict()
# create an instance of GetBinrackZonesByZoneIdOrNameRequest from a dict
get_binrack_zones_by_zone_id_or_name_request_from_dict = GetBinrackZonesByZoneIdOrNameRequest.from_dict(get_binrack_zones_by_zone_id_or_name_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


