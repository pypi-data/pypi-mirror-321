# WarehouseTransferModel

Transfer model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_date** | **datetime** | The date that transfer is created | [optional] 
**from_location_id** | **str** | The location id that transfer is from | [optional] 
**reference_number** | **str** | Transfer unique reference number | [optional] 
**status** | [**TransferStatus**](TransferStatus.md) |  | [optional] 
**to_location_id** | **str** | The location id that transfer is to | [optional] 
**transfer_id** | **int** | Transfer unique id | [optional] 
**transfer_type** | [**TransferType**](TransferType.md) |  | [optional] 
**update_date** | **datetime** | The date that transfer is last updated | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_v2.models.warehouse_transfer_model import WarehouseTransferModel

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseTransferModel from a JSON string
warehouse_transfer_model_instance = WarehouseTransferModel.from_json(json)
# print the JSON string representation of the object
print(WarehouseTransferModel.to_json())

# convert the object into a dict
warehouse_transfer_model_dict = warehouse_transfer_model_instance.to_dict()
# create an instance of WarehouseTransferModel from a dict
warehouse_transfer_model_from_dict = WarehouseTransferModel.from_dict(warehouse_transfer_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


