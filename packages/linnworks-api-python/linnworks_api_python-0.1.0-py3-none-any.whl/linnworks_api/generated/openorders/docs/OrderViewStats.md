# OrderViewStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view_id** | **int** |  | [optional] 
**view_name** | **str** |  | [optional] 
**is_system** | **bool** |  | [optional] 
**total_orders** | **int** |  | [optional] 
**location_id** | **str** |  | [optional] 
**expiry_date** | **datetime** |  | [optional] [readonly] 
**is_calculating** | **bool** |  | [optional] [readonly] 
**view_exists** | **bool** |  | [optional] [readonly] 
**last_requested** | **datetime** |  | [optional] [readonly] 
**user_management** | [**ViewUserManagement**](ViewUserManagement.md) |  | [optional] 
**order_view_user_preference** | [**OrderViewUserPreference**](OrderViewUserPreference.md) |  | [optional] 
**owner** | [**ViewUser**](ViewUser.md) |  | [optional] 
**is_cacheable** | **bool** |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.openorders.models.order_view_stats import OrderViewStats

# TODO update the JSON string below
json = "{}"
# create an instance of OrderViewStats from a JSON string
order_view_stats_instance = OrderViewStats.from_json(json)
# print the JSON string representation of the object
print(OrderViewStats.to_json())

# convert the object into a dict
order_view_stats_dict = order_view_stats_instance.to_dict()
# create an instance of OrderViewStats from a dict
order_view_stats_from_dict = OrderViewStats.from_dict(order_view_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


