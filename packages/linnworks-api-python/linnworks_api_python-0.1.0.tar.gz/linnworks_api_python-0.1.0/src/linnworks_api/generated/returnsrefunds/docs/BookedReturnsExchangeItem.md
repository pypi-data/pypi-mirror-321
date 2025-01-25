# BookedReturnsExchangeItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fk_order_item_row_id** | **str** |  | [optional] 
**order_item_batch_id** | **int** |  | [optional] 
**stock_item_id** | **str** |  | [optional] 
**batch_inventory_id** | **int** |  | [optional] 
**batch_number** | **str** |  | [optional] 
**row_type** | **str** |  | [optional] 
**sku** | **str** |  | [optional] 
**item_title** | **str** |  | [optional] 
**return_qty** | **int** |  | [optional] 
**max_return_qty** | **int** |  | [optional] 
**new_qty** | **int** |  | [optional] 
**new_sku** | **str** |  | [optional] 
**new_title** | **str** |  | [optional] 
**fk_new_stock_item_id** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 
**fk_return_location_id** | **str** |  | [optional] 
**return_location** | **str** |  | [optional] 
**pending_refund_amount** | **float** |  | [optional] 
**scrapped** | **bool** |  | [optional] 
**scrap_qty** | **int** |  | [optional] 
**parent_order_item_row_id** | **str** |  | [optional] 
**additional_cost** | **float** |  | [optional] 
**c_currency** | **str** |  | [optional] 
**pk_return_id** | **int** |  | [optional] 
**channel_reason** | **str** |  | [optional] 
**channel_reason_sec** | **str** |  | [optional] 
**return_date** | **datetime** |  | [optional] 
**despatch_unit_value** | **float** |  | [optional] 
**batch_inventory** | [**StockItemBatchInventory**](StockItemBatchInventory.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.booked_returns_exchange_item import BookedReturnsExchangeItem

# TODO update the JSON string below
json = "{}"
# create an instance of BookedReturnsExchangeItem from a JSON string
booked_returns_exchange_item_instance = BookedReturnsExchangeItem.from_json(json)
# print the JSON string representation of the object
print(BookedReturnsExchangeItem.to_json())

# convert the object into a dict
booked_returns_exchange_item_dict = booked_returns_exchange_item_instance.to_dict()
# create an instance of BookedReturnsExchangeItem from a dict
booked_returns_exchange_item_from_dict = BookedReturnsExchangeItem.from_dict(booked_returns_exchange_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


