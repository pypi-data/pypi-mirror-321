# UpdateShipmentPalletRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipment_id** | **int** |  | [optional] 
**shipping_plan_id** | **int** |  | [optional] 
**shipment_pallets** | [**List[ShipmentPalletUpdateModel]**](ShipmentPalletUpdateModel.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.update_shipment_pallet_request import UpdateShipmentPalletRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateShipmentPalletRequest from a JSON string
update_shipment_pallet_request_instance = UpdateShipmentPalletRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateShipmentPalletRequest.to_json())

# convert the object into a dict
update_shipment_pallet_request_dict = update_shipment_pallet_request_instance.to_dict()
# create an instance of UpdateShipmentPalletRequest from a dict
update_shipment_pallet_request_from_dict = UpdateShipmentPalletRequest.from_dict(update_shipment_pallet_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


