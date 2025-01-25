# InventoryDeleteInventoryItemTitlesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory_item_title_ids** | **List[str]** | list of stockitem Titles | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_delete_inventory_item_titles_request import InventoryDeleteInventoryItemTitlesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryDeleteInventoryItemTitlesRequest from a JSON string
inventory_delete_inventory_item_titles_request_instance = InventoryDeleteInventoryItemTitlesRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryDeleteInventoryItemTitlesRequest.to_json())

# convert the object into a dict
inventory_delete_inventory_item_titles_request_dict = inventory_delete_inventory_item_titles_request_instance.to_dict()
# create an instance of InventoryDeleteInventoryItemTitlesRequest from a dict
inventory_delete_inventory_item_titles_request_from_dict = InventoryDeleteInventoryItemTitlesRequest.from_dict(inventory_delete_inventory_item_titles_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


