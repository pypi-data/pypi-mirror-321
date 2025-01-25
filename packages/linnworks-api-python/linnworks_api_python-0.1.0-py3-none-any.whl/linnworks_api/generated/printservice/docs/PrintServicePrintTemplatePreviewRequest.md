# PrintServicePrintTemplatePreviewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **int** | Template id | [optional] 

## Example

```python
from linnworks_api.generated.printservice.models.print_service_print_template_preview_request import PrintServicePrintTemplatePreviewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PrintServicePrintTemplatePreviewRequest from a JSON string
print_service_print_template_preview_request_instance = PrintServicePrintTemplatePreviewRequest.from_json(json)
# print the JSON string representation of the object
print(PrintServicePrintTemplatePreviewRequest.to_json())

# convert the object into a dict
print_service_print_template_preview_request_dict = print_service_print_template_preview_request_instance.to_dict()
# create an instance of PrintServicePrintTemplatePreviewRequest from a dict
print_service_print_template_preview_request_from_dict = PrintServicePrintTemplatePreviewRequest.from_dict(print_service_print_template_preview_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


