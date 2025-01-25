# InventoryDeleteBatchInventoryInBulkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_inventory_ids** | **List[int]** | List of batch inventory ids | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_delete_batch_inventory_in_bulk_request import InventoryDeleteBatchInventoryInBulkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryDeleteBatchInventoryInBulkRequest from a JSON string
inventory_delete_batch_inventory_in_bulk_request_instance = InventoryDeleteBatchInventoryInBulkRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryDeleteBatchInventoryInBulkRequest.to_json())

# convert the object into a dict
inventory_delete_batch_inventory_in_bulk_request_dict = inventory_delete_batch_inventory_in_bulk_request_instance.to_dict()
# create an instance of InventoryDeleteBatchInventoryInBulkRequest from a dict
inventory_delete_batch_inventory_in_bulk_request_from_dict = InventoryDeleteBatchInventoryInBulkRequest.from_dict(inventory_delete_batch_inventory_in_bulk_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


