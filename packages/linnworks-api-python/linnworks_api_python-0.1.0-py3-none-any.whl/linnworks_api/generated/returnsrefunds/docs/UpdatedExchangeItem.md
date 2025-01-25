# UpdatedExchangeItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rma_row_id** | **int** |  | [optional] 
**remove_from_booking** | **bool** |  | [optional] 
**exchange_stock_item_id** | **str** |  | [optional] 
**exchange_sku** | **str** |  | [optional] 
**exchange_title** | **str** |  | [optional] 
**exchange_quantity** | **int** |  | [optional] 
**despatch_location_id** | **str** |  | [optional] 
**additional_cost** | **float** |  | [optional] 
**order_item_row_id** | **str** |  | [optional] 
**return_item_sku** | **str** |  | [optional] 
**return_item_title** | **str** |  | [optional] 
**batch_inventory_id** | **int** |  | [optional] 
**return_location** | **str** |  | [optional] 
**return_quantity** | **int** |  | [optional] 
**refund_amount** | **float** |  | [optional] 
**refund_row_id** | **str** |  | [optional] 
**scrap_quantity** | **int** |  | [optional] 
**reason_category** | **str** |  | [optional] 
**is_free_text** | **bool** |  | [optional] [readonly] 
**reason** | **str** |  | [optional] 
**reason_tag** | **str** |  | [optional] 
**sub_reason_tag** | **str** |  | [optional] 
**status** | [**PostSaleStatus**](PostSaleStatus.md) |  | [optional] 
**binrack_override** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.updated_exchange_item import UpdatedExchangeItem

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatedExchangeItem from a JSON string
updated_exchange_item_instance = UpdatedExchangeItem.from_json(json)
# print the JSON string representation of the object
print(UpdatedExchangeItem.to_json())

# convert the object into a dict
updated_exchange_item_dict = updated_exchange_item_instance.to_dict()
# create an instance of UpdatedExchangeItem from a dict
updated_exchange_item_from_dict = UpdatedExchangeItem.from_dict(updated_exchange_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


