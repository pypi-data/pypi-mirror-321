# UpdateShipmentBoxPalletModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipment_box_id** | **int** |  | [optional] 
**shipment_pallet_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.update_shipment_box_pallet_model import UpdateShipmentBoxPalletModel

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateShipmentBoxPalletModel from a JSON string
update_shipment_box_pallet_model_instance = UpdateShipmentBoxPalletModel.from_json(json)
# print the JSON string representation of the object
print(UpdateShipmentBoxPalletModel.to_json())

# convert the object into a dict
update_shipment_box_pallet_model_dict = update_shipment_box_pallet_model_instance.to_dict()
# create an instance of UpdateShipmentBoxPalletModel from a dict
update_shipment_box_pallet_model_from_dict = UpdateShipmentBoxPalletModel.from_dict(update_shipment_box_pallet_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


