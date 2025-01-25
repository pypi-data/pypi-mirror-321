# StockItemIdentifier

Stock item identifiers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_item_id** | **str** | Stock item id | [optional] 
**type** | **str** | Product identifier type | [optional] 
**value** | **str** | Product identifier | [optional] 

## Example

```python
from linnworks_api.generated.picking.models.stock_item_identifier import StockItemIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of StockItemIdentifier from a JSON string
stock_item_identifier_instance = StockItemIdentifier.from_json(json)
# print the JSON string representation of the object
print(StockItemIdentifier.to_json())

# convert the object into a dict
stock_item_identifier_dict = stock_item_identifier_instance.to_dict()
# create an instance of StockItemIdentifier from a dict
stock_item_identifier_from_dict = StockItemIdentifier.from_dict(stock_item_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


