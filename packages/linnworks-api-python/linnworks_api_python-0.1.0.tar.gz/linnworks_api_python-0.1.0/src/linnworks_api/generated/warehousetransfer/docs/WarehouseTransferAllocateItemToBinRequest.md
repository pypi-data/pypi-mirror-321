# WarehouseTransferAllocateItemToBinRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_src_bin_id** | **str** | The id of the source bin. | [optional] 
**pk_dst_bin_id** | **str** | The id of the destination bin. | [optional] 
**pk_transfer_item_id** | **str** | The transfer item to be reallocated. | [optional] 
**quantity** | **int** | The quantity to reallocate. | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer.models.warehouse_transfer_allocate_item_to_bin_request import WarehouseTransferAllocateItemToBinRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseTransferAllocateItemToBinRequest from a JSON string
warehouse_transfer_allocate_item_to_bin_request_instance = WarehouseTransferAllocateItemToBinRequest.from_json(json)
# print the JSON string representation of the object
print(WarehouseTransferAllocateItemToBinRequest.to_json())

# convert the object into a dict
warehouse_transfer_allocate_item_to_bin_request_dict = warehouse_transfer_allocate_item_to_bin_request_instance.to_dict()
# create an instance of WarehouseTransferAllocateItemToBinRequest from a dict
warehouse_transfer_allocate_item_to_bin_request_from_dict = WarehouseTransferAllocateItemToBinRequest.from_dict(warehouse_transfer_allocate_item_to_bin_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


