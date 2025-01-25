# OrderNoteType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note_type_id** | **int** |  | [optional] 
**note_type** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.order_note_type import OrderNoteType

# TODO update the JSON string below
json = "{}"
# create an instance of OrderNoteType from a JSON string
order_note_type_instance = OrderNoteType.from_json(json)
# print the JSON string representation of the object
print(OrderNoteType.to_json())

# convert the object into a dict
order_note_type_dict = order_note_type_instance.to_dict()
# create an instance of OrderNoteType from a dict
order_note_type_from_dict = OrderNoteType.from_dict(order_note_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


