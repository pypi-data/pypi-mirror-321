# OrderRelation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_order_id** | **str** |  | [optional] 
**child_order_id** | **str** |  | [optional] 
**parent** | **int** |  | [optional] 
**child** | **int** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.order_relation import OrderRelation

# TODO update the JSON string below
json = "{}"
# create an instance of OrderRelation from a JSON string
order_relation_instance = OrderRelation.from_json(json)
# print the JSON string representation of the object
print(OrderRelation.to_json())

# convert the object into a dict
order_relation_dict = order_relation_instance.to_dict()
# create an instance of OrderRelation from a dict
order_relation_from_dict = OrderRelation.from_dict(order_relation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


