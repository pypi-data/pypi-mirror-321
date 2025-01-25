# UpdatedRefundLine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refund_row_id** | **str** |  | [optional] 
**remove_from_refund** | **bool** |  | [optional] 
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
from linnworks_api.generated.returnsrefunds.models.updated_refund_line import UpdatedRefundLine

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatedRefundLine from a JSON string
updated_refund_line_instance = UpdatedRefundLine.from_json(json)
# print the JSON string representation of the object
print(UpdatedRefundLine.to_json())

# convert the object into a dict
updated_refund_line_dict = updated_refund_line_instance.to_dict()
# create an instance of UpdatedRefundLine from a dict
updated_refund_line_from_dict = UpdatedRefundLine.from_dict(updated_refund_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


