# GetBinrackZonesByBinrackIdOrNameRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binrack_ids** | **List[int]** | Binrack Ids, StockLocationIntId optional, if different to supplied binrack ids, zones will still be returned. | [optional] 
**binrack_names** | **List[str]** | Binrack names, StockLocationIntId required. | [optional] 
**stock_location_int_id** | **int** | Stock Location interger id. | [optional] 

## Example

```python
from linnworks_api.generated.wms.models.get_binrack_zones_by_binrack_id_or_name_request import GetBinrackZonesByBinrackIdOrNameRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetBinrackZonesByBinrackIdOrNameRequest from a JSON string
get_binrack_zones_by_binrack_id_or_name_request_instance = GetBinrackZonesByBinrackIdOrNameRequest.from_json(json)
# print the JSON string representation of the object
print(GetBinrackZonesByBinrackIdOrNameRequest.to_json())

# convert the object into a dict
get_binrack_zones_by_binrack_id_or_name_request_dict = get_binrack_zones_by_binrack_id_or_name_request_instance.to_dict()
# create an instance of GetBinrackZonesByBinrackIdOrNameRequest from a dict
get_binrack_zones_by_binrack_id_or_name_request_from_dict = GetBinrackZonesByBinrackIdOrNameRequest.from_dict(get_binrack_zones_by_binrack_id_or_name_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


