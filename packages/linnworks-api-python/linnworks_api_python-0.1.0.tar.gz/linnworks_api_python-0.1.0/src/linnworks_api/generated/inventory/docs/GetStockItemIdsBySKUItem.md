# GetStockItemIdsBySKUItem

Response item of StockItemId and SKU

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_item_id** | **str** |  | [optional] 
**sku** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.get_stock_item_ids_by_sku_item import GetStockItemIdsBySKUItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetStockItemIdsBySKUItem from a JSON string
get_stock_item_ids_by_sku_item_instance = GetStockItemIdsBySKUItem.from_json(json)
# print the JSON string representation of the object
print(GetStockItemIdsBySKUItem.to_json())

# convert the object into a dict
get_stock_item_ids_by_sku_item_dict = get_stock_item_ids_by_sku_item_instance.to_dict()
# create an instance of GetStockItemIdsBySKUItem from a dict
get_stock_item_ids_by_sku_item_from_dict = GetStockItemIdsBySKUItem.from_dict(get_stock_item_ids_by_sku_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


