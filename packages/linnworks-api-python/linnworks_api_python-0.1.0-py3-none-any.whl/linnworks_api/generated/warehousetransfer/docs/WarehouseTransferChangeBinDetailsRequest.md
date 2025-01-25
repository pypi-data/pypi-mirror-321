# WarehouseTransferChangeBinDetailsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_transfer_id** | **str** | The id of the transfer the bin belongs to. | [optional] 
**pk_bin_id** | **str** | The id of the bin. | [optional] 
**bin_name** | **str** | The new name for the bin (pass an empty string if no change is required). | [optional] 
**bin_reference** | **str** | The new reference for the bin (pass an empty string if no change is required). | [optional] 
**bin_barcode** | **str** | The new barcode for the bin  (pass an empty string if no change is required). | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer.models.warehouse_transfer_change_bin_details_request import WarehouseTransferChangeBinDetailsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseTransferChangeBinDetailsRequest from a JSON string
warehouse_transfer_change_bin_details_request_instance = WarehouseTransferChangeBinDetailsRequest.from_json(json)
# print the JSON string representation of the object
print(WarehouseTransferChangeBinDetailsRequest.to_json())

# convert the object into a dict
warehouse_transfer_change_bin_details_request_dict = warehouse_transfer_change_bin_details_request_instance.to_dict()
# create an instance of WarehouseTransferChangeBinDetailsRequest from a dict
warehouse_transfer_change_bin_details_request_from_dict = WarehouseTransferChangeBinDetailsRequest.from_dict(warehouse_transfer_change_bin_details_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


