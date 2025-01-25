# UpdateShippingPlanRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_id** | **int** |  | 
**from_location** | **str** |  | 
**packing_type** | **int** |  | [optional] 
**plan_id** | **str** |  | [optional] 
**status** | **int** |  | [optional] 
**to_location** | **str** |  | 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.update_shipping_plan_request import UpdateShippingPlanRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateShippingPlanRequest from a JSON string
update_shipping_plan_request_instance = UpdateShippingPlanRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateShippingPlanRequest.to_json())

# convert the object into a dict
update_shipping_plan_request_dict = update_shipping_plan_request_instance.to_dict()
# create an instance of UpdateShippingPlanRequest from a dict
update_shipping_plan_request_from_dict = UpdateShippingPlanRequest.from_dict(update_shipping_plan_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


