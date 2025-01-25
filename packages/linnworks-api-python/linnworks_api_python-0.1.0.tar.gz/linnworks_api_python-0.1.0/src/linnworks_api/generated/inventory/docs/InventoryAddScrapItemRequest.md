# InventoryAddScrapItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**AddScrapItemRequest**](AddScrapItemRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_add_scrap_item_request import InventoryAddScrapItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryAddScrapItemRequest from a JSON string
inventory_add_scrap_item_request_instance = InventoryAddScrapItemRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryAddScrapItemRequest.to_json())

# convert the object into a dict
inventory_add_scrap_item_request_dict = inventory_add_scrap_item_request_instance.to_dict()
# create an instance of InventoryAddScrapItemRequest from a dict
inventory_add_scrap_item_request_from_dict = InventoryAddScrapItemRequest.from_dict(inventory_add_scrap_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


