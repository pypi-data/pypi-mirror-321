# InventoryStockLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_location_id** | **str** |  | [optional] 
**stock_location_int_id** | **int** |  | [optional] 
**location_name** | **str** |  | [optional] 
**location_tag** | **str** |  | [optional] 
**is_fulfillment_center** | **bool** |  | [optional] 
**is_warehouse_managed** | **bool** |  | [optional] 
**bin_rack** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.inventory_stock_location import InventoryStockLocation

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryStockLocation from a JSON string
inventory_stock_location_instance = InventoryStockLocation.from_json(json)
# print the JSON string representation of the object
print(InventoryStockLocation.to_json())

# convert the object into a dict
inventory_stock_location_dict = inventory_stock_location_instance.to_dict()
# create an instance of InventoryStockLocation from a dict
inventory_stock_location_from_dict = InventoryStockLocation.from_dict(inventory_stock_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


