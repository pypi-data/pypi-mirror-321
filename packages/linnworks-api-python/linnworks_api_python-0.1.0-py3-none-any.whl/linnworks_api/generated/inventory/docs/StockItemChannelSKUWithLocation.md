# StockItemChannelSKUWithLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fk_row_id** | **str** |  | [optional] 
**location_id** | **int** |  | [optional] 
**location_name** | **str** |  | [optional] 
**ignore_sync** | **bool** |  | [optional] 
**max_listed_quantity** | **int** |  | [optional] 
**end_when_stock** | **int** |  | [optional] 
**stock_percentage** | **float** |  | [optional] 
**last_update** | **datetime** |  | [optional] 
**update_status** | **str** |  | [optional] 
**submitted_quantity** | **int** |  | [optional] 
**listed_quantity** | **int** |  | [optional] 
**retry_count** | **int** |  | [optional] 
**stock_item_id** | **str** |  | [optional] 
**stock_item_int_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.stock_item_channel_sku_with_location import StockItemChannelSKUWithLocation

# TODO update the JSON string below
json = "{}"
# create an instance of StockItemChannelSKUWithLocation from a JSON string
stock_item_channel_sku_with_location_instance = StockItemChannelSKUWithLocation.from_json(json)
# print the JSON string representation of the object
print(StockItemChannelSKUWithLocation.to_json())

# convert the object into a dict
stock_item_channel_sku_with_location_dict = stock_item_channel_sku_with_location_instance.to_dict()
# create an instance of StockItemChannelSKUWithLocation from a dict
stock_item_channel_sku_with_location_from_dict = StockItemChannelSKUWithLocation.from_dict(stock_item_channel_sku_with_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


