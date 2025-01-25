# StockItemImageSimple


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_row_id** | **str** |  | [optional] 
**is_main** | **bool** |  | [optional] 
**sort_order** | **int** |  | [optional] 
**checksum_value** | **str** |  | [optional] 
**raw_checksum** | **str** |  | [optional] 
**stock_item_id** | **str** |  | [optional] 
**stock_item_int_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.stock_item_image_simple import StockItemImageSimple

# TODO update the JSON string below
json = "{}"
# create an instance of StockItemImageSimple from a JSON string
stock_item_image_simple_instance = StockItemImageSimple.from_json(json)
# print the JSON string representation of the object
print(StockItemImageSimple.to_json())

# convert the object into a dict
stock_item_image_simple_dict = stock_item_image_simple_instance.to_dict()
# create an instance of StockItemImageSimple from a dict
stock_item_image_simple_from_dict = StockItemImageSimple.from_dict(stock_item_image_simple_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


