# AddItemsToTransferResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transfer_items** | [**List[WarehouseTransferItem]**](WarehouseTransferItem.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer.models.add_items_to_transfer_response import AddItemsToTransferResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddItemsToTransferResponse from a JSON string
add_items_to_transfer_response_instance = AddItemsToTransferResponse.from_json(json)
# print the JSON string representation of the object
print(AddItemsToTransferResponse.to_json())

# convert the object into a dict
add_items_to_transfer_response_dict = add_items_to_transfer_response_instance.to_dict()
# create an instance of AddItemsToTransferResponse from a dict
add_items_to_transfer_response_from_dict = AddItemsToTransferResponse.from_dict(add_items_to_transfer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


