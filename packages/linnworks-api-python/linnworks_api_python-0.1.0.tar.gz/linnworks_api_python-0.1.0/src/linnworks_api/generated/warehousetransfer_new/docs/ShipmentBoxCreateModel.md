# ShipmentBoxCreateModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipment_id** | **int** |  | [optional] 
**shipment_pallet_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**height** | **float** |  | [optional] 
**depth** | **float** |  | [optional] 
**width** | **float** |  | [optional] 
**weight** | **float** |  | [optional] 
**weight_unit** | [**ShipmentWeightUnit**](ShipmentWeightUnit.md) |  | [optional] 
**dimension_unit** | [**ShipmentDimensionUnit**](ShipmentDimensionUnit.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.shipment_box_create_model import ShipmentBoxCreateModel

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentBoxCreateModel from a JSON string
shipment_box_create_model_instance = ShipmentBoxCreateModel.from_json(json)
# print the JSON string representation of the object
print(ShipmentBoxCreateModel.to_json())

# convert the object into a dict
shipment_box_create_model_dict = shipment_box_create_model_instance.to_dict()
# create an instance of ShipmentBoxCreateModel from a dict
shipment_box_create_model_from_dict = ShipmentBoxCreateModel.from_dict(shipment_box_create_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


