# NewRefundLine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**return_row_id** | **int** |  | [optional] 
**order_item_row_id** | **str** |  | [optional] 
**refunded_unit** | **str** |  | [optional] 
**cancelled_quantity** | **int** |  | [optional] 
**external_reference** | **str** |  | [optional] 
**is_free_text** | **bool** |  | [optional] [readonly] 
**free_text_or_note** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 
**quantity** | **int** |  | [optional] 
**reason_tag** | **str** |  | [optional] 
**sub_reason_tag** | **str** |  | [optional] 
**insufficient_refund_tag** | **str** |  | [optional] 
**insufficient_refund_note** | **str** |  | [optional] 
**reason_category** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.new_refund_line import NewRefundLine

# TODO update the JSON string below
json = "{}"
# create an instance of NewRefundLine from a JSON string
new_refund_line_instance = NewRefundLine.from_json(json)
# print the JSON string representation of the object
print(NewRefundLine.to_json())

# convert the object into a dict
new_refund_line_dict = new_refund_line_instance.to_dict()
# create an instance of NewRefundLine from a dict
new_refund_line_from_dict = NewRefundLine.from_dict(new_refund_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


