# GetOpenOrdersDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**orders** | [**List[OrderDetails]**](OrderDetails.md) | List of orders | [optional] 

## Example

```python
from linnworks_api.generated.openorders.models.get_open_orders_details_response import GetOpenOrdersDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetOpenOrdersDetailsResponse from a JSON string
get_open_orders_details_response_instance = GetOpenOrdersDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(GetOpenOrdersDetailsResponse.to_json())

# convert the object into a dict
get_open_orders_details_response_dict = get_open_orders_details_response_instance.to_dict()
# create an instance of GetOpenOrdersDetailsResponse from a dict
get_open_orders_details_response_from_dict = GetOpenOrdersDetailsResponse.from_dict(get_open_orders_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


