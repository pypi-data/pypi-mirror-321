# OrderRefundHeader


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refund_header_id** | **int** |  | [optional] 
**currency** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 
**refund_lines** | [**List[VerifiedRefund]**](VerifiedRefund.md) |  | [optional] 
**refund_link** | **str** |  | [optional] 
**order_id** | **str** |  | [optional] 
**num_order_id** | **int** |  | [optional] 
**status** | [**PostSaleStatus**](PostSaleStatus.md) |  | [optional] 
**order_source** | **str** |  | [optional] 
**order_sub_source** | **str** |  | [optional] 
**external_reference** | **str** |  | [optional] 
**channel_initiated** | **bool** |  | [optional] 
**created_date** | **datetime** |  | [optional] 
**actioned** | **bool** |  | [optional] 
**last_action_date** | **datetime** |  | [optional] 

## Example

```python
from linnworks_api.generated.postsale.models.order_refund_header import OrderRefundHeader

# TODO update the JSON string below
json = "{}"
# create an instance of OrderRefundHeader from a JSON string
order_refund_header_instance = OrderRefundHeader.from_json(json)
# print the JSON string representation of the object
print(OrderRefundHeader.to_json())

# convert the object into a dict
order_refund_header_dict = order_refund_header_instance.to_dict()
# create an instance of OrderRefundHeader from a dict
order_refund_header_from_dict = OrderRefundHeader.from_dict(order_refund_header_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


