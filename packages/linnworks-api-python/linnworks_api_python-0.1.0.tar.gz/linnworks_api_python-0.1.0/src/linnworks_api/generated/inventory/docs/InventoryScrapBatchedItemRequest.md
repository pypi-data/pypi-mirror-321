# InventoryScrapBatchedItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**ScrapBatchedItemRequest**](ScrapBatchedItemRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_scrap_batched_item_request import InventoryScrapBatchedItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryScrapBatchedItemRequest from a JSON string
inventory_scrap_batched_item_request_instance = InventoryScrapBatchedItemRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryScrapBatchedItemRequest.to_json())

# convert the object into a dict
inventory_scrap_batched_item_request_dict = inventory_scrap_batched_item_request_instance.to_dict()
# create an instance of InventoryScrapBatchedItemRequest from a dict
inventory_scrap_batched_item_request_from_dict = InventoryScrapBatchedItemRequest.from_dict(inventory_scrap_batched_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


