# ShipmentPalletUpdateModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipment_pallet_id** | **int** |  | [optional] 
**shipment_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**height** | **float** |  | [optional] 
**depth** | **float** |  | [optional] 
**width** | **float** |  | [optional] 
**weight** | **float** |  | [optional] 
**is_stacked** | **bool** |  | [optional] 
**weight_unit** | [**ShipmentWeightUnit**](ShipmentWeightUnit.md) |  | [optional] 
**dimension_unit** | [**ShipmentDimensionUnit**](ShipmentDimensionUnit.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.shipment_pallet_update_model import ShipmentPalletUpdateModel

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentPalletUpdateModel from a JSON string
shipment_pallet_update_model_instance = ShipmentPalletUpdateModel.from_json(json)
# print the JSON string representation of the object
print(ShipmentPalletUpdateModel.to_json())

# convert the object into a dict
shipment_pallet_update_model_dict = shipment_pallet_update_model_instance.to_dict()
# create an instance of ShipmentPalletUpdateModel from a dict
shipment_pallet_update_model_from_dict = ShipmentPalletUpdateModel.from_dict(shipment_pallet_update_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


