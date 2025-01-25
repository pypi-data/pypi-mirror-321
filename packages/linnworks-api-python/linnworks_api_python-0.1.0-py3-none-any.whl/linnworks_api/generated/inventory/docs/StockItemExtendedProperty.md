# StockItemExtendedProperty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_row_id** | **str** |  | [optional] 
**fk_stock_item_id** | **str** |  | [optional] 
**propery_name** | **str** |  | [optional] 
**property_value** | **str** |  | [optional] 
**property_type** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.stock_item_extended_property import StockItemExtendedProperty

# TODO update the JSON string below
json = "{}"
# create an instance of StockItemExtendedProperty from a JSON string
stock_item_extended_property_instance = StockItemExtendedProperty.from_json(json)
# print the JSON string representation of the object
print(StockItemExtendedProperty.to_json())

# convert the object into a dict
stock_item_extended_property_dict = stock_item_extended_property_instance.to_dict()
# create an instance of StockItemExtendedProperty from a dict
stock_item_extended_property_from_dict = StockItemExtendedProperty.from_dict(stock_item_extended_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


