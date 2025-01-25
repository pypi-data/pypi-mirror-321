# GetOpenOrdersDetailsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_ids** | **List[str]** | List of order ids as unique identifiers | [optional] 
**detail_level** | **List[str]** | (optional) List of detail level limiters. If the list is null or empty Full details will be returned, as in all detail levels are applied | [optional] 

## Example

```python
from linnworks_api.generated.openorders.models.get_open_orders_details_request import GetOpenOrdersDetailsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetOpenOrdersDetailsRequest from a JSON string
get_open_orders_details_request_instance = GetOpenOrdersDetailsRequest.from_json(json)
# print the JSON string representation of the object
print(GetOpenOrdersDetailsRequest.to_json())

# convert the object into a dict
get_open_orders_details_request_dict = get_open_orders_details_request_instance.to_dict()
# create an instance of GetOpenOrdersDetailsRequest from a dict
get_open_orders_details_request_from_dict = GetOpenOrdersDetailsRequest.from_dict(get_open_orders_details_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


