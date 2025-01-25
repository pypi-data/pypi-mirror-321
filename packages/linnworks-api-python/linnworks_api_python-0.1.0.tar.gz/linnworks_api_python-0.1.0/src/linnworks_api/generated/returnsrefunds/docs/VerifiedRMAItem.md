# VerifiedRMAItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rma_row_id** | **int** |  | [optional] 
**rma_header_id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**status** | [**PostSaleStatus**](PostSaleStatus.md) |  | [optional] 
**external_reference** | **str** |  | [optional] 
**created_date** | **datetime** |  | [optional] 
**actioned** | **bool** |  | [optional] 
**actioned_date** | **datetime** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**resend_quantity** | **int** |  | [optional] [readonly] 
**new_order_id** | **str** |  | [optional] 
**validation_error** | **str** |  | [optional] 
**error** | **str** |  | [optional] 
**errors** | [**List[RMAError]**](RMAError.md) |  | [optional] 
**info** | **str** |  | [optional] 
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
**binrack_override** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.verified_rma_item import VerifiedRMAItem

# TODO update the JSON string below
json = "{}"
# create an instance of VerifiedRMAItem from a JSON string
verified_rma_item_instance = VerifiedRMAItem.from_json(json)
# print the JSON string representation of the object
print(VerifiedRMAItem.to_json())

# convert the object into a dict
verified_rma_item_dict = verified_rma_item_instance.to_dict()
# create an instance of VerifiedRMAItem from a dict
verified_rma_item_from_dict = VerifiedRMAItem.from_dict(verified_rma_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


