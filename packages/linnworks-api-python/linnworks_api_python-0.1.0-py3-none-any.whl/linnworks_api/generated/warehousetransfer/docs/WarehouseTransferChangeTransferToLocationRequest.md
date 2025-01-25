# WarehouseTransferChangeTransferToLocationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_transfer_id** | **str** | The id of the transfer. | [optional] 
**new_location_id** | **str** | The location id which represents the to location. | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer.models.warehouse_transfer_change_transfer_to_location_request import WarehouseTransferChangeTransferToLocationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseTransferChangeTransferToLocationRequest from a JSON string
warehouse_transfer_change_transfer_to_location_request_instance = WarehouseTransferChangeTransferToLocationRequest.from_json(json)
# print the JSON string representation of the object
print(WarehouseTransferChangeTransferToLocationRequest.to_json())

# convert the object into a dict
warehouse_transfer_change_transfer_to_location_request_dict = warehouse_transfer_change_transfer_to_location_request_instance.to_dict()
# create an instance of WarehouseTransferChangeTransferToLocationRequest from a dict
warehouse_transfer_change_transfer_to_location_request_from_dict = WarehouseTransferChangeTransferToLocationRequest.from_dict(warehouse_transfer_change_transfer_to_location_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


