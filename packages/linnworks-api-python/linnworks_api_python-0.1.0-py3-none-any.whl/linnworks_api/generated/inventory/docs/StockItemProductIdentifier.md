# StockItemProductIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_id** | **int** |  | [optional] 
**stock_item_id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**modified_date** | **datetime** |  | [optional] 
**modified_user_name** | **str** |  | [optional] 
**site** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.stock_item_product_identifier import StockItemProductIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of StockItemProductIdentifier from a JSON string
stock_item_product_identifier_instance = StockItemProductIdentifier.from_json(json)
# print the JSON string representation of the object
print(StockItemProductIdentifier.to_json())

# convert the object into a dict
stock_item_product_identifier_dict = stock_item_product_identifier_instance.to_dict()
# create an instance of StockItemProductIdentifier from a dict
stock_item_product_identifier_from_dict = StockItemProductIdentifier.from_dict(stock_item_product_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


