# UpdatedResendItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rma_row_id** | **int** |  | [optional] 
**remove_from_booking** | **bool** |  | [optional] 
**resend_quantity** | **int** |  | [optional] 
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
from linnworks_api.generated.returnsrefunds.models.updated_resend_item import UpdatedResendItem

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatedResendItem from a JSON string
updated_resend_item_instance = UpdatedResendItem.from_json(json)
# print the JSON string representation of the object
print(UpdatedResendItem.to_json())

# convert the object into a dict
updated_resend_item_dict = updated_resend_item_instance.to_dict()
# create an instance of UpdatedResendItem from a dict
updated_resend_item_from_dict = UpdatedResendItem.from_dict(updated_resend_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


