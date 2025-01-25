# WarehouseTransferChangeTransferItemReceivedQuantityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_transfer_id** | **str** | The id of the transfer. | [optional] 
**pk_bin_id** | **str** | The id of the bin. | [optional] 
**pk_transfer_item_id** | **str** | The id of the bin item. | [optional] 
**quantity** | **int** | The new quantity. | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer.models.warehouse_transfer_change_transfer_item_received_quantity_request import WarehouseTransferChangeTransferItemReceivedQuantityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseTransferChangeTransferItemReceivedQuantityRequest from a JSON string
warehouse_transfer_change_transfer_item_received_quantity_request_instance = WarehouseTransferChangeTransferItemReceivedQuantityRequest.from_json(json)
# print the JSON string representation of the object
print(WarehouseTransferChangeTransferItemReceivedQuantityRequest.to_json())

# convert the object into a dict
warehouse_transfer_change_transfer_item_received_quantity_request_dict = warehouse_transfer_change_transfer_item_received_quantity_request_instance.to_dict()
# create an instance of WarehouseTransferChangeTransferItemReceivedQuantityRequest from a dict
warehouse_transfer_change_transfer_item_received_quantity_request_from_dict = WarehouseTransferChangeTransferItemReceivedQuantityRequest.from_dict(warehouse_transfer_change_transfer_item_received_quantity_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


