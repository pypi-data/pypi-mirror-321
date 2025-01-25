# PrintServiceCreateReturnShippingLabelsPDFWithSKUsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_num** | **str** | Reference number of the order to print return labels for | [optional] 
**skus_and_quantities** | [**List[KeyValueStringInt32]**](KeyValueStringInt32.md) | A list of the SKUs and quantities to include. If empty then same as the outbound shipment | [optional] 
**return_postal_service_name** | **str** | Name of the postal service to use. If null then specified in settings or same as the outbound shipment | [optional] 

## Example

```python
from linnworks_api.generated.printservice.models.print_service_create_return_shipping_labels_pdf_with_skus_request import PrintServiceCreateReturnShippingLabelsPDFWithSKUsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PrintServiceCreateReturnShippingLabelsPDFWithSKUsRequest from a JSON string
print_service_create_return_shipping_labels_pdf_with_skus_request_instance = PrintServiceCreateReturnShippingLabelsPDFWithSKUsRequest.from_json(json)
# print the JSON string representation of the object
print(PrintServiceCreateReturnShippingLabelsPDFWithSKUsRequest.to_json())

# convert the object into a dict
print_service_create_return_shipping_labels_pdf_with_skus_request_dict = print_service_create_return_shipping_labels_pdf_with_skus_request_instance.to_dict()
# create an instance of PrintServiceCreateReturnShippingLabelsPDFWithSKUsRequest from a dict
print_service_create_return_shipping_labels_pdf_with_skus_request_from_dict = PrintServiceCreateReturnShippingLabelsPDFWithSKUsRequest.from_dict(print_service_create_return_shipping_labels_pdf_with_skus_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


