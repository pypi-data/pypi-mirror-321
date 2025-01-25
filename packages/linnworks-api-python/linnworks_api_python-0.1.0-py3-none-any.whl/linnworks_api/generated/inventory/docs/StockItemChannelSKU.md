# StockItemChannelSKU


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_sku_row_id** | **str** |  | [optional] 
**sku** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**sub_source** | **str** |  | [optional] 
**update_status** | **str** |  | [optional] 
**channel_reference_id** | **str** |  | [optional] 
**last_update** | **datetime** |  | [optional] 
**max_listed_quantity** | **int** |  | [optional] 
**end_when_stock** | **int** |  | [optional] 
**submitted_quantity** | **int** |  | [optional] 
**listed_quantity** | **int** |  | [optional] 
**stock_percentage** | **float** |  | [optional] 
**ignore_sync** | **bool** |  | [optional] 
**ignore_sync_multi_location** | **bool** |  | [optional] 
**is_multi_location** | **bool** |  | [optional] 
**stock_item_id** | **str** |  | [optional] 
**stock_item_int_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.stock_item_channel_sku import StockItemChannelSKU

# TODO update the JSON string below
json = "{}"
# create an instance of StockItemChannelSKU from a JSON string
stock_item_channel_sku_instance = StockItemChannelSKU.from_json(json)
# print the JSON string representation of the object
print(StockItemChannelSKU.to_json())

# convert the object into a dict
stock_item_channel_sku_dict = stock_item_channel_sku_instance.to_dict()
# create an instance of StockItemChannelSKU from a dict
stock_item_channel_sku_from_dict = StockItemChannelSKU.from_dict(stock_item_channel_sku_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


