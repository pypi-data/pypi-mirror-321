# InventoryAddScrapCategoriesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**AddScrapCategoriesRequest**](AddScrapCategoriesRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_add_scrap_categories_request import InventoryAddScrapCategoriesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryAddScrapCategoriesRequest from a JSON string
inventory_add_scrap_categories_request_instance = InventoryAddScrapCategoriesRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryAddScrapCategoriesRequest.to_json())

# convert the object into a dict
inventory_add_scrap_categories_request_dict = inventory_add_scrap_categories_request_instance.to_dict()
# create an instance of InventoryAddScrapCategoriesRequest from a dict
inventory_add_scrap_categories_request_from_dict = InventoryAddScrapCategoriesRequest.from_dict(inventory_add_scrap_categories_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


