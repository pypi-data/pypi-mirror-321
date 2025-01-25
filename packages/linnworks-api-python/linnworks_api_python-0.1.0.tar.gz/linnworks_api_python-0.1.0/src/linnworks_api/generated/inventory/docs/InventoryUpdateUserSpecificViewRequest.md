# InventoryUpdateUserSpecificViewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view_name** | **str** | Current user-specific view name | [optional] 
**view** | [**InventoryView**](InventoryView.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_update_user_specific_view_request import InventoryUpdateUserSpecificViewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryUpdateUserSpecificViewRequest from a JSON string
inventory_update_user_specific_view_request_instance = InventoryUpdateUserSpecificViewRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryUpdateUserSpecificViewRequest.to_json())

# convert the object into a dict
inventory_update_user_specific_view_request_dict = inventory_update_user_specific_view_request_instance.to_dict()
# create an instance of InventoryUpdateUserSpecificViewRequest from a dict
inventory_update_user_specific_view_request_from_dict = InventoryUpdateUserSpecificViewRequest.from_dict(inventory_update_user_specific_view_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


