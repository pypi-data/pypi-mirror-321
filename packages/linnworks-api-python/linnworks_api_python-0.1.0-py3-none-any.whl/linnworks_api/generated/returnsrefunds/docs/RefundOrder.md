# RefundOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_order_id** | **str** |  | [optional] 
**n_order_id** | **int** |  | [optional] 
**c_full_name** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**sub_source** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 
**issue_refund_url** | **str** |  | [optional] 
**c_currency** | **str** |  | [optional] 
**reference_num** | **str** |  | [optional] 
**secondary_reference** | **str** |  | [optional] 
**refund_reference** | **str** |  | [optional] 
**refund_date** | **datetime** |  | [optional] 
**sub_total** | **float** |  | [optional] 
**total** | **float** |  | [optional] 
**tax_rate** | **float** |  | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.refund_order import RefundOrder

# TODO update the JSON string below
json = "{}"
# create an instance of RefundOrder from a JSON string
refund_order_instance = RefundOrder.from_json(json)
# print the JSON string representation of the object
print(RefundOrder.to_json())

# convert the object into a dict
refund_order_dict = refund_order_instance.to_dict()
# create an instance of RefundOrder from a dict
refund_order_from_dict = RefundOrder.from_dict(refund_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


