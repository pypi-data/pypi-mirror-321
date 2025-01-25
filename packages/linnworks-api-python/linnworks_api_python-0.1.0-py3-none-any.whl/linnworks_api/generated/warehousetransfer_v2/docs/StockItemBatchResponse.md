# StockItemBatchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fk_bin_rack_id** | **int** |  | [optional] 
**batch_id** | **int** |  | [optional] 
**batch_inventory_id** | **int** |  | [optional] 
**bin_rack_type** | [**BinRackResponse**](BinRackResponse.md) |  | [optional] 
**bin_rack** | **str** |  | [optional] 
**expires_on** | **datetime** |  | [optional] 
**number** | **str** |  | [optional] 
**priority_sequence** | **int** |  | [optional] 
**available** | **int** |  | [optional] 
**quantity** | **int** |  | [optional] 
**sell_by** | **datetime** |  | [optional] 
**status** | **str** |  | [optional] 
**stock_item_int_id** | **int** |  | [optional] 
**stock_item_id** | **str** |  | [optional] 
**stock_location_id** | **str** |  | [optional] 
**stock_value** | **float** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_v2.models.stock_item_batch_response import StockItemBatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StockItemBatchResponse from a JSON string
stock_item_batch_response_instance = StockItemBatchResponse.from_json(json)
# print the JSON string representation of the object
print(StockItemBatchResponse.to_json())

# convert the object into a dict
stock_item_batch_response_dict = stock_item_batch_response_instance.to_dict()
# create an instance of StockItemBatchResponse from a dict
stock_item_batch_response_from_dict = StockItemBatchResponse.from_dict(stock_item_batch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


