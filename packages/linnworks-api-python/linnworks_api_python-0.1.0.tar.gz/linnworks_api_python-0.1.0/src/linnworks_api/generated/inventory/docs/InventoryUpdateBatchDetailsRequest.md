# InventoryUpdateBatchDetailsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**UpdateBatchDetailsRequest**](UpdateBatchDetailsRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_update_batch_details_request import InventoryUpdateBatchDetailsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryUpdateBatchDetailsRequest from a JSON string
inventory_update_batch_details_request_instance = InventoryUpdateBatchDetailsRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryUpdateBatchDetailsRequest.to_json())

# convert the object into a dict
inventory_update_batch_details_request_dict = inventory_update_batch_details_request_instance.to_dict()
# create an instance of InventoryUpdateBatchDetailsRequest from a dict
inventory_update_batch_details_request_from_dict = InventoryUpdateBatchDetailsRequest.from_dict(inventory_update_batch_details_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


