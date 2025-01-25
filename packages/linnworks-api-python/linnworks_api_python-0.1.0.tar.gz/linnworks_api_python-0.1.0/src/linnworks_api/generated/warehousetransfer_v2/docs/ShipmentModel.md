# ShipmentModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**shipping_plan_id** | **int** |  | [optional] 
**amazon_shipment_id** | **str** |  | [optional] 
**warehouse_address** | **str** |  | [optional] 
**status** | [**ShipmentStatus**](ShipmentStatus.md) |  | [optional] 
**update_date** | **datetime** |  | [optional] 
**create_date** | **datetime** |  | [optional] 
**items** | [**List[ShipmentItemModel]**](ShipmentItemModel.md) |  | [optional] 
**contact_name** | **str** |  | [optional] 
**contact_email** | **str** |  | [optional] 
**contact_phone_number** | **str** |  | [optional] 
**ready_to_ship_window** | **datetime** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_v2.models.shipment_model import ShipmentModel

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentModel from a JSON string
shipment_model_instance = ShipmentModel.from_json(json)
# print the JSON string representation of the object
print(ShipmentModel.to_json())

# convert the object into a dict
shipment_model_dict = shipment_model_instance.to_dict()
# create an instance of ShipmentModel from a dict
shipment_model_from_dict = ShipmentModel.from_dict(shipment_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


