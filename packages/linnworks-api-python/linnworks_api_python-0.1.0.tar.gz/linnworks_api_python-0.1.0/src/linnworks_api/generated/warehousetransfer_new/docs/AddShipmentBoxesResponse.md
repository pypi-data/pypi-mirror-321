# AddShipmentBoxesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipment_box_id** | **int** |  | [optional] 
**shipment_id** | **int** |  | [optional] 
**shipment_pallet_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**height** | **float** |  | [optional] 
**depth** | **float** |  | [optional] 
**width** | **float** |  | [optional] 
**weight** | **float** |  | [optional] 
**tracking_number** | **str** |  | [optional] 
**shipment_dimension_unit** | [**AmazonShipmentDimensionUnit**](AmazonShipmentDimensionUnit.md) |  | [optional] 
**shipment_weight_unit** | [**AmazonShipmentWeightUnit**](AmazonShipmentWeightUnit.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.add_shipment_boxes_response import AddShipmentBoxesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddShipmentBoxesResponse from a JSON string
add_shipment_boxes_response_instance = AddShipmentBoxesResponse.from_json(json)
# print the JSON string representation of the object
print(AddShipmentBoxesResponse.to_json())

# convert the object into a dict
add_shipment_boxes_response_dict = add_shipment_boxes_response_instance.to_dict()
# create an instance of AddShipmentBoxesResponse from a dict
add_shipment_boxes_response_from_dict = AddShipmentBoxesResponse.from_dict(add_shipment_boxes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


