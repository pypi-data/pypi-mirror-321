# UpdateShippingPlanRequestInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_id** | **int** |  | 
**from_location** | **str** |  | 
**inbound_plan_id** | **str** |  | [optional] 
**is_packing_info_known** | **bool** |  | [optional] 
**plan_id** | **str** |  | [optional] 
**status** | [**ShippingPlanStatus**](ShippingPlanStatus.md) |  | [optional] 
**to_location** | **str** |  | 

## Example

```python
from linnworks_api.generated.warehousetransfer_v2.models.update_shipping_plan_request_input import UpdateShippingPlanRequestInput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateShippingPlanRequestInput from a JSON string
update_shipping_plan_request_input_instance = UpdateShippingPlanRequestInput.from_json(json)
# print the JSON string representation of the object
print(UpdateShippingPlanRequestInput.to_json())

# convert the object into a dict
update_shipping_plan_request_input_dict = update_shipping_plan_request_input_instance.to_dict()
# create an instance of UpdateShippingPlanRequestInput from a dict
update_shipping_plan_request_input_from_dict = UpdateShippingPlanRequestInput.from_dict(update_shipping_plan_request_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


