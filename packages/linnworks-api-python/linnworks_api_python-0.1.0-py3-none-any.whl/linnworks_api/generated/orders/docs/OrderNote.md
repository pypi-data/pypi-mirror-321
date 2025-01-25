# OrderNote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_note_id** | **str** |  | [optional] 
**order_id** | **str** |  | [optional] 
**note_date** | **datetime** |  | [optional] 
**internal** | **bool** |  | [optional] 
**note** | **str** |  | [optional] 
**created_by** | **str** |  | [optional] 
**note_type_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.order_note import OrderNote

# TODO update the JSON string below
json = "{}"
# create an instance of OrderNote from a JSON string
order_note_instance = OrderNote.from_json(json)
# print the JSON string representation of the object
print(OrderNote.to_json())

# convert the object into a dict
order_note_dict = order_note_instance.to_dict()
# create an instance of OrderNote from a dict
order_note_from_dict = OrderNote.from_dict(order_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


