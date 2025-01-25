# VerifiedRefundItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_item_row_id** | **str** |  | [optional] 
**return_row_id** | **int** |  | [optional] 
**item_sku** | **str** |  | [optional] 
**channel_sku** | **str** |  | [optional] 
**item_title** | **str** |  | [optional] 
**cost** | **float** |  | [optional] 
**cancelled_quantity** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.postsale.models.verified_refund_item import VerifiedRefundItem

# TODO update the JSON string below
json = "{}"
# create an instance of VerifiedRefundItem from a JSON string
verified_refund_item_instance = VerifiedRefundItem.from_json(json)
# print the JSON string representation of the object
print(VerifiedRefundItem.to_json())

# convert the object into a dict
verified_refund_item_dict = verified_refund_item_instance.to_dict()
# create an instance of VerifiedRefundItem from a dict
verified_refund_item_from_dict = VerifiedRefundItem.from_dict(verified_refund_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


