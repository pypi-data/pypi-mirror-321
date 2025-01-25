# OrderShippingInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor** | **str** |  | [optional] 
**postal_service_id** | **str** |  | [optional] 
**postal_service_name** | **str** |  | [optional] 
**total_weight** | **float** |  | [optional] 
**item_weight** | **float** |  | [optional] 
**package_category_id** | **str** |  | [optional] 
**package_category** | **str** |  | [optional] 
**package_type_id** | **str** |  | [optional] 
**package_type** | **str** |  | [optional] 
**postage_cost** | **float** |  | [optional] 
**postage_cost_ex_tax** | **float** |  | [optional] 
**tracking_number** | **str** |  | [optional] 
**manual_adjust** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.openorders.models.order_shipping_info import OrderShippingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OrderShippingInfo from a JSON string
order_shipping_info_instance = OrderShippingInfo.from_json(json)
# print the JSON string representation of the object
print(OrderShippingInfo.to_json())

# convert the object into a dict
order_shipping_info_dict = order_shipping_info_instance.to_dict()
# create an instance of OrderShippingInfo from a dict
order_shipping_info_from_dict = OrderShippingInfo.from_dict(order_shipping_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


