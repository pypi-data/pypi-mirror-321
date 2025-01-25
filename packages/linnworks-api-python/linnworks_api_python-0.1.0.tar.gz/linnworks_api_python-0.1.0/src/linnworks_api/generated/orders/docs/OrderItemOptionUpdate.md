# OrderItemOptionUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_entry** | **bool** |  | [optional] 
**pk_option_id** | **str** |  | [optional] 
**var_property** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.order_item_option_update import OrderItemOptionUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of OrderItemOptionUpdate from a JSON string
order_item_option_update_instance = OrderItemOptionUpdate.from_json(json)
# print the JSON string representation of the object
print(OrderItemOptionUpdate.to_json())

# convert the object into a dict
order_item_option_update_dict = order_item_option_update_instance.to_dict()
# create an instance of OrderItemOptionUpdate from a dict
order_item_option_update_from_dict = OrderItemOptionUpdate.from_dict(order_item_option_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


