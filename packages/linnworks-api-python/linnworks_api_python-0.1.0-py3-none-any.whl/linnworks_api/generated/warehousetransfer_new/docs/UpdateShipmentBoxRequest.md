# UpdateShipmentBoxRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipment_id** | **int** |  | 
**shipping_plan_id** | **int** |  | 
**shipment_boxes** | [**List[ShipmentBoxUpdateModel]**](ShipmentBoxUpdateModel.md) |  | 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.update_shipment_box_request import UpdateShipmentBoxRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateShipmentBoxRequest from a JSON string
update_shipment_box_request_instance = UpdateShipmentBoxRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateShipmentBoxRequest.to_json())

# convert the object into a dict
update_shipment_box_request_dict = update_shipment_box_request_instance.to_dict()
# create an instance of UpdateShipmentBoxRequest from a dict
update_shipment_box_request_from_dict = UpdateShipmentBoxRequest.from_dict(update_shipment_box_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


