# WarehouseTransferSetReferenceNumberRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_transfer_id** | **str** | The transfer id of the transfer to change the reference number of. | [optional] 
**reference_number** | **str** | The new reference number. | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer.models.warehouse_transfer_set_reference_number_request import WarehouseTransferSetReferenceNumberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseTransferSetReferenceNumberRequest from a JSON string
warehouse_transfer_set_reference_number_request_instance = WarehouseTransferSetReferenceNumberRequest.from_json(json)
# print the JSON string representation of the object
print(WarehouseTransferSetReferenceNumberRequest.to_json())

# convert the object into a dict
warehouse_transfer_set_reference_number_request_dict = warehouse_transfer_set_reference_number_request_instance.to_dict()
# create an instance of WarehouseTransferSetReferenceNumberRequest from a dict
warehouse_transfer_set_reference_number_request_from_dict = WarehouseTransferSetReferenceNumberRequest.from_dict(warehouse_transfer_set_reference_number_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


