# ProcessedOrdersDeleteOrderNoteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_order_note_id** | **str** | Primary key for order note | [optional] 

## Example

```python
from linnworks_api.generated.processedorders.models.processed_orders_delete_order_note_request import ProcessedOrdersDeleteOrderNoteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessedOrdersDeleteOrderNoteRequest from a JSON string
processed_orders_delete_order_note_request_instance = ProcessedOrdersDeleteOrderNoteRequest.from_json(json)
# print the JSON string representation of the object
print(ProcessedOrdersDeleteOrderNoteRequest.to_json())

# convert the object into a dict
processed_orders_delete_order_note_request_dict = processed_orders_delete_order_note_request_instance.to_dict()
# create an instance of ProcessedOrdersDeleteOrderNoteRequest from a dict
processed_orders_delete_order_note_request_from_dict = ProcessedOrdersDeleteOrderNoteRequest.from_dict(processed_orders_delete_order_note_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


