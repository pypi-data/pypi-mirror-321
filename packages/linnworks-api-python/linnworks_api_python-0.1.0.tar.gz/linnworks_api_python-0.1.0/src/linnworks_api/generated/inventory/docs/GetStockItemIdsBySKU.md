# GetStockItemIdsBySKU

Get stock item id's by sku request class.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[GetStockItemIdsBySKUItem]**](GetStockItemIdsBySKUItem.md) | Response items of StockItemId and SKU | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.get_stock_item_ids_by_sku import GetStockItemIdsBySKU

# TODO update the JSON string below
json = "{}"
# create an instance of GetStockItemIdsBySKU from a JSON string
get_stock_item_ids_by_sku_instance = GetStockItemIdsBySKU.from_json(json)
# print the JSON string representation of the object
print(GetStockItemIdsBySKU.to_json())

# convert the object into a dict
get_stock_item_ids_by_sku_dict = get_stock_item_ids_by_sku_instance.to_dict()
# create an instance of GetStockItemIdsBySKU from a dict
get_stock_item_ids_by_sku_from_dict = GetStockItemIdsBySKU.from_dict(get_stock_item_ids_by_sku_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


