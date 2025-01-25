# PrintServiceCreatePDFfromJobForceTemplateStockInRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_type** | **str** | The template type | [optional] 
**printing_keys** | [**List[PrintingKey]**](PrintingKey.md) | A list of IDs to print (e.g. Order IDs or Warehouse Transfer IDs) | [optional] 
**template_id** | **int** | The ID of the template to use | [optional] 
**parameters** | [**List[KeyValueStringString]**](KeyValueStringString.md) |  | [optional] 
**printer_name** | **str** | printer name of the virtual printer to use. If null then the sepecified in the template | [optional] 
**print_zone_code** | **str** | Print zone code, if present, will override the printer used if the template has a set printer for that zone | [optional] 
**page_start_number** | **int** | The starting page of the document to generate from (optional, default to 0) | [optional] 
**operation_id** | **str** | The ID of the current operation, used in logging for tracing (optional, default to null) | [optional] 
**context** | [**ClientContext**](ClientContext.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.printservice.models.print_service_create_pd_ffrom_job_force_template_stock_in_request import PrintServiceCreatePDFfromJobForceTemplateStockInRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PrintServiceCreatePDFfromJobForceTemplateStockInRequest from a JSON string
print_service_create_pd_ffrom_job_force_template_stock_in_request_instance = PrintServiceCreatePDFfromJobForceTemplateStockInRequest.from_json(json)
# print the JSON string representation of the object
print(PrintServiceCreatePDFfromJobForceTemplateStockInRequest.to_json())

# convert the object into a dict
print_service_create_pd_ffrom_job_force_template_stock_in_request_dict = print_service_create_pd_ffrom_job_force_template_stock_in_request_instance.to_dict()
# create an instance of PrintServiceCreatePDFfromJobForceTemplateStockInRequest from a dict
print_service_create_pd_ffrom_job_force_template_stock_in_request_from_dict = PrintServiceCreatePDFfromJobForceTemplateStockInRequest.from_dict(print_service_create_pd_ffrom_job_force_template_stock_in_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


