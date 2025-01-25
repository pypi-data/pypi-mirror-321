# ReturnInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_return_id** | **int** |  | [optional] 
**row_type** | **str** |  | [optional] 
**return_reference** | **str** |  | [optional] 
**fk_order_id** | **str** |  | [optional] 
**fk_order_item_row_id** | **str** |  | [optional] 
**order_item_batch_id** | **int** |  | [optional] 
**n_order_id** | **int** |  | [optional] 
**sku** | **str** |  | [optional] 
**item_title** | **str** |  | [optional] 
**batch_number** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 
**channel_reason** | **str** |  | [optional] 
**channel_reason_sec** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**return_qty** | **int** |  | [optional] 
**fk_return_location_id** | **str** |  | [optional] 
**scrapped** | **bool** |  | [optional] 
**scrap_qty** | **int** |  | [optional] 
**last_state** | **str** |  | [optional] 
**last_date** | **datetime** |  | [optional] 
**completed** | **bool** |  | [optional] 
**fk_new_order_id** | **str** |  | [optional] 
**fk_new_order_item_row_id** | **str** |  | [optional] 
**fk_new_stock_item_id** | **str** |  | [optional] 
**new_qty** | **int** |  | [optional] 
**new_order_id** | **int** |  | [optional] 
**new_order_cancelled** | **bool** |  | [optional] 
**new_sku** | **str** |  | [optional] 
**new_item_title** | **str** |  | [optional] 
**new_order_processed_on** | **datetime** |  | [optional] 
**additional_cost** | **float** |  | [optional] 
**fk_refund_row_id** | **str** |  | [optional] 
**refunded_amount** | **float** |  | [optional] 
**pending_refund** | **float** |  | [optional] 
**return_date** | **datetime** |  | [optional] 

## Example

```python
from linnworks_api.generated.processedorders.models.return_info import ReturnInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnInfo from a JSON string
return_info_instance = ReturnInfo.from_json(json)
# print the JSON string representation of the object
print(ReturnInfo.to_json())

# convert the object into a dict
return_info_dict = return_info_instance.to_dict()
# create an instance of ReturnInfo from a dict
return_info_from_dict = ReturnInfo.from_dict(return_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


