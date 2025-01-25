# ItemizedRefundReason


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**item_id** | **str** |  | [optional] 
**reasons** | [**List[ChannelReasonBase]**](ChannelReasonBase.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.itemized_refund_reason import ItemizedRefundReason

# TODO update the JSON string below
json = "{}"
# create an instance of ItemizedRefundReason from a JSON string
itemized_refund_reason_instance = ItemizedRefundReason.from_json(json)
# print the JSON string representation of the object
print(ItemizedRefundReason.to_json())

# convert the object into a dict
itemized_refund_reason_dict = itemized_refund_reason_instance.to_dict()
# create an instance of ItemizedRefundReason from a dict
itemized_refund_reason_from_dict = ItemizedRefundReason.from_dict(itemized_refund_reason_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


