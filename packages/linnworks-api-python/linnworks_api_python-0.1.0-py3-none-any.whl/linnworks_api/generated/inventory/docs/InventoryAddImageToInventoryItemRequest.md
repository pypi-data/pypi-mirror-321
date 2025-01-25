# InventoryAddImageToInventoryItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**AddImageToInventoryItemRequest**](AddImageToInventoryItemRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_add_image_to_inventory_item_request import InventoryAddImageToInventoryItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryAddImageToInventoryItemRequest from a JSON string
inventory_add_image_to_inventory_item_request_instance = InventoryAddImageToInventoryItemRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryAddImageToInventoryItemRequest.to_json())

# convert the object into a dict
inventory_add_image_to_inventory_item_request_dict = inventory_add_image_to_inventory_item_request_instance.to_dict()
# create an instance of InventoryAddImageToInventoryItemRequest from a dict
inventory_add_image_to_inventory_item_request_from_dict = InventoryAddImageToInventoryItemRequest.from_dict(inventory_add_image_to_inventory_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


