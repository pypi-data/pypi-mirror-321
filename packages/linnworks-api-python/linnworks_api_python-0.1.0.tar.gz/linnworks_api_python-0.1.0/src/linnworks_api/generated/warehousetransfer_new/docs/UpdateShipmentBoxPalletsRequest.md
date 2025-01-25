# UpdateShipmentBoxPalletsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipment_box_pallets** | [**List[UpdateShipmentBoxPalletModel]**](UpdateShipmentBoxPalletModel.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.update_shipment_box_pallets_request import UpdateShipmentBoxPalletsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateShipmentBoxPalletsRequest from a JSON string
update_shipment_box_pallets_request_instance = UpdateShipmentBoxPalletsRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateShipmentBoxPalletsRequest.to_json())

# convert the object into a dict
update_shipment_box_pallets_request_dict = update_shipment_box_pallets_request_instance.to_dict()
# create an instance of UpdateShipmentBoxPalletsRequest from a dict
update_shipment_box_pallets_request_from_dict = UpdateShipmentBoxPalletsRequest.from_dict(update_shipment_box_pallets_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


