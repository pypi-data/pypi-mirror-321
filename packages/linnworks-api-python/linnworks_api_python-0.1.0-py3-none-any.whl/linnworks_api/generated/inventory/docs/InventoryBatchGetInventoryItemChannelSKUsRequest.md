# InventoryBatchGetInventoryItemChannelSKUsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory_item_ids** | **List[str]** | List of Stock item Id&#39;s&#39; | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_batch_get_inventory_item_channel_skus_request import InventoryBatchGetInventoryItemChannelSKUsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryBatchGetInventoryItemChannelSKUsRequest from a JSON string
inventory_batch_get_inventory_item_channel_skus_request_instance = InventoryBatchGetInventoryItemChannelSKUsRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryBatchGetInventoryItemChannelSKUsRequest.to_json())

# convert the object into a dict
inventory_batch_get_inventory_item_channel_skus_request_dict = inventory_batch_get_inventory_item_channel_skus_request_instance.to_dict()
# create an instance of InventoryBatchGetInventoryItemChannelSKUsRequest from a dict
inventory_batch_get_inventory_item_channel_skus_request_from_dict = InventoryBatchGetInventoryItemChannelSKUsRequest.from_dict(inventory_batch_get_inventory_item_channel_skus_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


