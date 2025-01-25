# InventoryUpdateCompositeParentStockLevelRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_item_id** | **str** | Stock item id | [optional] 
**location_id** | **str** | Stock location id | [optional] 
**field_value** | **int** | Stock tracked status | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_update_composite_parent_stock_level_request import InventoryUpdateCompositeParentStockLevelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryUpdateCompositeParentStockLevelRequest from a JSON string
inventory_update_composite_parent_stock_level_request_instance = InventoryUpdateCompositeParentStockLevelRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryUpdateCompositeParentStockLevelRequest.to_json())

# convert the object into a dict
inventory_update_composite_parent_stock_level_request_dict = inventory_update_composite_parent_stock_level_request_instance.to_dict()
# create an instance of InventoryUpdateCompositeParentStockLevelRequest from a dict
inventory_update_composite_parent_stock_level_request_from_dict = InventoryUpdateCompositeParentStockLevelRequest.from_dict(inventory_update_composite_parent_stock_level_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


