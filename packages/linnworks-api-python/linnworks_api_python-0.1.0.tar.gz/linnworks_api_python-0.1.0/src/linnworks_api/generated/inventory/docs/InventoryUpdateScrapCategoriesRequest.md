# InventoryUpdateScrapCategoriesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**UpdateScrapCategoriesRequest**](UpdateScrapCategoriesRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_update_scrap_categories_request import InventoryUpdateScrapCategoriesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryUpdateScrapCategoriesRequest from a JSON string
inventory_update_scrap_categories_request_instance = InventoryUpdateScrapCategoriesRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryUpdateScrapCategoriesRequest.to_json())

# convert the object into a dict
inventory_update_scrap_categories_request_dict = inventory_update_scrap_categories_request_instance.to_dict()
# create an instance of InventoryUpdateScrapCategoriesRequest from a dict
inventory_update_scrap_categories_request_from_dict = InventoryUpdateScrapCategoriesRequest.from_dict(inventory_update_scrap_categories_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


