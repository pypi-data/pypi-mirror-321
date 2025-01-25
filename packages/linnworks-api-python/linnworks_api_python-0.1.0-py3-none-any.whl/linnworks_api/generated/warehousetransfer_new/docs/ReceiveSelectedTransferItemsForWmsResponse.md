# ReceiveSelectedTransferItemsForWmsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[ItemReceiveResult]**](ItemReceiveResult.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.receive_selected_transfer_items_for_wms_response import ReceiveSelectedTransferItemsForWmsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReceiveSelectedTransferItemsForWmsResponse from a JSON string
receive_selected_transfer_items_for_wms_response_instance = ReceiveSelectedTransferItemsForWmsResponse.from_json(json)
# print the JSON string representation of the object
print(ReceiveSelectedTransferItemsForWmsResponse.to_json())

# convert the object into a dict
receive_selected_transfer_items_for_wms_response_dict = receive_selected_transfer_items_for_wms_response_instance.to_dict()
# create an instance of ReceiveSelectedTransferItemsForWmsResponse from a dict
receive_selected_transfer_items_for_wms_response_from_dict = ReceiveSelectedTransferItemsForWmsResponse.from_dict(receive_selected_transfer_items_for_wms_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


