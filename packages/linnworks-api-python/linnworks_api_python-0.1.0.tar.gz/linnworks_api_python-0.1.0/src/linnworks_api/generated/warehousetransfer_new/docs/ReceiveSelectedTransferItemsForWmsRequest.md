# ReceiveSelectedTransferItemsForWmsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binrack_id** | **int** |  | [optional] 
**transfer_id** | **int** |  | [optional] 
**transfer_item_ids** | **List[int]** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.receive_selected_transfer_items_for_wms_request import ReceiveSelectedTransferItemsForWmsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReceiveSelectedTransferItemsForWmsRequest from a JSON string
receive_selected_transfer_items_for_wms_request_instance = ReceiveSelectedTransferItemsForWmsRequest.from_json(json)
# print the JSON string representation of the object
print(ReceiveSelectedTransferItemsForWmsRequest.to_json())

# convert the object into a dict
receive_selected_transfer_items_for_wms_request_dict = receive_selected_transfer_items_for_wms_request_instance.to_dict()
# create an instance of ReceiveSelectedTransferItemsForWmsRequest from a dict
receive_selected_transfer_items_for_wms_request_from_dict = ReceiveSelectedTransferItemsForWmsRequest.from_dict(receive_selected_transfer_items_for_wms_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


