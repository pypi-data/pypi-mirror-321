# CreateShippingPlanRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_id** | **int** |  | [optional] 
**from_location_id** | **str** |  | 
**packing_type** | **int** |  | [optional] 
**who_preps** | [**WhoPreps**](WhoPreps.md) |  | [optional] 
**plan_id** | **str** |  | [optional] 
**status** | **int** |  | [optional] 
**to_location_id** | **str** |  | 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.create_shipping_plan_request import CreateShippingPlanRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateShippingPlanRequest from a JSON string
create_shipping_plan_request_instance = CreateShippingPlanRequest.from_json(json)
# print the JSON string representation of the object
print(CreateShippingPlanRequest.to_json())

# convert the object into a dict
create_shipping_plan_request_dict = create_shipping_plan_request_instance.to_dict()
# create an instance of CreateShippingPlanRequest from a dict
create_shipping_plan_request_from_dict = CreateShippingPlanRequest.from_dict(create_shipping_plan_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


