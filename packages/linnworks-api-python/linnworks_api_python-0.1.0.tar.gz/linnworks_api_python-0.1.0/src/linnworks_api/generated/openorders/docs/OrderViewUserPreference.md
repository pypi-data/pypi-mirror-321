# OrderViewUserPreference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view_id** | **int** |  | [optional] 
**is_visible** | **bool** |  | [optional] 
**sequence** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.openorders.models.order_view_user_preference import OrderViewUserPreference

# TODO update the JSON string below
json = "{}"
# create an instance of OrderViewUserPreference from a JSON string
order_view_user_preference_instance = OrderViewUserPreference.from_json(json)
# print the JSON string representation of the object
print(OrderViewUserPreference.to_json())

# convert the object into a dict
order_view_user_preference_dict = order_view_user_preference_instance.to_dict()
# create an instance of OrderViewUserPreference from a dict
order_view_user_preference_from_dict = OrderViewUserPreference.from_dict(order_view_user_preference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


