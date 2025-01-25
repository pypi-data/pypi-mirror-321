# GetShippingPlanByIdResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_id** | **int** |  | [optional] 
**default_shipment_id** | **str** |  | [optional] 
**from_location** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**is_packing_info_known** | **bool** |  | [optional] 
**plan_id** | **str** |  | [optional] 
**shipment_items_count** | **int** |  | [optional] 
**shipments** | [**List[ShipmentResponse]**](ShipmentResponse.md) |  | [optional] 
**status** | [**ShippingPlanStatus**](ShippingPlanStatus.md) |  | [optional] 
**to_location** | **str** |  | [optional] 
**placement_option_id** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_v2.models.get_shipping_plan_by_id_response import GetShippingPlanByIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetShippingPlanByIdResponse from a JSON string
get_shipping_plan_by_id_response_instance = GetShippingPlanByIdResponse.from_json(json)
# print the JSON string representation of the object
print(GetShippingPlanByIdResponse.to_json())

# convert the object into a dict
get_shipping_plan_by_id_response_dict = get_shipping_plan_by_id_response_instance.to_dict()
# create an instance of GetShippingPlanByIdResponse from a dict
get_shipping_plan_by_id_response_from_dict = GetShippingPlanByIdResponse.from_dict(get_shipping_plan_by_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


