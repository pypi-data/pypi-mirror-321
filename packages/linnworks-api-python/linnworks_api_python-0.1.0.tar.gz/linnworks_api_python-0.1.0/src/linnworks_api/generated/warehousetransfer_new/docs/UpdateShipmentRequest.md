# UpdateShipmentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**shipment_id** | **str** |  | [optional] 
**ship_to** | **str** |  | [optional] 
**status_id** | **int** |  | 
**who_preps** | [**WhoPreps**](WhoPreps.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.update_shipment_request import UpdateShipmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateShipmentRequest from a JSON string
update_shipment_request_instance = UpdateShipmentRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateShipmentRequest.to_json())

# convert the object into a dict
update_shipment_request_dict = update_shipment_request_instance.to_dict()
# create an instance of UpdateShipmentRequest from a dict
update_shipment_request_from_dict = UpdateShipmentRequest.from_dict(update_shipment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


