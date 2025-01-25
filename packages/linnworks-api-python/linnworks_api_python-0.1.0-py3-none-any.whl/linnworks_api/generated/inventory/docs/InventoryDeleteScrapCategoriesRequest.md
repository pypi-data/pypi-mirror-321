# InventoryDeleteScrapCategoriesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**DeleteScrapCategoriesRequest**](DeleteScrapCategoriesRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_delete_scrap_categories_request import InventoryDeleteScrapCategoriesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryDeleteScrapCategoriesRequest from a JSON string
inventory_delete_scrap_categories_request_instance = InventoryDeleteScrapCategoriesRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryDeleteScrapCategoriesRequest.to_json())

# convert the object into a dict
inventory_delete_scrap_categories_request_dict = inventory_delete_scrap_categories_request_instance.to_dict()
# create an instance of InventoryDeleteScrapCategoriesRequest from a dict
inventory_delete_scrap_categories_request_from_dict = InventoryDeleteScrapCategoriesRequest.from_dict(inventory_delete_scrap_categories_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


