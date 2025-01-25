# InventoryDeleteInventoryItemImageBulkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**List[DeleteInventoryItemImagesRequest]**](DeleteInventoryItemImagesRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_delete_inventory_item_image_bulk_request import InventoryDeleteInventoryItemImageBulkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryDeleteInventoryItemImageBulkRequest from a JSON string
inventory_delete_inventory_item_image_bulk_request_instance = InventoryDeleteInventoryItemImageBulkRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryDeleteInventoryItemImageBulkRequest.to_json())

# convert the object into a dict
inventory_delete_inventory_item_image_bulk_request_dict = inventory_delete_inventory_item_image_bulk_request_instance.to_dict()
# create an instance of InventoryDeleteInventoryItemImageBulkRequest from a dict
inventory_delete_inventory_item_image_bulk_request_from_dict = InventoryDeleteInventoryItemImageBulkRequest.from_dict(inventory_delete_inventory_item_image_bulk_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


