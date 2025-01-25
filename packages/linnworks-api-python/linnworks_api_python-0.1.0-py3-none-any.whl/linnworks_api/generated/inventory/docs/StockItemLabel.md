# StockItemLabel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_item_id** | **str** |  | [optional] 
**item_number** | **str** |  | [optional] 
**item_title** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**bin_rack** | **str** |  | [optional] 
**batch_number** | **str** |  | [optional] 
**batch_inventory_id** | **int** |  | [optional] 
**location_id** | **str** |  | [optional] 
**stock_item_int_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.stock_item_label import StockItemLabel

# TODO update the JSON string below
json = "{}"
# create an instance of StockItemLabel from a JSON string
stock_item_label_instance = StockItemLabel.from_json(json)
# print the JSON string representation of the object
print(StockItemLabel.to_json())

# convert the object into a dict
stock_item_label_dict = stock_item_label_instance.to_dict()
# create an instance of StockItemLabel from a dict
stock_item_label_from_dict = StockItemLabel.from_dict(stock_item_label_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


