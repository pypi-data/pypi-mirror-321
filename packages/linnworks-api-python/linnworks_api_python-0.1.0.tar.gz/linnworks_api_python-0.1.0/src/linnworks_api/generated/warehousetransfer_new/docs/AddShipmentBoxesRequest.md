# AddShipmentBoxesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipment_id** | **int** |  | [optional] 
**shipping_plan_id** | **int** |  | [optional] 
**shipment_boxes** | [**List[ShipmentBoxCreateModel]**](ShipmentBoxCreateModel.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.add_shipment_boxes_request import AddShipmentBoxesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddShipmentBoxesRequest from a JSON string
add_shipment_boxes_request_instance = AddShipmentBoxesRequest.from_json(json)
# print the JSON string representation of the object
print(AddShipmentBoxesRequest.to_json())

# convert the object into a dict
add_shipment_boxes_request_dict = add_shipment_boxes_request_instance.to_dict()
# create an instance of AddShipmentBoxesRequest from a dict
add_shipment_boxes_request_from_dict = AddShipmentBoxesRequest.from_dict(add_shipment_boxes_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


