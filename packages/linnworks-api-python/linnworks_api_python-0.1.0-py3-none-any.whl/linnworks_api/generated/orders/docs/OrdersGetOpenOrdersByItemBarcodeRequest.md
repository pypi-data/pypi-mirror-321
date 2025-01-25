# OrdersGetOpenOrdersByItemBarcodeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_barcode** | **str** | Item barcode | [optional] 
**filters** | [**FieldsFilter**](FieldsFilter.md) |  | [optional] 
**location_id** | **str** | User location | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_get_open_orders_by_item_barcode_request import OrdersGetOpenOrdersByItemBarcodeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersGetOpenOrdersByItemBarcodeRequest from a JSON string
orders_get_open_orders_by_item_barcode_request_instance = OrdersGetOpenOrdersByItemBarcodeRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersGetOpenOrdersByItemBarcodeRequest.to_json())

# convert the object into a dict
orders_get_open_orders_by_item_barcode_request_dict = orders_get_open_orders_by_item_barcode_request_instance.to_dict()
# create an instance of OrdersGetOpenOrdersByItemBarcodeRequest from a dict
orders_get_open_orders_by_item_barcode_request_from_dict = OrdersGetOpenOrdersByItemBarcodeRequest.from_dict(orders_get_open_orders_by_item_barcode_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


