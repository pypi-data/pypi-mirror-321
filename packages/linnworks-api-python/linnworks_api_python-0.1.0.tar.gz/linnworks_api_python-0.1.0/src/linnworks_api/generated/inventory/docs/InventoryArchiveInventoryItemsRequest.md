# InventoryArchiveInventoryItemsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameters** | [**InventoryParametersRequest**](InventoryParametersRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_archive_inventory_items_request import InventoryArchiveInventoryItemsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryArchiveInventoryItemsRequest from a JSON string
inventory_archive_inventory_items_request_instance = InventoryArchiveInventoryItemsRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryArchiveInventoryItemsRequest.to_json())

# convert the object into a dict
inventory_archive_inventory_items_request_dict = inventory_archive_inventory_items_request_instance.to_dict()
# create an instance of InventoryArchiveInventoryItemsRequest from a dict
inventory_archive_inventory_items_request_from_dict = InventoryArchiveInventoryItemsRequest.from_dict(inventory_archive_inventory_items_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


