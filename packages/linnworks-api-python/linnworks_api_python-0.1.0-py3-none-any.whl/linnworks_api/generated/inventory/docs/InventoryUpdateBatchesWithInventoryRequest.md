# InventoryUpdateBatchesWithInventoryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batches** | [**List[StockItemBatch]**](StockItemBatch.md) | List of batches to update | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_update_batches_with_inventory_request import InventoryUpdateBatchesWithInventoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryUpdateBatchesWithInventoryRequest from a JSON string
inventory_update_batches_with_inventory_request_instance = InventoryUpdateBatchesWithInventoryRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryUpdateBatchesWithInventoryRequest.to_json())

# convert the object into a dict
inventory_update_batches_with_inventory_request_dict = inventory_update_batches_with_inventory_request_instance.to_dict()
# create an instance of InventoryUpdateBatchesWithInventoryRequest from a dict
inventory_update_batches_with_inventory_request_from_dict = InventoryUpdateBatchesWithInventoryRequest.from_dict(inventory_update_batches_with_inventory_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


