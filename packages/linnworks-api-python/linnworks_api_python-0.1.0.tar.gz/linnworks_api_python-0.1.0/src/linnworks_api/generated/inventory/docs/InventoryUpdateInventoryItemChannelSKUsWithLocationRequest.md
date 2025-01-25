# InventoryUpdateInventoryItemChannelSKUsWithLocationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory_item_channel_skus_with_location** | [**List[StockItemChannelSKUWithLocation]**](StockItemChannelSKUWithLocation.md) | Listing information | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_update_inventory_item_channel_skus_with_location_request import InventoryUpdateInventoryItemChannelSKUsWithLocationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryUpdateInventoryItemChannelSKUsWithLocationRequest from a JSON string
inventory_update_inventory_item_channel_skus_with_location_request_instance = InventoryUpdateInventoryItemChannelSKUsWithLocationRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryUpdateInventoryItemChannelSKUsWithLocationRequest.to_json())

# convert the object into a dict
inventory_update_inventory_item_channel_skus_with_location_request_dict = inventory_update_inventory_item_channel_skus_with_location_request_instance.to_dict()
# create an instance of InventoryUpdateInventoryItemChannelSKUsWithLocationRequest from a dict
inventory_update_inventory_item_channel_skus_with_location_request_from_dict = InventoryUpdateInventoryItemChannelSKUsWithLocationRequest.from_dict(inventory_update_inventory_item_channel_skus_with_location_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


