# GetTransportDetailResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipment_id** | **int** |  | [optional] 
**shipment_carrier_id** | **int** |  | [optional] 
**shipment_type** | [**AmazonShipmentType**](AmazonShipmentType.md) |  | [optional] 
**transportation_status** | [**ShipmentTransportationStatus**](ShipmentTransportationStatus.md) |  | [optional] 
**shipment_seller_freight_id** | **int** |  | [optional] 
**contact_name** | **str** |  | [optional] 
**contact_phone** | **str** |  | [optional] 
**contact_email** | **str** |  | [optional] 
**contact_fax** | **str** |  | [optional] 
**seller_freight_date** | **datetime** |  | [optional] 
**pro_number** | **str** |  | [optional] 
**seller_declared_currency** | **str** |  | [optional] 
**seller_declared_value** | **float** |  | [optional] 
**partnered_estimated_currency_code** | **str** |  | [optional] 
**partnered_estimated_value** | **float** |  | [optional] 
**partnered_estimated_confirm_deadline** | **datetime** |  | [optional] 
**partnered_estimated_void_deadline** | **datetime** |  | [optional] 
**site_code** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.get_transport_detail_response import GetTransportDetailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransportDetailResponse from a JSON string
get_transport_detail_response_instance = GetTransportDetailResponse.from_json(json)
# print the JSON string representation of the object
print(GetTransportDetailResponse.to_json())

# convert the object into a dict
get_transport_detail_response_dict = get_transport_detail_response_instance.to_dict()
# create an instance of GetTransportDetailResponse from a dict
get_transport_detail_response_from_dict = GetTransportDetailResponse.from_dict(get_transport_detail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


