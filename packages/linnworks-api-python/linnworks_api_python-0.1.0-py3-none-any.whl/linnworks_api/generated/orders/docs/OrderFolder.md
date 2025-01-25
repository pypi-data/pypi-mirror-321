# OrderFolder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_folder_id** | **str** |  | [optional] 
**folder_name** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.order_folder import OrderFolder

# TODO update the JSON string below
json = "{}"
# create an instance of OrderFolder from a JSON string
order_folder_instance = OrderFolder.from_json(json)
# print the JSON string representation of the object
print(OrderFolder.to_json())

# convert the object into a dict
order_folder_dict = order_folder_instance.to_dict()
# create an instance of OrderFolder from a dict
order_folder_from_dict = OrderFolder.from_dict(order_folder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


