# InventoryCreateInventoryItemChannelSKUsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory_item_channel_skus** | [**List[StockItemChannelSKU]**](StockItemChannelSKU.md) | stockitem channel skus | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_create_inventory_item_channel_skus_request import InventoryCreateInventoryItemChannelSKUsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryCreateInventoryItemChannelSKUsRequest from a JSON string
inventory_create_inventory_item_channel_skus_request_instance = InventoryCreateInventoryItemChannelSKUsRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryCreateInventoryItemChannelSKUsRequest.to_json())

# convert the object into a dict
inventory_create_inventory_item_channel_skus_request_dict = inventory_create_inventory_item_channel_skus_request_instance.to_dict()
# create an instance of InventoryCreateInventoryItemChannelSKUsRequest from a dict
inventory_create_inventory_item_channel_skus_request_from_dict = InventoryCreateInventoryItemChannelSKUsRequest.from_dict(inventory_create_inventory_item_channel_skus_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


