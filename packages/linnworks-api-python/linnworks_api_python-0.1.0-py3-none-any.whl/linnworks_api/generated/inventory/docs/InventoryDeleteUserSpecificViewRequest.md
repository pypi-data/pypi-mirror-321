# InventoryDeleteUserSpecificViewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view_name** | **str** | User-specific view name | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_delete_user_specific_view_request import InventoryDeleteUserSpecificViewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryDeleteUserSpecificViewRequest from a JSON string
inventory_delete_user_specific_view_request_instance = InventoryDeleteUserSpecificViewRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryDeleteUserSpecificViewRequest.to_json())

# convert the object into a dict
inventory_delete_user_specific_view_request_dict = inventory_delete_user_specific_view_request_instance.to_dict()
# create an instance of InventoryDeleteUserSpecificViewRequest from a dict
inventory_delete_user_specific_view_request_from_dict = InventoryDeleteUserSpecificViewRequest.from_dict(inventory_delete_user_specific_view_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


