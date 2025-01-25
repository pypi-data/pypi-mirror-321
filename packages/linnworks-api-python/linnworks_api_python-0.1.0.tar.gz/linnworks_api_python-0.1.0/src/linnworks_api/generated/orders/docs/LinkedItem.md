# LinkedItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_stock_id** | **str** |  | [optional] 
**item_number** | **str** |  | [optional] 
**item_name** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.linked_item import LinkedItem

# TODO update the JSON string below
json = "{}"
# create an instance of LinkedItem from a JSON string
linked_item_instance = LinkedItem.from_json(json)
# print the JSON string representation of the object
print(LinkedItem.to_json())

# convert the object into a dict
linked_item_dict = linked_item_instance.to_dict()
# create an instance of LinkedItem from a dict
linked_item_from_dict = LinkedItem.from_dict(linked_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


