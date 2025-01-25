# InventoryGetInventoryItemBatchInformationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**GetInventoryItemBatchInformationRequest**](GetInventoryItemBatchInformationRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_get_inventory_item_batch_information_request import InventoryGetInventoryItemBatchInformationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryGetInventoryItemBatchInformationRequest from a JSON string
inventory_get_inventory_item_batch_information_request_instance = InventoryGetInventoryItemBatchInformationRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryGetInventoryItemBatchInformationRequest.to_json())

# convert the object into a dict
inventory_get_inventory_item_batch_information_request_dict = inventory_get_inventory_item_batch_information_request_instance.to_dict()
# create an instance of InventoryGetInventoryItemBatchInformationRequest from a dict
inventory_get_inventory_item_batch_information_request_from_dict = InventoryGetInventoryItemBatchInformationRequest.from_dict(inventory_get_inventory_item_batch_information_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


