# PrintServiceCreatePDFfromJobForceTemplateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_type** | **str** | The template type | [optional] 
**ids** | **List[str]** | A list of IDs to print (e.g. Order IDs or Warehouse Transfer IDs) | [optional] 
**template_id** | **int** | The ID of the template to use | [optional] 
**parameters** | [**List[KeyValueStringString]**](KeyValueStringString.md) |  | [optional] 
**printer_name** | **str** | printer name of the ivrtual printer to use. If null then the sepecified in the template | [optional] 
**print_zone_code** | **str** | Print zone code, if present, will override the printer used if the template has a set printer for that zone | [optional] 
**page_start_number** | **int** | First page number. Used for splitting prints into multiple requests (optional, default to 0) | [optional] 
**operation_id** | **str** | The ID of the current operation, used in logging for tracing (optional, default to null) | [optional] 
**context** | [**ClientContext**](ClientContext.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.printservice.models.print_service_create_pd_ffrom_job_force_template_request import PrintServiceCreatePDFfromJobForceTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PrintServiceCreatePDFfromJobForceTemplateRequest from a JSON string
print_service_create_pd_ffrom_job_force_template_request_instance = PrintServiceCreatePDFfromJobForceTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(PrintServiceCreatePDFfromJobForceTemplateRequest.to_json())

# convert the object into a dict
print_service_create_pd_ffrom_job_force_template_request_dict = print_service_create_pd_ffrom_job_force_template_request_instance.to_dict()
# create an instance of PrintServiceCreatePDFfromJobForceTemplateRequest from a dict
print_service_create_pd_ffrom_job_force_template_request_from_dict = PrintServiceCreatePDFfromJobForceTemplateRequest.from_dict(print_service_create_pd_ffrom_job_force_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


