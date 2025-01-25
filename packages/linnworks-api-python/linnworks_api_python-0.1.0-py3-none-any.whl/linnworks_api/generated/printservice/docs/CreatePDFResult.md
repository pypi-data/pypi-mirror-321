# CreatePDFResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyed_error** | [**List[PrintError]**](PrintError.md) |  | [optional] 
**url** | **str** | URL to PDF file | [optional] 
**ids_processed** | **List[str]** | List of processed order or item IDs | [optional] 
**processed_ids** | **Dict[str, List[str]]** |  | [optional] 
**page_count** | **int** |  | [optional] 
**print_errors** | **List[str]** | List of OrderId / Error message | [optional] 

## Example

```python
from linnworks_api.generated.printservice.models.create_pdf_result import CreatePDFResult

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePDFResult from a JSON string
create_pdf_result_instance = CreatePDFResult.from_json(json)
# print the JSON string representation of the object
print(CreatePDFResult.to_json())

# convert the object into a dict
create_pdf_result_dict = create_pdf_result_instance.to_dict()
# create an instance of CreatePDFResult from a dict
create_pdf_result_from_dict = CreatePDFResult.from_dict(create_pdf_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


