# OrdersAssignToFolderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_ids** | **List[str]** | list of order ids to be assigned | [optional] 
**folder** | **str** | folder to be assigned | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_assign_to_folder_request import OrdersAssignToFolderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersAssignToFolderRequest from a JSON string
orders_assign_to_folder_request_instance = OrdersAssignToFolderRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersAssignToFolderRequest.to_json())

# convert the object into a dict
orders_assign_to_folder_request_dict = orders_assign_to_folder_request_instance.to_dict()
# create an instance of OrdersAssignToFolderRequest from a dict
orders_assign_to_folder_request_from_dict = OrdersAssignToFolderRequest.from_dict(orders_assign_to_folder_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


