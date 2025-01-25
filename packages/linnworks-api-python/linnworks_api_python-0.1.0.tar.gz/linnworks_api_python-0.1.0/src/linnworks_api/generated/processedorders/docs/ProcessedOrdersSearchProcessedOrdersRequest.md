# ProcessedOrdersSearchProcessedOrdersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**SearchProcessedOrdersRequest**](SearchProcessedOrdersRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.processedorders.models.processed_orders_search_processed_orders_request import ProcessedOrdersSearchProcessedOrdersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessedOrdersSearchProcessedOrdersRequest from a JSON string
processed_orders_search_processed_orders_request_instance = ProcessedOrdersSearchProcessedOrdersRequest.from_json(json)
# print the JSON string representation of the object
print(ProcessedOrdersSearchProcessedOrdersRequest.to_json())

# convert the object into a dict
processed_orders_search_processed_orders_request_dict = processed_orders_search_processed_orders_request_instance.to_dict()
# create an instance of ProcessedOrdersSearchProcessedOrdersRequest from a dict
processed_orders_search_processed_orders_request_from_dict = ProcessedOrdersSearchProcessedOrdersRequest.from_dict(processed_orders_search_processed_orders_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


