# GetOrdersLowFidelityResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**orders** | [**List[OpenOrderLowFidelity]**](OpenOrderLowFidelity.md) | List of low fidelity order headers with order items, composites and product identifiers | [optional] 

## Example

```python
from linnworks_api.generated.openorders.models.get_orders_low_fidelity_response import GetOrdersLowFidelityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrdersLowFidelityResponse from a JSON string
get_orders_low_fidelity_response_instance = GetOrdersLowFidelityResponse.from_json(json)
# print the JSON string representation of the object
print(GetOrdersLowFidelityResponse.to_json())

# convert the object into a dict
get_orders_low_fidelity_response_dict = get_orders_low_fidelity_response_instance.to_dict()
# create an instance of GetOrdersLowFidelityResponse from a dict
get_orders_low_fidelity_response_from_dict = GetOrdersLowFidelityResponse.from_dict(get_orders_low_fidelity_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


