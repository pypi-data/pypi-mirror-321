# ApproveShipmentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipment_id** | **int** |  | [optional] 
**status_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.approve_shipment_response import ApproveShipmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApproveShipmentResponse from a JSON string
approve_shipment_response_instance = ApproveShipmentResponse.from_json(json)
# print the JSON string representation of the object
print(ApproveShipmentResponse.to_json())

# convert the object into a dict
approve_shipment_response_dict = approve_shipment_response_instance.to_dict()
# create an instance of ApproveShipmentResponse from a dict
approve_shipment_response_from_dict = ApproveShipmentResponse.from_dict(approve_shipment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


