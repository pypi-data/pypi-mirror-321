# WarehouseTransferDeleteTransferPropertyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_transfer_id** | **str** | pkTransferId | [optional] 
**pk_transfer_property_id** | **str** | pkTransferPropertyId | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer.models.warehouse_transfer_delete_transfer_property_request import WarehouseTransferDeleteTransferPropertyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseTransferDeleteTransferPropertyRequest from a JSON string
warehouse_transfer_delete_transfer_property_request_instance = WarehouseTransferDeleteTransferPropertyRequest.from_json(json)
# print the JSON string representation of the object
print(WarehouseTransferDeleteTransferPropertyRequest.to_json())

# convert the object into a dict
warehouse_transfer_delete_transfer_property_request_dict = warehouse_transfer_delete_transfer_property_request_instance.to_dict()
# create an instance of WarehouseTransferDeleteTransferPropertyRequest from a dict
warehouse_transfer_delete_transfer_property_request_from_dict = WarehouseTransferDeleteTransferPropertyRequest.from_dict(warehouse_transfer_delete_transfer_property_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


