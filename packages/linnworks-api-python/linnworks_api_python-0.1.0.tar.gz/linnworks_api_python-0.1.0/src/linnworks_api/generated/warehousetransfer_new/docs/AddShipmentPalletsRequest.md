# AddShipmentPalletsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipment_id** | **int** |  | [optional] 
**shipping_plan_id** | **int** |  | [optional] 
**shipment_pallets** | [**List[ShipmentPalletCreateModel]**](ShipmentPalletCreateModel.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.add_shipment_pallets_request import AddShipmentPalletsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddShipmentPalletsRequest from a JSON string
add_shipment_pallets_request_instance = AddShipmentPalletsRequest.from_json(json)
# print the JSON string representation of the object
print(AddShipmentPalletsRequest.to_json())

# convert the object into a dict
add_shipment_pallets_request_dict = add_shipment_pallets_request_instance.to_dict()
# create an instance of AddShipmentPalletsRequest from a dict
add_shipment_pallets_request_from_dict = AddShipmentPalletsRequest.from_dict(add_shipment_pallets_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


