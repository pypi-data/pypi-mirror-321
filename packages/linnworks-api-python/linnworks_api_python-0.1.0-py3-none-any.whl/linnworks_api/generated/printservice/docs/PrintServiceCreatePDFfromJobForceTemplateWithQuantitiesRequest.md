# PrintServiceCreatePDFfromJobForceTemplateWithQuantitiesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_type** | **str** | The template type | [optional] 
**ids_and_quantities** | [**List[KeyValueGuidInt32]**](KeyValueGuidInt32.md) | Stock Id and quantity of stock | [optional] 
**template_id** | **int** | The ID of the template to use | [optional] 
**parameters** | [**List[KeyValueStringString]**](KeyValueStringString.md) |  | [optional] 
**printer_name** | **str** | Printer name of the virtual printer to use. If null then the sepecified in the template | [optional] 
**print_zone_code** | **str** | Print zone code, if present, will override the printer used if the template has a set printer for that zone | [optional] 

## Example

```python
from linnworks_api.generated.printservice.models.print_service_create_pd_ffrom_job_force_template_with_quantities_request import PrintServiceCreatePDFfromJobForceTemplateWithQuantitiesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PrintServiceCreatePDFfromJobForceTemplateWithQuantitiesRequest from a JSON string
print_service_create_pd_ffrom_job_force_template_with_quantities_request_instance = PrintServiceCreatePDFfromJobForceTemplateWithQuantitiesRequest.from_json(json)
# print the JSON string representation of the object
print(PrintServiceCreatePDFfromJobForceTemplateWithQuantitiesRequest.to_json())

# convert the object into a dict
print_service_create_pd_ffrom_job_force_template_with_quantities_request_dict = print_service_create_pd_ffrom_job_force_template_with_quantities_request_instance.to_dict()
# create an instance of PrintServiceCreatePDFfromJobForceTemplateWithQuantitiesRequest from a dict
print_service_create_pd_ffrom_job_force_template_with_quantities_request_from_dict = PrintServiceCreatePDFfromJobForceTemplateWithQuantitiesRequest.from_dict(print_service_create_pd_ffrom_job_force_template_with_quantities_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


