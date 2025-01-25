# GenericPagedResultWarehouseTransfer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_number** | **int** |  | [optional] 
**entries_per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] [readonly] 
**data** | [**List[WarehouseTransfer]**](WarehouseTransfer.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer.models.generic_paged_result_warehouse_transfer import GenericPagedResultWarehouseTransfer

# TODO update the JSON string below
json = "{}"
# create an instance of GenericPagedResultWarehouseTransfer from a JSON string
generic_paged_result_warehouse_transfer_instance = GenericPagedResultWarehouseTransfer.from_json(json)
# print the JSON string representation of the object
print(GenericPagedResultWarehouseTransfer.to_json())

# convert the object into a dict
generic_paged_result_warehouse_transfer_dict = generic_paged_result_warehouse_transfer_instance.to_dict()
# create an instance of GenericPagedResultWarehouseTransfer from a dict
generic_paged_result_warehouse_transfer_from_dict = GenericPagedResultWarehouseTransfer.from_dict(generic_paged_result_warehouse_transfer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


