# InventoryCreateCategoryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_name** | **str** | Category name | [optional] 
**category_id** | **str** | Category id (optional) | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_create_category_request import InventoryCreateCategoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryCreateCategoryRequest from a JSON string
inventory_create_category_request_instance = InventoryCreateCategoryRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryCreateCategoryRequest.to_json())

# convert the object into a dict
inventory_create_category_request_dict = inventory_create_category_request_instance.to_dict()
# create an instance of InventoryCreateCategoryRequest from a dict
inventory_create_category_request_from_dict = InventoryCreateCategoryRequest.from_dict(inventory_create_category_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


