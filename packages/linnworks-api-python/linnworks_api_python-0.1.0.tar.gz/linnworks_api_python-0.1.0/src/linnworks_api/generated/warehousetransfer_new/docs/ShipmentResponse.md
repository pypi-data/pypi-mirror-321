# ShipmentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_date** | **datetime** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**shipment_id** | **str** |  | [optional] 
**shipping_items** | [**List[ShipmentItemResponse]**](ShipmentItemResponse.md) |  | [optional] 
**shipping_plan_id** | **int** |  | [optional] 
**ship_to** | **str** |  | [optional] 
**status_id** | **int** |  | [optional] 
**who_preps** | [**WhoPreps**](WhoPreps.md) |  | [optional] 
**update_date** | **datetime** |  | [optional] 
**warehouse_address** | **str** |  | [optional] 
**is_converted_to_send_to_amazon** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.shipment_response import ShipmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentResponse from a JSON string
shipment_response_instance = ShipmentResponse.from_json(json)
# print the JSON string representation of the object
print(ShipmentResponse.to_json())

# convert the object into a dict
shipment_response_dict = shipment_response_instance.to_dict()
# create an instance of ShipmentResponse from a dict
shipment_response_from_dict = ShipmentResponse.from_dict(shipment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


