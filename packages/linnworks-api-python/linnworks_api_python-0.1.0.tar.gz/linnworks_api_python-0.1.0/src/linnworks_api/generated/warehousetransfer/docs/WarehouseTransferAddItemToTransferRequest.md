# WarehouseTransferAddItemToTransferRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fk_transfer_id** | **str** | fkTransferId | [optional] 
**pk_stock_item_id** | **str** | pkStockItemId | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer.models.warehouse_transfer_add_item_to_transfer_request import WarehouseTransferAddItemToTransferRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseTransferAddItemToTransferRequest from a JSON string
warehouse_transfer_add_item_to_transfer_request_instance = WarehouseTransferAddItemToTransferRequest.from_json(json)
# print the JSON string representation of the object
print(WarehouseTransferAddItemToTransferRequest.to_json())

# convert the object into a dict
warehouse_transfer_add_item_to_transfer_request_dict = warehouse_transfer_add_item_to_transfer_request_instance.to_dict()
# create an instance of WarehouseTransferAddItemToTransferRequest from a dict
warehouse_transfer_add_item_to_transfer_request_from_dict = WarehouseTransferAddItemToTransferRequest.from_dict(warehouse_transfer_add_item_to_transfer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


