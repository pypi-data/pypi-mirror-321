# GetOpenOrdersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view_id** | **int** |  | 
**location_id** | **str** |  | 
**entries_per_page** | **int** |  | 
**page_number** | **int** |  | [optional] 
**order_ids** | **List[str]** |  | [optional] 

## Example

```python
from linnworks_api.generated.openorders.models.get_open_orders_request import GetOpenOrdersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetOpenOrdersRequest from a JSON string
get_open_orders_request_instance = GetOpenOrdersRequest.from_json(json)
# print the JSON string representation of the object
print(GetOpenOrdersRequest.to_json())

# convert the object into a dict
get_open_orders_request_dict = get_open_orders_request_instance.to_dict()
# create an instance of GetOpenOrdersRequest from a dict
get_open_orders_request_from_dict = GetOpenOrdersRequest.from_dict(get_open_orders_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


