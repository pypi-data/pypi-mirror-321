# RefundInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_refund_row_id** | **str** |  | [optional] 
**sku** | **str** |  | [optional] 
**item_title** | **str** |  | [optional] 
**is_item** | **bool** |  | [optional] 
**is_service** | **bool** |  | [optional] 
**amount** | **float** |  | [optional] 
**reason** | **str** |  | [optional] 
**actioned** | **bool** |  | [optional] 
**action_date** | **datetime** |  | [optional] 
**return_reference** | **str** |  | [optional] 
**cost** | **float** |  | [optional] 
**refund_status** | **str** |  | [optional] 
**ignored_validation** | **bool** |  | [optional] 
**fk_order_item_row_id** | **str** |  | [optional] 
**should_serialize_channel_reason** | **bool** |  | [optional] [readonly] 
**channel_reason** | **str** |  | [optional] 
**should_serialize_channel_reason_sec** | **bool** |  | [optional] [readonly] 
**channel_reason_sec** | **str** |  | [optional] 
**is_new** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.processedorders.models.refund_info import RefundInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RefundInfo from a JSON string
refund_info_instance = RefundInfo.from_json(json)
# print the JSON string representation of the object
print(RefundInfo.to_json())

# convert the object into a dict
refund_info_dict = refund_info_instance.to_dict()
# create an instance of RefundInfo from a dict
refund_info_from_dict = RefundInfo.from_dict(refund_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


