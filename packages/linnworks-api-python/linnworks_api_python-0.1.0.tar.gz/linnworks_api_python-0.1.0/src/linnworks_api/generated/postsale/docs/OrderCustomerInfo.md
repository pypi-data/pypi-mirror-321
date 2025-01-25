# OrderCustomerInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_buyer_name** | **str** |  | [optional] 
**address** | [**CustomerAddress**](CustomerAddress.md) |  | [optional] 
**billing_address** | [**CustomerAddress**](CustomerAddress.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.postsale.models.order_customer_info import OrderCustomerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCustomerInfo from a JSON string
order_customer_info_instance = OrderCustomerInfo.from_json(json)
# print the JSON string representation of the object
print(OrderCustomerInfo.to_json())

# convert the object into a dict
order_customer_info_dict = order_customer_info_instance.to_dict()
# create an instance of OrderCustomerInfo from a dict
order_customer_info_from_dict = OrderCustomerInfo.from_dict(order_customer_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


