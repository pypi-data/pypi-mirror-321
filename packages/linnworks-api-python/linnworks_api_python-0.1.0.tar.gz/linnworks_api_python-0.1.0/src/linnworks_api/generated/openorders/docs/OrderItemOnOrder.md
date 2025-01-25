# OrderItemOnOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_purchase_item_id** | **str** |  | [optional] 
**rowid** | **str** |  | [optional] 
**pk_purchase_id** | **str** |  | [optional] 
**external_invoice_number** | **str** |  | [optional] 
**fk_supplier_id** | **str** |  | [optional] 
**date_of_delivery** | **datetime** |  | [optional] 
**quoted_delivery_date** | **datetime** |  | [optional] 
**supplier_name** | **str** |  | [optional] 
**fk_location_id** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.openorders.models.order_item_on_order import OrderItemOnOrder

# TODO update the JSON string below
json = "{}"
# create an instance of OrderItemOnOrder from a JSON string
order_item_on_order_instance = OrderItemOnOrder.from_json(json)
# print the JSON string representation of the object
print(OrderItemOnOrder.to_json())

# convert the object into a dict
order_item_on_order_dict = order_item_on_order_instance.to_dict()
# create an instance of OrderItemOnOrder from a dict
order_item_on_order_from_dict = OrderItemOnOrder.from_dict(order_item_on_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


