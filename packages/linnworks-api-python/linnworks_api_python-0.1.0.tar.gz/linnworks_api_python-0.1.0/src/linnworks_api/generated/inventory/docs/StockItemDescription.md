# StockItemDescription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_row_id** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**sub_source** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**stock_item_id** | **str** |  | [optional] 
**stock_item_int_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.stock_item_description import StockItemDescription

# TODO update the JSON string below
json = "{}"
# create an instance of StockItemDescription from a JSON string
stock_item_description_instance = StockItemDescription.from_json(json)
# print the JSON string representation of the object
print(StockItemDescription.to_json())

# convert the object into a dict
stock_item_description_dict = stock_item_description_instance.to_dict()
# create an instance of StockItemDescription from a dict
stock_item_description_from_dict = StockItemDescription.from_dict(stock_item_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


