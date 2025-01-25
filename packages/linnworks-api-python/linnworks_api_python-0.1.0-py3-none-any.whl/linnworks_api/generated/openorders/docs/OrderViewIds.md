# OrderViewIds


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view_id** | **int** |  | [optional] [readonly] 
**location_id** | **str** |  | [optional] [readonly] 
**total_orders** | **int** |  | [optional] [readonly] 
**order_ids** | **List[str]** |  | [optional] [readonly] 
**count** | **int** |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.openorders.models.order_view_ids import OrderViewIds

# TODO update the JSON string below
json = "{}"
# create an instance of OrderViewIds from a JSON string
order_view_ids_instance = OrderViewIds.from_json(json)
# print the JSON string representation of the object
print(OrderViewIds.to_json())

# convert the object into a dict
order_view_ids_dict = order_view_ids_instance.to_dict()
# create an instance of OrderViewIds from a dict
order_view_ids_from_dict = OrderViewIds.from_dict(order_view_ids_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


