# WarehouseTransferChangeTransferPropertyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_transfer_id** | **str** | The id of the transfer the property belongs to. | [optional] 
**pk_transfer_property_id** | **str** | The id of the property. | [optional] 
**new_value** | **str** | The new value for the property. | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer.models.warehouse_transfer_change_transfer_property_request import WarehouseTransferChangeTransferPropertyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseTransferChangeTransferPropertyRequest from a JSON string
warehouse_transfer_change_transfer_property_request_instance = WarehouseTransferChangeTransferPropertyRequest.from_json(json)
# print the JSON string representation of the object
print(WarehouseTransferChangeTransferPropertyRequest.to_json())

# convert the object into a dict
warehouse_transfer_change_transfer_property_request_dict = warehouse_transfer_change_transfer_property_request_instance.to_dict()
# create an instance of WarehouseTransferChangeTransferPropertyRequest from a dict
warehouse_transfer_change_transfer_property_request_from_dict = WarehouseTransferChangeTransferPropertyRequest.from_dict(warehouse_transfer_change_transfer_property_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


