# UpdateShipmentBoxModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipment_box_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**height** | **float** |  | [optional] 
**length** | **float** |  | [optional] 
**width** | **float** |  | [optional] 
**weight** | **float** |  | [optional] 
**weight_unit** | [**UnitOfWeight**](UnitOfWeight.md) |  | [optional] 
**measurement_unit** | [**UnitOfMeasurement**](UnitOfMeasurement.md) |  | [optional] 
**quantity** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_v2.models.update_shipment_box_model import UpdateShipmentBoxModel

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateShipmentBoxModel from a JSON string
update_shipment_box_model_instance = UpdateShipmentBoxModel.from_json(json)
# print the JSON string representation of the object
print(UpdateShipmentBoxModel.to_json())

# convert the object into a dict
update_shipment_box_model_dict = update_shipment_box_model_instance.to_dict()
# create an instance of UpdateShipmentBoxModel from a dict
update_shipment_box_model_from_dict = UpdateShipmentBoxModel.from_dict(update_shipment_box_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


