# StockItemTypeInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sku** | **str** |  | [optional] 
**stock_item_int_id** | **int** |  | [optional] 
**stock_item_id** | **str** |  | [optional] 
**is_variation_group** | **bool** |  | [optional] 
**is_composite_parent** | **bool** |  | [optional] 
**is_archived** | **bool** |  | [optional] 
**inventory_tracking_type** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.stock_item_type_info import StockItemTypeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of StockItemTypeInfo from a JSON string
stock_item_type_info_instance = StockItemTypeInfo.from_json(json)
# print the JSON string representation of the object
print(StockItemTypeInfo.to_json())

# convert the object into a dict
stock_item_type_info_dict = stock_item_type_info_instance.to_dict()
# create an instance of StockItemTypeInfo from a dict
stock_item_type_info_from_dict = StockItemTypeInfo.from_dict(stock_item_type_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


