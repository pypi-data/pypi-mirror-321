# SearchOrdersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_id** | **str** |  | [optional] 
**search_term** | **str** |  | [optional] 
**include_processed** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.openorders.models.search_orders_request import SearchOrdersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SearchOrdersRequest from a JSON string
search_orders_request_instance = SearchOrdersRequest.from_json(json)
# print the JSON string representation of the object
print(SearchOrdersRequest.to_json())

# convert the object into a dict
search_orders_request_dict = search_orders_request_instance.to_dict()
# create an instance of SearchOrdersRequest from a dict
search_orders_request_from_dict = SearchOrdersRequest.from_dict(search_orders_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


