# GetBatchesByWarehouseTransferIdResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batches** | [**List[StockItemBatchResponse]**](StockItemBatchResponse.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.get_batches_by_warehouse_transfer_id_response import GetBatchesByWarehouseTransferIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetBatchesByWarehouseTransferIdResponse from a JSON string
get_batches_by_warehouse_transfer_id_response_instance = GetBatchesByWarehouseTransferIdResponse.from_json(json)
# print the JSON string representation of the object
print(GetBatchesByWarehouseTransferIdResponse.to_json())

# convert the object into a dict
get_batches_by_warehouse_transfer_id_response_dict = get_batches_by_warehouse_transfer_id_response_instance.to_dict()
# create an instance of GetBatchesByWarehouseTransferIdResponse from a dict
get_batches_by_warehouse_transfer_id_response_from_dict = GetBatchesByWarehouseTransferIdResponse.from_dict(get_batches_by_warehouse_transfer_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


