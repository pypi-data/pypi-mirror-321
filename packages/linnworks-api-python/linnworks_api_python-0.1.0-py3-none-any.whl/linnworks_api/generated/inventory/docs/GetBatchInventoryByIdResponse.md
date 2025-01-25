# GetBatchInventoryByIdResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batches** | [**List[StockItemBatch]**](StockItemBatch.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.get_batch_inventory_by_id_response import GetBatchInventoryByIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetBatchInventoryByIdResponse from a JSON string
get_batch_inventory_by_id_response_instance = GetBatchInventoryByIdResponse.from_json(json)
# print the JSON string representation of the object
print(GetBatchInventoryByIdResponse.to_json())

# convert the object into a dict
get_batch_inventory_by_id_response_dict = get_batch_inventory_by_id_response_instance.to_dict()
# create an instance of GetBatchInventoryByIdResponse from a dict
get_batch_inventory_by_id_response_from_dict = GetBatchInventoryByIdResponse.from_dict(get_batch_inventory_by_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


