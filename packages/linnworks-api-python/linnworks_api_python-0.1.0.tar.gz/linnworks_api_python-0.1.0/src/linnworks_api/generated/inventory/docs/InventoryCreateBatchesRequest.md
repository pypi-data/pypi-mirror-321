# InventoryCreateBatchesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batches** | [**List[StockItemBatch]**](StockItemBatch.md) | List of batches to create | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_create_batches_request import InventoryCreateBatchesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryCreateBatchesRequest from a JSON string
inventory_create_batches_request_instance = InventoryCreateBatchesRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryCreateBatchesRequest.to_json())

# convert the object into a dict
inventory_create_batches_request_dict = inventory_create_batches_request_instance.to_dict()
# create an instance of InventoryCreateBatchesRequest from a dict
inventory_create_batches_request_from_dict = InventoryCreateBatchesRequest.from_dict(inventory_create_batches_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


