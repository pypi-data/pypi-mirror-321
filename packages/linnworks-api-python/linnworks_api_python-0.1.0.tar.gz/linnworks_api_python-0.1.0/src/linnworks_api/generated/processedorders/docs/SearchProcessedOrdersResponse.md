# SearchProcessedOrdersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**processed_orders** | [**GenericPagedResultProcessedOrderWeb**](GenericPagedResultProcessedOrderWeb.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.processedorders.models.search_processed_orders_response import SearchProcessedOrdersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SearchProcessedOrdersResponse from a JSON string
search_processed_orders_response_instance = SearchProcessedOrdersResponse.from_json(json)
# print the JSON string representation of the object
print(SearchProcessedOrdersResponse.to_json())

# convert the object into a dict
search_processed_orders_response_dict = search_processed_orders_response_instance.to_dict()
# create an instance of SearchProcessedOrdersResponse from a dict
search_processed_orders_response_from_dict = SearchProcessedOrdersResponse.from_dict(search_processed_orders_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


