# AddShipmentPalletsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipment_pallet_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**height** | **float** |  | [optional] 
**depth** | **float** |  | [optional] 
**width** | **float** |  | [optional] 
**shipment_dimension_unit_id** | **int** |  | [optional] 
**weight** | **float** |  | [optional] 
**shipment_weight_unit_id** | **int** |  | [optional] 
**is_stacked** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.add_shipment_pallets_response import AddShipmentPalletsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddShipmentPalletsResponse from a JSON string
add_shipment_pallets_response_instance = AddShipmentPalletsResponse.from_json(json)
# print the JSON string representation of the object
print(AddShipmentPalletsResponse.to_json())

# convert the object into a dict
add_shipment_pallets_response_dict = add_shipment_pallets_response_instance.to_dict()
# create an instance of AddShipmentPalletsResponse from a dict
add_shipment_pallets_response_from_dict = AddShipmentPalletsResponse.from_dict(add_shipment_pallets_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


