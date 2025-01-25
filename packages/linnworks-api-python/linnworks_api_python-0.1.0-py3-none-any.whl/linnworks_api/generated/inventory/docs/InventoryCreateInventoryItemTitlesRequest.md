# InventoryCreateInventoryItemTitlesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory_item_titles** | [**List[StockItemTitle]**](StockItemTitle.md) | list of stockitem Titles | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_create_inventory_item_titles_request import InventoryCreateInventoryItemTitlesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryCreateInventoryItemTitlesRequest from a JSON string
inventory_create_inventory_item_titles_request_instance = InventoryCreateInventoryItemTitlesRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryCreateInventoryItemTitlesRequest.to_json())

# convert the object into a dict
inventory_create_inventory_item_titles_request_dict = inventory_create_inventory_item_titles_request_instance.to_dict()
# create an instance of InventoryCreateInventoryItemTitlesRequest from a dict
inventory_create_inventory_item_titles_request_from_dict = InventoryCreateInventoryItemTitlesRequest.from_dict(inventory_create_inventory_item_titles_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


