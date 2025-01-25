# InventoryDuplicateInventoryItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory_item** | [**StockItem**](StockItem.md) |  | [optional] 
**source_item_id** | **str** | Source StockItem | [optional] 
**copy_images** | **bool** | Set to True to copy images from source stock item | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_duplicate_inventory_item_request import InventoryDuplicateInventoryItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryDuplicateInventoryItemRequest from a JSON string
inventory_duplicate_inventory_item_request_instance = InventoryDuplicateInventoryItemRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryDuplicateInventoryItemRequest.to_json())

# convert the object into a dict
inventory_duplicate_inventory_item_request_dict = inventory_duplicate_inventory_item_request_instance.to_dict()
# create an instance of InventoryDuplicateInventoryItemRequest from a dict
inventory_duplicate_inventory_item_request_from_dict = InventoryDuplicateInventoryItemRequest.from_dict(inventory_duplicate_inventory_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


