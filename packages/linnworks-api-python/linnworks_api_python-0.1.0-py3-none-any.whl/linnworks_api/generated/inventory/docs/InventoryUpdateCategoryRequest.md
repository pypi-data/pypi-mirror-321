# InventoryUpdateCategoryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | [**LinnworksCategory**](LinnworksCategory.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_update_category_request import InventoryUpdateCategoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryUpdateCategoryRequest from a JSON string
inventory_update_category_request_instance = InventoryUpdateCategoryRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryUpdateCategoryRequest.to_json())

# convert the object into a dict
inventory_update_category_request_dict = inventory_update_category_request_instance.to_dict()
# create an instance of InventoryUpdateCategoryRequest from a dict
inventory_update_category_request_from_dict = InventoryUpdateCategoryRequest.from_dict(inventory_update_category_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


