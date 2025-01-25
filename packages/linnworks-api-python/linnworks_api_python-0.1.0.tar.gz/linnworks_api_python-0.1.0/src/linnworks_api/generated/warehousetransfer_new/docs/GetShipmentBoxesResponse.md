# GetShipmentBoxesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipment_boxes** | [**List[ShipmentBoxModel]**](ShipmentBoxModel.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.get_shipment_boxes_response import GetShipmentBoxesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetShipmentBoxesResponse from a JSON string
get_shipment_boxes_response_instance = GetShipmentBoxesResponse.from_json(json)
# print the JSON string representation of the object
print(GetShipmentBoxesResponse.to_json())

# convert the object into a dict
get_shipment_boxes_response_dict = get_shipment_boxes_response_instance.to_dict()
# create an instance of GetShipmentBoxesResponse from a dict
get_shipment_boxes_response_from_dict = GetShipmentBoxesResponse.from_dict(get_shipment_boxes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


