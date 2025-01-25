# InventoryUnarchiveInventoryItemsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameters** | [**InventoryParametersRequest**](InventoryParametersRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_unarchive_inventory_items_request import InventoryUnarchiveInventoryItemsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryUnarchiveInventoryItemsRequest from a JSON string
inventory_unarchive_inventory_items_request_instance = InventoryUnarchiveInventoryItemsRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryUnarchiveInventoryItemsRequest.to_json())

# convert the object into a dict
inventory_unarchive_inventory_items_request_dict = inventory_unarchive_inventory_items_request_instance.to_dict()
# create an instance of InventoryUnarchiveInventoryItemsRequest from a dict
inventory_unarchive_inventory_items_request_from_dict = InventoryUnarchiveInventoryItemsRequest.from_dict(inventory_unarchive_inventory_items_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


