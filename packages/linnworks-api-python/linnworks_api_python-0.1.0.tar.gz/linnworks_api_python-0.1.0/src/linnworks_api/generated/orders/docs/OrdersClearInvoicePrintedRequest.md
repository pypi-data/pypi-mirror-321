# OrdersClearInvoicePrintedRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_ids** | **List[str]** | List of orders | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_clear_invoice_printed_request import OrdersClearInvoicePrintedRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersClearInvoicePrintedRequest from a JSON string
orders_clear_invoice_printed_request_instance = OrdersClearInvoicePrintedRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersClearInvoicePrintedRequest.to_json())

# convert the object into a dict
orders_clear_invoice_printed_request_dict = orders_clear_invoice_printed_request_instance.to_dict()
# create an instance of OrdersClearInvoicePrintedRequest from a dict
orders_clear_invoice_printed_request_from_dict = OrdersClearInvoicePrintedRequest.from_dict(orders_clear_invoice_printed_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


