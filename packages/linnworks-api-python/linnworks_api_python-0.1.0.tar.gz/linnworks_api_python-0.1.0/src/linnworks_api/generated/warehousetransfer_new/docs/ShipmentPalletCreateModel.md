# ShipmentPalletCreateModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipment_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**height** | **float** |  | [optional] 
**depth** | **float** |  | [optional] 
**width** | **float** |  | [optional] 
**weight** | **float** |  | [optional] 
**weight_unit** | [**ShipmentWeightUnit**](ShipmentWeightUnit.md) |  | [optional] 
**dimension_unit** | [**ShipmentDimensionUnit**](ShipmentDimensionUnit.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.shipment_pallet_create_model import ShipmentPalletCreateModel

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentPalletCreateModel from a JSON string
shipment_pallet_create_model_instance = ShipmentPalletCreateModel.from_json(json)
# print the JSON string representation of the object
print(ShipmentPalletCreateModel.to_json())

# convert the object into a dict
shipment_pallet_create_model_dict = shipment_pallet_create_model_instance.to_dict()
# create an instance of ShipmentPalletCreateModel from a dict
shipment_pallet_create_model_from_dict = ShipmentPalletCreateModel.from_dict(shipment_pallet_create_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


