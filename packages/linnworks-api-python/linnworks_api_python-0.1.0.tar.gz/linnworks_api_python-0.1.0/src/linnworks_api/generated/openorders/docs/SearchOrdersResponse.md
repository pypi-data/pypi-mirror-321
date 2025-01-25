# SearchOrdersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**open_orders** | [**List[OrderViewIds]**](OrderViewIds.md) |  | [optional] 
**processed_orders** | **List[str]** |  | [optional] 

## Example

```python
from linnworks_api.generated.openorders.models.search_orders_response import SearchOrdersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SearchOrdersResponse from a JSON string
search_orders_response_instance = SearchOrdersResponse.from_json(json)
# print the JSON string representation of the object
print(SearchOrdersResponse.to_json())

# convert the object into a dict
search_orders_response_dict = search_orders_response_instance.to_dict()
# create an instance of SearchOrdersResponse from a dict
search_orders_response_from_dict = SearchOrdersResponse.from_dict(search_orders_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


