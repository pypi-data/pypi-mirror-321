# UserOrderView


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_view_id** | **int** |  | [optional] 
**view_name** | **str** |  | [optional] 
**owner_name** | **str** |  | [optional] 
**allow_modify** | **bool** |  | [optional] 
**json_detail** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.user_order_view import UserOrderView

# TODO update the JSON string below
json = "{}"
# create an instance of UserOrderView from a JSON string
user_order_view_instance = UserOrderView.from_json(json)
# print the JSON string representation of the object
print(UserOrderView.to_json())

# convert the object into a dict
user_order_view_dict = user_order_view_instance.to_dict()
# create an instance of UserOrderView from a dict
user_order_view_from_dict = UserOrderView.from_dict(user_order_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


