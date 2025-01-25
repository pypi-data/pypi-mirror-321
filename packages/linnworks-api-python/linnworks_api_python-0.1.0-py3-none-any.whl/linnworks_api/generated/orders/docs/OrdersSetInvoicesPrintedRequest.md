# OrdersSetInvoicesPrintedRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_ids** | **List[str]** | List of orders to mark as label printed | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_set_invoices_printed_request import OrdersSetInvoicesPrintedRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersSetInvoicesPrintedRequest from a JSON string
orders_set_invoices_printed_request_instance = OrdersSetInvoicesPrintedRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersSetInvoicesPrintedRequest.to_json())

# convert the object into a dict
orders_set_invoices_printed_request_dict = orders_set_invoices_printed_request_instance.to_dict()
# create an instance of OrdersSetInvoicesPrintedRequest from a dict
orders_set_invoices_printed_request_from_dict = OrdersSetInvoicesPrintedRequest.from_dict(orders_set_invoices_printed_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


