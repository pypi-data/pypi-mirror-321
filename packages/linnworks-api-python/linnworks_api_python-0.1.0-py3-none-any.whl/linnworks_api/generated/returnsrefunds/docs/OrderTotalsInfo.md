# OrderTotalsInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subtotal** | **float** |  | [optional] 
**postage_cost** | **float** |  | [optional] 
**postage_cost_ex_tax** | **float** |  | [optional] 
**tax** | **float** |  | [optional] 
**total_charge** | **float** |  | [optional] 
**payment_method** | **str** |  | [optional] 
**payment_method_id** | **str** |  | [optional] 
**profit_margin** | **float** |  | [optional] [readonly] 
**total_discount** | **float** |  | [optional] 
**currency** | **str** |  | [optional] 
**country_tax_rate** | **float** |  | [optional] 
**conversion_rate** | **float** |  | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.order_totals_info import OrderTotalsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OrderTotalsInfo from a JSON string
order_totals_info_instance = OrderTotalsInfo.from_json(json)
# print the JSON string representation of the object
print(OrderTotalsInfo.to_json())

# convert the object into a dict
order_totals_info_dict = order_totals_info_instance.to_dict()
# create an instance of OrderTotalsInfo from a dict
order_totals_info_from_dict = OrderTotalsInfo.from_dict(order_totals_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


