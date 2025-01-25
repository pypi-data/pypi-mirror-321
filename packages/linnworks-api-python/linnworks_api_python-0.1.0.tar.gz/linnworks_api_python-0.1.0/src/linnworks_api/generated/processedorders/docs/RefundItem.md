# RefundItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_refund_row_id** | **str** |  | [optional] 
**is_manual_refund** | **bool** |  | [optional] 
**type** | **str** |  | [optional] 
**fk_order_item_id** | **str** |  | [optional] 
**refund_qty** | **int** |  | [optional] 
**refund_amount** | **float** |  | [optional] 
**reason** | **str** |  | [optional] 
**channel_reason** | **str** |  | [optional] 
**channel_reason_sec** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.processedorders.models.refund_item import RefundItem

# TODO update the JSON string below
json = "{}"
# create an instance of RefundItem from a JSON string
refund_item_instance = RefundItem.from_json(json)
# print the JSON string representation of the object
print(RefundItem.to_json())

# convert the object into a dict
refund_item_dict = refund_item_instance.to_dict()
# create an instance of RefundItem from a dict
refund_item_from_dict = RefundItem.from_dict(refund_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


