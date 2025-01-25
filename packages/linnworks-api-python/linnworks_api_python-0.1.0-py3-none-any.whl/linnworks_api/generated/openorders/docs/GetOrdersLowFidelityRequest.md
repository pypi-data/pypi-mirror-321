# GetOrdersLowFidelityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_id** | **str** | (Optional) Fulfilment location id. Defaults to Default location | [optional] 

## Example

```python
from linnworks_api.generated.openorders.models.get_orders_low_fidelity_request import GetOrdersLowFidelityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrdersLowFidelityRequest from a JSON string
get_orders_low_fidelity_request_instance = GetOrdersLowFidelityRequest.from_json(json)
# print the JSON string representation of the object
print(GetOrdersLowFidelityRequest.to_json())

# convert the object into a dict
get_orders_low_fidelity_request_dict = get_orders_low_fidelity_request_instance.to_dict()
# create an instance of GetOrdersLowFidelityRequest from a dict
get_orders_low_fidelity_request_from_dict = GetOrdersLowFidelityRequest.from_dict(get_orders_low_fidelity_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


