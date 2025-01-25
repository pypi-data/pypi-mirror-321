# ShipmentTypeModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.shipment_type_model import ShipmentTypeModel

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentTypeModel from a JSON string
shipment_type_model_instance = ShipmentTypeModel.from_json(json)
# print the JSON string representation of the object
print(ShipmentTypeModel.to_json())

# convert the object into a dict
shipment_type_model_dict = shipment_type_model_instance.to_dict()
# create an instance of ShipmentTypeModel from a dict
shipment_type_model_from_dict = ShipmentTypeModel.from_dict(shipment_type_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


