# OrderDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** |  | [optional] 
**num_order_id** | **int** |  | [optional] 
**processed** | **bool** |  | [optional] 
**processed_date_time** | **datetime** |  | [optional] 
**fulfilment_location_id** | **str** |  | [optional] 
**general_info** | [**OrderGeneralInfo**](OrderGeneralInfo.md) |  | [optional] 
**shipping_info** | [**OrderShippingInfo**](OrderShippingInfo.md) |  | [optional] 
**customer_info** | [**OrderCustomerInfo**](OrderCustomerInfo.md) |  | [optional] 
**totals_info** | [**OrderTotalsInfo**](OrderTotalsInfo.md) |  | [optional] 
**extended_properties** | [**List[ExtendedProperty]**](ExtendedProperty.md) |  | [optional] 
**folder_name** | **List[str]** |  | [optional] 
**items** | [**List[OrderItem]**](OrderItem.md) |  | [optional] 
**notes** | [**List[OrderNote]**](OrderNote.md) |  | [optional] 
**paid_date_time** | **datetime** |  | [optional] 
**tax_id** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.postsale.models.order_details import OrderDetails

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDetails from a JSON string
order_details_instance = OrderDetails.from_json(json)
# print the JSON string representation of the object
print(OrderDetails.to_json())

# convert the object into a dict
order_details_dict = order_details_instance.to_dict()
# create an instance of OrderDetails from a dict
order_details_from_dict = OrderDetails.from_dict(order_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


