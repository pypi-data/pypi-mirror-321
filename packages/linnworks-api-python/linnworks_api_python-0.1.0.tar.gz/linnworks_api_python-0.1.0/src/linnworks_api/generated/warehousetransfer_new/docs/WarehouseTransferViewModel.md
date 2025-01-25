# WarehouseTransferViewModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_transfer_id** | **int** |  | [optional] 
**from_location_id** | **str** |  | [optional] 
**to_location_id** | **str** |  | [optional] 
**from_location** | **str** |  | [optional] 
**to_location** | **str** |  | [optional] 
**status** | [**TransferStatus**](TransferStatus.md) |  | [optional] 
**transfer_type** | [**TransferType**](TransferType.md) |  | [optional] 
**reference_number** | **str** |  | [optional] 
**create_date** | **datetime** |  | [optional] 
**update_date** | **datetime** |  | [optional] 
**number_of_items** | **int** |  | [optional] 
**total_requested_quantity** | **int** |  | [optional] 
**total_received_quantity** | **int** |  | [optional] 
**total_sent_quantity** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.warehouse_transfer_view_model import WarehouseTransferViewModel

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseTransferViewModel from a JSON string
warehouse_transfer_view_model_instance = WarehouseTransferViewModel.from_json(json)
# print the JSON string representation of the object
print(WarehouseTransferViewModel.to_json())

# convert the object into a dict
warehouse_transfer_view_model_dict = warehouse_transfer_view_model_instance.to_dict()
# create an instance of WarehouseTransferViewModel from a dict
warehouse_transfer_view_model_from_dict = WarehouseTransferViewModel.from_dict(warehouse_transfer_view_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


