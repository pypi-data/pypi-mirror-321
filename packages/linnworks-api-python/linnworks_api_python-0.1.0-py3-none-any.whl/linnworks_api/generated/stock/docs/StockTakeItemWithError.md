# StockTakeItemWithError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bin_rack** | **str** | (optional) Only applicable to non-batched and non-WMS locations. Singular BinRack will be updated for the given item for a given location. Will be ignored for a batched or WMS item. | [optional] 
**picking_wave_items** | [**List[BatchPickingWaveStockItems]**](BatchPickingWaveStockItems.md) | (optional) Pickwave items associated with the batch. This data will be used for concurrency check and validation of data.   Super important stuff when you are submitting batch inventory stock count in WMS location.   Order items will automatically be allocated to a specific batch when the order is placed/printed/added to pickwave. This will normally block stock count,   however it is possible to get the state of pickwave items, and if all items are picked from the location the user can still count them. When stock count is submitted  we need to also submit the state of the pickwave at the point of count, so we can compare state was and the state is, discount any stock from the count that was processed/shipped   If this parameter is not supplied and the batch is allocated to orders, the stock count for this item will be blocked and will not be submitted | [optional] 
**errors** | **List[str]** | List of errors for specific stock take item | [optional] 
**stock_item_id** | **str** | Stock Item Id | [optional] 
**quantity** | **int** | Current stock level | [optional] 
**original_quantity** | **int** | (Optional) Original quantity, used to validate if the original has changed since the items have been counted. If supplied and different to expected then an error will be returned. | [optional] 
**stock_value** | **float** | (optional) Stock value (unit cost * quantity). If not provided it will be calculated from current stock value | [optional] 
**batch_inventory_id** | **int** | (conditional) If item is batched or in WMS location, you must provide BatchInventoryId which is being updated.   If its newly discovered item, use BookInStockBatch call in Stock controller to create a new batch inventory | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.stock_take_item_with_error import StockTakeItemWithError

# TODO update the JSON string below
json = "{}"
# create an instance of StockTakeItemWithError from a JSON string
stock_take_item_with_error_instance = StockTakeItemWithError.from_json(json)
# print the JSON string representation of the object
print(StockTakeItemWithError.to_json())

# convert the object into a dict
stock_take_item_with_error_dict = stock_take_item_with_error_instance.to_dict()
# create an instance of StockTakeItemWithError from a dict
stock_take_item_with_error_from_dict = StockTakeItemWithError.from_dict(stock_take_item_with_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


