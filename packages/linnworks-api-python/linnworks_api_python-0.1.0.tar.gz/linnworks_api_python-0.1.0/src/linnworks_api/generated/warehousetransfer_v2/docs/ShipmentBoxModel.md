# ShipmentBoxModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipment_box_id** | **int** |  | [optional] 
**shipment_id** | **int** |  | [optional] 
**packing_group_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**height** | **float** |  | [optional] 
**length** | **float** |  | [optional] 
**width** | **float** |  | [optional] 
**shipment_measurement_unit** | [**UnitOfMeasurement**](UnitOfMeasurement.md) |  | [optional] 
**weight** | **float** |  | [optional] 
**shipment_weight_unit** | [**UnitOfWeight**](UnitOfWeight.md) |  | [optional] 
**quantity** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_v2.models.shipment_box_model import ShipmentBoxModel

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentBoxModel from a JSON string
shipment_box_model_instance = ShipmentBoxModel.from_json(json)
# print the JSON string representation of the object
print(ShipmentBoxModel.to_json())

# convert the object into a dict
shipment_box_model_dict = shipment_box_model_instance.to_dict()
# create an instance of ShipmentBoxModel from a dict
shipment_box_model_from_dict = ShipmentBoxModel.from_dict(shipment_box_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


