# InventoryGetScrapHistoryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**GetScrapHistoryRequest**](GetScrapHistoryRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_get_scrap_history_request import InventoryGetScrapHistoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryGetScrapHistoryRequest from a JSON string
inventory_get_scrap_history_request_instance = InventoryGetScrapHistoryRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryGetScrapHistoryRequest.to_json())

# convert the object into a dict
inventory_get_scrap_history_request_dict = inventory_get_scrap_history_request_instance.to_dict()
# create an instance of InventoryGetScrapHistoryRequest from a dict
inventory_get_scrap_history_request_from_dict = InventoryGetScrapHistoryRequest.from_dict(inventory_get_scrap_history_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


