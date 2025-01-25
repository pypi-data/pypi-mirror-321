# StockItemComposition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**linked_stock_item_id** | **str** |  | [optional] 
**item_title** | **str** |  | [optional] 
**sku** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**purchase_price** | **float** |  | [optional] 
**inventory_tracking_type** | **int** |  | [optional] 
**dim_height** | **float** |  | [optional] 
**dim_width** | **float** |  | [optional] 
**dim_depth** | **float** |  | [optional] 
**weight** | **float** |  | [optional] 
**package_group_id** | **str** |  | [optional] 
**tax_rate** | **float** |  | [optional] 
**stock_item_id** | **str** |  | [optional] 
**stock_item_int_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.stock_item_composition import StockItemComposition

# TODO update the JSON string below
json = "{}"
# create an instance of StockItemComposition from a JSON string
stock_item_composition_instance = StockItemComposition.from_json(json)
# print the JSON string representation of the object
print(StockItemComposition.to_json())

# convert the object into a dict
stock_item_composition_dict = stock_item_composition_instance.to_dict()
# create an instance of StockItemComposition from a dict
stock_item_composition_from_dict = StockItemComposition.from_dict(stock_item_composition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


