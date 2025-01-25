# OrdersSetAvailableFoldersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folders** | [**List[OrderFolder]**](OrderFolder.md) | folders list | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_set_available_folders_request import OrdersSetAvailableFoldersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersSetAvailableFoldersRequest from a JSON string
orders_set_available_folders_request_instance = OrdersSetAvailableFoldersRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersSetAvailableFoldersRequest.to_json())

# convert the object into a dict
orders_set_available_folders_request_dict = orders_set_available_folders_request_instance.to_dict()
# create an instance of OrdersSetAvailableFoldersRequest from a dict
orders_set_available_folders_request_from_dict = OrdersSetAvailableFoldersRequest.from_dict(orders_set_available_folders_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


