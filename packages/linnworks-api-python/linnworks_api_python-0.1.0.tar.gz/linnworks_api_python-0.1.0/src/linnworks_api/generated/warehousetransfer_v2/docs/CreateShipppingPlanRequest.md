# CreateShipppingPlanRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_id** | **int** |  | [optional] 
**from_location_id** | **str** |  | 
**plan_id** | **str** |  | [optional] 
**status** | [**ShippingPlanStatus**](ShippingPlanStatus.md) |  | [optional] 
**to_location_id** | **str** |  | 

## Example

```python
from linnworks_api.generated.warehousetransfer_v2.models.create_shippping_plan_request import CreateShipppingPlanRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateShipppingPlanRequest from a JSON string
create_shippping_plan_request_instance = CreateShipppingPlanRequest.from_json(json)
# print the JSON string representation of the object
print(CreateShipppingPlanRequest.to_json())

# convert the object into a dict
create_shippping_plan_request_dict = create_shippping_plan_request_instance.to_dict()
# create an instance of CreateShipppingPlanRequest from a dict
create_shippping_plan_request_from_dict = CreateShipppingPlanRequest.from_dict(create_shippping_plan_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


