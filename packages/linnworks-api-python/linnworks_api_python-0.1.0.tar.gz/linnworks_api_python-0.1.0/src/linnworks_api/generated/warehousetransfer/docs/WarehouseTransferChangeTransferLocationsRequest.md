# WarehouseTransferChangeTransferLocationsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_transfer_id** | **str** | The id of the transfer. | [optional] 
**from_location_id** | **str** | The location id which represents the from location. | [optional] 
**to_location_id** | **str** | The location id which represents the to location. | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer.models.warehouse_transfer_change_transfer_locations_request import WarehouseTransferChangeTransferLocationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseTransferChangeTransferLocationsRequest from a JSON string
warehouse_transfer_change_transfer_locations_request_instance = WarehouseTransferChangeTransferLocationsRequest.from_json(json)
# print the JSON string representation of the object
print(WarehouseTransferChangeTransferLocationsRequest.to_json())

# convert the object into a dict
warehouse_transfer_change_transfer_locations_request_dict = warehouse_transfer_change_transfer_locations_request_instance.to_dict()
# create an instance of WarehouseTransferChangeTransferLocationsRequest from a dict
warehouse_transfer_change_transfer_locations_request_from_dict = WarehouseTransferChangeTransferLocationsRequest.from_dict(warehouse_transfer_change_transfer_locations_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


