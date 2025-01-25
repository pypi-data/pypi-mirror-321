# PrintServiceCreateReturnShippingLabelsPDFRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** | A list containing the (single) pkOrderId of the order to print return labels for | [optional] 
**order_item_ids_and_quantities** | [**List[KeyValueGuidInt32]**](KeyValueGuidInt32.md) | A list of the order item IDs and quantities to include. If empty then same as the outbound shipment | [optional] 
**return_postal_service_name** | **str** | Name of the postal service to use. If null then specified in settings or same as the outbound shipment | [optional] 

## Example

```python
from linnworks_api.generated.printservice.models.print_service_create_return_shipping_labels_pdf_request import PrintServiceCreateReturnShippingLabelsPDFRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PrintServiceCreateReturnShippingLabelsPDFRequest from a JSON string
print_service_create_return_shipping_labels_pdf_request_instance = PrintServiceCreateReturnShippingLabelsPDFRequest.from_json(json)
# print the JSON string representation of the object
print(PrintServiceCreateReturnShippingLabelsPDFRequest.to_json())

# convert the object into a dict
print_service_create_return_shipping_labels_pdf_request_dict = print_service_create_return_shipping_labels_pdf_request_instance.to_dict()
# create an instance of PrintServiceCreateReturnShippingLabelsPDFRequest from a dict
print_service_create_return_shipping_labels_pdf_request_from_dict = PrintServiceCreateReturnShippingLabelsPDFRequest.from_dict(print_service_create_return_shipping_labels_pdf_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


