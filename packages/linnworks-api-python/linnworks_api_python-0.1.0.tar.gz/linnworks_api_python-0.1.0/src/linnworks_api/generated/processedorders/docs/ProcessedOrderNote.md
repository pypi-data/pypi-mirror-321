# ProcessedOrderNote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_order_note_id** | **str** |  | [optional] 
**fk_order_id** | **str** |  | [optional] 
**note** | **str** |  | [optional] 
**note_entry_date** | **datetime** |  | [optional] 
**note_user_name** | **str** |  | [optional] 
**internal** | **bool** |  | [optional] 
**note_type_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.processedorders.models.processed_order_note import ProcessedOrderNote

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessedOrderNote from a JSON string
processed_order_note_instance = ProcessedOrderNote.from_json(json)
# print the JSON string representation of the object
print(ProcessedOrderNote.to_json())

# convert the object into a dict
processed_order_note_dict = processed_order_note_instance.to_dict()
# create an instance of ProcessedOrderNote from a dict
processed_order_note_from_dict = ProcessedOrderNote.from_dict(processed_order_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


