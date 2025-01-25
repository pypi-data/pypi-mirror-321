# GetBatchInventoryByIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_inventory_ids** | **List[int]** |  | [optional] 
**load_related_inventory_lines** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.get_batch_inventory_by_id_request import GetBatchInventoryByIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetBatchInventoryByIdRequest from a JSON string
get_batch_inventory_by_id_request_instance = GetBatchInventoryByIdRequest.from_json(json)
# print the JSON string representation of the object
print(GetBatchInventoryByIdRequest.to_json())

# convert the object into a dict
get_batch_inventory_by_id_request_dict = get_batch_inventory_by_id_request_instance.to_dict()
# create an instance of GetBatchInventoryByIdRequest from a dict
get_batch_inventory_by_id_request_from_dict = GetBatchInventoryByIdRequest.from_dict(get_batch_inventory_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


