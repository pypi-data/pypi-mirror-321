# ShipmentCarrierModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipment_carrier_id** | **int** |  | [optional] 
**is_partnered** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**country** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.shipment_carrier_model import ShipmentCarrierModel

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentCarrierModel from a JSON string
shipment_carrier_model_instance = ShipmentCarrierModel.from_json(json)
# print the JSON string representation of the object
print(ShipmentCarrierModel.to_json())

# convert the object into a dict
shipment_carrier_model_dict = shipment_carrier_model_instance.to_dict()
# create an instance of ShipmentCarrierModel from a dict
shipment_carrier_model_from_dict = ShipmentCarrierModel.from_dict(shipment_carrier_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


