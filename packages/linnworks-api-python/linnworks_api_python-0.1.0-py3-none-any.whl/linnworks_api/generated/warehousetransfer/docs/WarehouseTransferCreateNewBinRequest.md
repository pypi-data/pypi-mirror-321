# WarehouseTransferCreateNewBinRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_transfer_id** | **str** | The transfer to create the bin for. | [optional] 
**barcode** | **str** | The barcode of the bin. | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer.models.warehouse_transfer_create_new_bin_request import WarehouseTransferCreateNewBinRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseTransferCreateNewBinRequest from a JSON string
warehouse_transfer_create_new_bin_request_instance = WarehouseTransferCreateNewBinRequest.from_json(json)
# print the JSON string representation of the object
print(WarehouseTransferCreateNewBinRequest.to_json())

# convert the object into a dict
warehouse_transfer_create_new_bin_request_dict = warehouse_transfer_create_new_bin_request_instance.to_dict()
# create an instance of WarehouseTransferCreateNewBinRequest from a dict
warehouse_transfer_create_new_bin_request_from_dict = WarehouseTransferCreateNewBinRequest.from_dict(warehouse_transfer_create_new_bin_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


