# InventoryDeleteCategoryByIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_id** | **str** | Unique id that identifies the category that you want to delete. | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_delete_category_by_id_request import InventoryDeleteCategoryByIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryDeleteCategoryByIdRequest from a JSON string
inventory_delete_category_by_id_request_instance = InventoryDeleteCategoryByIdRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryDeleteCategoryByIdRequest.to_json())

# convert the object into a dict
inventory_delete_category_by_id_request_dict = inventory_delete_category_by_id_request_instance.to_dict()
# create an instance of InventoryDeleteCategoryByIdRequest from a dict
inventory_delete_category_by_id_request_from_dict = InventoryDeleteCategoryByIdRequest.from_dict(inventory_delete_category_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


