# ShipmentSellerFreightModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipment_seller_freight_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.shipment_seller_freight_model import ShipmentSellerFreightModel

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentSellerFreightModel from a JSON string
shipment_seller_freight_model_instance = ShipmentSellerFreightModel.from_json(json)
# print the JSON string representation of the object
print(ShipmentSellerFreightModel.to_json())

# convert the object into a dict
shipment_seller_freight_model_dict = shipment_seller_freight_model_instance.to_dict()
# create an instance of ShipmentSellerFreightModel from a dict
shipment_seller_freight_model_from_dict = ShipmentSellerFreightModel.from_dict(shipment_seller_freight_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


