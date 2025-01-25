# InventoryCreateUserSpecificViewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view** | [**InventoryView**](InventoryView.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_create_user_specific_view_request import InventoryCreateUserSpecificViewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryCreateUserSpecificViewRequest from a JSON string
inventory_create_user_specific_view_request_instance = InventoryCreateUserSpecificViewRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryCreateUserSpecificViewRequest.to_json())

# convert the object into a dict
inventory_create_user_specific_view_request_dict = inventory_create_user_specific_view_request_instance.to_dict()
# create an instance of InventoryCreateUserSpecificViewRequest from a dict
inventory_create_user_specific_view_request_from_dict = InventoryCreateUserSpecificViewRequest.from_dict(inventory_create_user_specific_view_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


