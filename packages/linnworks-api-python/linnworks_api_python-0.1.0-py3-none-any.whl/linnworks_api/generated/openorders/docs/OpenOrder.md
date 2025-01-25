# OpenOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_order_id** | **int** |  | [optional] 
**general_info** | [**OrderGeneralInfo**](OrderGeneralInfo.md) |  | [optional] 
**shipping_info** | [**OrderShippingInfo**](OrderShippingInfo.md) |  | [optional] 
**customer_info** | [**OrderCustomerInfo**](OrderCustomerInfo.md) |  | [optional] 
**totals_info** | [**OrderTotalsInfo**](OrderTotalsInfo.md) |  | [optional] 
**tax_info** | [**OrderTaxInfo**](OrderTaxInfo.md) |  | [optional] 
**folder_name** | **List[str]** |  | [optional] 
**is_post_filtered_out** | **bool** |  | [optional] 
**can_fulfil** | **bool** |  | [optional] 
**fulfillment** | [**OrderFulfillmentState**](OrderFulfillmentState.md) |  | [optional] 
**items** | [**List[OrderItem]**](OrderItem.md) |  | [optional] 
**has_items** | **bool** |  | [optional] [readonly] 
**total_items_sum** | **int** |  | [optional] [readonly] 
**order_id** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.openorders.models.open_order import OpenOrder

# TODO update the JSON string below
json = "{}"
# create an instance of OpenOrder from a JSON string
open_order_instance = OpenOrder.from_json(json)
# print the JSON string representation of the object
print(OpenOrder.to_json())

# convert the object into a dict
open_order_dict = open_order_instance.to_dict()
# create an instance of OpenOrder from a dict
open_order_from_dict = OpenOrder.from_dict(open_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


