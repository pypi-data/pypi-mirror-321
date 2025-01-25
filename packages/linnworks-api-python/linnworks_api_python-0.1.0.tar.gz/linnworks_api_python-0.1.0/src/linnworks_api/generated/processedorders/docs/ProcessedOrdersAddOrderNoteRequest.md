# ProcessedOrdersAddOrderNoteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_order_id** | **str** | The order id | [optional] 
**note_text** | **str** | The note text | [optional] 
**is_internal** | **bool** | True if the note should be internal, False if it shouldn&#39;t | [optional] 

## Example

```python
from linnworks_api.generated.processedorders.models.processed_orders_add_order_note_request import ProcessedOrdersAddOrderNoteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessedOrdersAddOrderNoteRequest from a JSON string
processed_orders_add_order_note_request_instance = ProcessedOrdersAddOrderNoteRequest.from_json(json)
# print the JSON string representation of the object
print(ProcessedOrdersAddOrderNoteRequest.to_json())

# convert the object into a dict
processed_orders_add_order_note_request_dict = processed_orders_add_order_note_request_instance.to_dict()
# create an instance of ProcessedOrdersAddOrderNoteRequest from a dict
processed_orders_add_order_note_request_from_dict = ProcessedOrdersAddOrderNoteRequest.from_dict(processed_orders_add_order_note_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


