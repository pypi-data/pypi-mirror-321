# ProcessedOrdersChangeOrderNoteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_order_note_id** | **str** | Primary key for order note | [optional] 
**note_text** | **str** | New note message | [optional] 
**is_internal** | **bool** | Whether the note is an internal note | [optional] 
**note_type_id** | **int** | Set the type of note | [optional] 

## Example

```python
from linnworks_api.generated.processedorders.models.processed_orders_change_order_note_request import ProcessedOrdersChangeOrderNoteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessedOrdersChangeOrderNoteRequest from a JSON string
processed_orders_change_order_note_request_instance = ProcessedOrdersChangeOrderNoteRequest.from_json(json)
# print the JSON string representation of the object
print(ProcessedOrdersChangeOrderNoteRequest.to_json())

# convert the object into a dict
processed_orders_change_order_note_request_dict = processed_orders_change_order_note_request_instance.to_dict()
# create an instance of ProcessedOrdersChangeOrderNoteRequest from a dict
processed_orders_change_order_note_request_from_dict = ProcessedOrdersChangeOrderNoteRequest.from_dict(processed_orders_change_order_note_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


