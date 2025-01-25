# UpdateWarehouseBinrackBinrackToZoneRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binrack_to_zones** | [**List[WarehouseBinrackToZoneRequestItem]**](WarehouseBinrackToZoneRequestItem.md) | Binrack to zones collection, a BinRackId of zero will assume the Binrack should be removed from the zone. | [optional] 

## Example

```python
from linnworks_api.generated.wms.models.update_warehouse_binrack_binrack_to_zone_request import UpdateWarehouseBinrackBinrackToZoneRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWarehouseBinrackBinrackToZoneRequest from a JSON string
update_warehouse_binrack_binrack_to_zone_request_instance = UpdateWarehouseBinrackBinrackToZoneRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateWarehouseBinrackBinrackToZoneRequest.to_json())

# convert the object into a dict
update_warehouse_binrack_binrack_to_zone_request_dict = update_warehouse_binrack_binrack_to_zone_request_instance.to_dict()
# create an instance of UpdateWarehouseBinrackBinrackToZoneRequest from a dict
update_warehouse_binrack_binrack_to_zone_request_from_dict = UpdateWarehouseBinrackBinrackToZoneRequest.from_dict(update_warehouse_binrack_binrack_to_zone_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


