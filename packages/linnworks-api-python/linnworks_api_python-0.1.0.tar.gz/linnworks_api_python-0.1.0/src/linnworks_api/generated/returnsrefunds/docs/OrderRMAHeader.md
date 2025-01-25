# OrderRMAHeader


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rma_header_id** | **int** |  | [optional] 
**rma_lines** | [**List[VerifiedRMAItem]**](VerifiedRMAItem.md) |  | [optional] 
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
from linnworks_api.generated.returnsrefunds.models.order_rma_header import OrderRMAHeader

# TODO update the JSON string below
json = "{}"
# create an instance of OrderRMAHeader from a JSON string
order_rma_header_instance = OrderRMAHeader.from_json(json)
# print the JSON string representation of the object
print(OrderRMAHeader.to_json())

# convert the object into a dict
order_rma_header_dict = order_rma_header_instance.to_dict()
# create an instance of OrderRMAHeader from a dict
order_rma_header_from_dict = OrderRMAHeader.from_dict(order_rma_header_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


