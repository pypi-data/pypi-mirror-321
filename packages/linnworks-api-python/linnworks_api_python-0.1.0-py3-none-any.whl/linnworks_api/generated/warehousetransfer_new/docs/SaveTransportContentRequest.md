# SaveTransportContentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pro_number** | **str** |  | [optional] 
**shipping_method** | **int** |  | [optional] 
**shipping_carrier_type** | **int** |  | [optional] 
**carrier_id** | **int** |  | [optional] 
**contact_person** | [**TransportationContact**](TransportationContact.md) |  | [optional] 
**seller_freight_class_id** | **int** |  | [optional] 
**freight_ready_date** | **datetime** |  | [optional] 
**send_pallets** | **bool** |  | [optional] 
**pallet_is_stacked** | **bool** |  | [optional] 
**total_shipment_weight** | **int** |  | [optional] 
**seller_declared_value** | **int** |  | [optional] 
**seller_declared_currency** | **str** |  | [optional] 
**tracking_numbers** | [**List[BoxTrackingNumber]**](BoxTrackingNumber.md) |  | [optional] 
**shipment_id** | **int** |  | [optional] 
**transportation_status** | [**ShipmentTransportationStatus**](ShipmentTransportationStatus.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.save_transport_content_request import SaveTransportContentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SaveTransportContentRequest from a JSON string
save_transport_content_request_instance = SaveTransportContentRequest.from_json(json)
# print the JSON string representation of the object
print(SaveTransportContentRequest.to_json())

# convert the object into a dict
save_transport_content_request_dict = save_transport_content_request_instance.to_dict()
# create an instance of SaveTransportContentRequest from a dict
save_transport_content_request_from_dict = SaveTransportContentRequest.from_dict(save_transport_content_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


