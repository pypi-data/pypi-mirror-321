# CalcOrderItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fk_stock_item_id** | **str** |  | [optional] 
**fk_order_item_id** | **str** |  | [optional] 
**stock_item_int_id** | **int** |  | [optional] 
**sku** | **str** |  | [optional] 
**n_qty** | **int** |  | [optional] 
**item_weight** | **float** |  | [optional] 
**dim_height** | **float** |  | [optional] 
**dim_width** | **float** |  | [optional] 
**dim_depth** | **float** |  | [optional] 
**package_group** | **str** |  | [optional] 
**fk_composite_parent_row_id** | **str** |  | [optional] 
**is_composite_child** | **bool** |  | [optional] [readonly] 
**boxes** | [**List[StockItemBoxConfiguration]**](StockItemBoxConfiguration.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.calc_order_item import CalcOrderItem

# TODO update the JSON string below
json = "{}"
# create an instance of CalcOrderItem from a JSON string
calc_order_item_instance = CalcOrderItem.from_json(json)
# print the JSON string representation of the object
print(CalcOrderItem.to_json())

# convert the object into a dict
calc_order_item_dict = calc_order_item_instance.to_dict()
# create an instance of CalcOrderItem from a dict
calc_order_item_from_dict = CalcOrderItem.from_dict(calc_order_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


