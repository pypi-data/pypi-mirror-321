# StockItemImage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | [optional] 
**full_source** | **str** |  | [optional] 
**check_sum_value** | **str** |  | [optional] 
**pk_row_id** | **str** |  | [optional] 
**is_main** | **bool** |  | [optional] 
**sort_order** | **int** |  | [optional] 
**checksum_value** | **str** |  | [optional] 
**raw_checksum** | **str** |  | [optional] 
**stock_item_id** | **str** |  | [optional] 
**stock_item_int_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.stock_item_image import StockItemImage

# TODO update the JSON string below
json = "{}"
# create an instance of StockItemImage from a JSON string
stock_item_image_instance = StockItemImage.from_json(json)
# print the JSON string representation of the object
print(StockItemImage.to_json())

# convert the object into a dict
stock_item_image_dict = stock_item_image_instance.to_dict()
# create an instance of StockItemImage from a dict
stock_item_image_from_dict = StockItemImage.from_dict(stock_item_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


