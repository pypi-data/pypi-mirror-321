# UpdateStockLevelsBulkRequestItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sku** | **str** | SKU - Optional if stock item id is provided | [optional] 
**stock_item_id** | **str** | StockItemId - Optional if stock SKU is provided, calls will be faster if this is provided. | [optional] 
**stock_location_name** | **str** | Stock location name, optional if StockLocationId is provided. | [optional] 
**stock_location_id** | **str** | Stock Location Id, optional if StockLocationName is provided, calls will be faster if this is provided. | [optional] 
**stock_level** | **int** | StockLevel - Optional | [optional] 
**stock_value** | **float** | StockValue - Optional, if unit cost is provided then value will be calculated from this, otherwise existing stock value or purchase price will be used. | [optional] 
**unit_cost** | **float** | UnitCost - Optional, if stock value is provided then value will be calculated from this, otherwise existing stock value or purchase price will be used. | [optional] 
**binrack** | **str** | Binrack - Optional, if not provided or empty exisitng binrack will remain. | [optional] 
**minimum_level** | **int** | Minimum level - Optional | [optional] 
**row_index** | **int** | RowIndex - Optional, can be used to marry up request items with response items. | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.update_stock_levels_bulk_request_item import UpdateStockLevelsBulkRequestItem

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateStockLevelsBulkRequestItem from a JSON string
update_stock_levels_bulk_request_item_instance = UpdateStockLevelsBulkRequestItem.from_json(json)
# print the JSON string representation of the object
print(UpdateStockLevelsBulkRequestItem.to_json())

# convert the object into a dict
update_stock_levels_bulk_request_item_dict = update_stock_levels_bulk_request_item_instance.to_dict()
# create an instance of UpdateStockLevelsBulkRequestItem from a dict
update_stock_levels_bulk_request_item_from_dict = UpdateStockLevelsBulkRequestItem.from_dict(update_stock_levels_bulk_request_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


