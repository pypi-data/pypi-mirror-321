# StockItemExtendedPropertyUpsertItem

Stock item extended property

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fk_stock_item_id** | **str** | Stock Item ID, optional if SKU provided | [optional] 
**sku** | **str** | Stock Item ID, optional if fkStockItemId provided | [optional] 
**propery_name** | **str** | Property name | [optional] 
**property_value** | **str** | Property value | [optional] 
**property_type** | **str** | Property type | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.stock_item_extended_property_upsert_item import StockItemExtendedPropertyUpsertItem

# TODO update the JSON string below
json = "{}"
# create an instance of StockItemExtendedPropertyUpsertItem from a JSON string
stock_item_extended_property_upsert_item_instance = StockItemExtendedPropertyUpsertItem.from_json(json)
# print the JSON string representation of the object
print(StockItemExtendedPropertyUpsertItem.to_json())

# convert the object into a dict
stock_item_extended_property_upsert_item_dict = stock_item_extended_property_upsert_item_instance.to_dict()
# create an instance of StockItemExtendedPropertyUpsertItem from a dict
stock_item_extended_property_upsert_item_from_dict = StockItemExtendedPropertyUpsertItem.from_dict(stock_item_extended_property_upsert_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


