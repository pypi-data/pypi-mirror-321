# StockItemExtendedPropertyWithSku


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_number** | **str** | The ItemNumber (SKU) of the item  This is used to calculate the StockItemId if it has been omitted | [optional] 
**pk_row_id** | **str** |  | [optional] 
**fk_stock_item_id** | **str** |  | [optional] 
**propery_name** | **str** |  | [optional] 
**property_value** | **str** |  | [optional] 
**property_type** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.stock_item_extended_property_with_sku import StockItemExtendedPropertyWithSku

# TODO update the JSON string below
json = "{}"
# create an instance of StockItemExtendedPropertyWithSku from a JSON string
stock_item_extended_property_with_sku_instance = StockItemExtendedPropertyWithSku.from_json(json)
# print the JSON string representation of the object
print(StockItemExtendedPropertyWithSku.to_json())

# convert the object into a dict
stock_item_extended_property_with_sku_dict = stock_item_extended_property_with_sku_instance.to_dict()
# create an instance of StockItemExtendedPropertyWithSku from a dict
stock_item_extended_property_with_sku_from_dict = StockItemExtendedPropertyWithSku.from_dict(stock_item_extended_property_with_sku_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


