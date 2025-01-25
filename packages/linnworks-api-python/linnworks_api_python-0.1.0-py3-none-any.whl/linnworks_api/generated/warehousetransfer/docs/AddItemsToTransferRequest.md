# AddItemsToTransferRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transfer_id** | **str** |  | [optional] 
**transfer_items** | [**List[WarehouseTransferItemQuantity]**](WarehouseTransferItemQuantity.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer.models.add_items_to_transfer_request import AddItemsToTransferRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddItemsToTransferRequest from a JSON string
add_items_to_transfer_request_instance = AddItemsToTransferRequest.from_json(json)
# print the JSON string representation of the object
print(AddItemsToTransferRequest.to_json())

# convert the object into a dict
add_items_to_transfer_request_dict = add_items_to_transfer_request_instance.to_dict()
# create an instance of AddItemsToTransferRequest from a dict
add_items_to_transfer_request_from_dict = AddItemsToTransferRequest.from_dict(add_items_to_transfer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


