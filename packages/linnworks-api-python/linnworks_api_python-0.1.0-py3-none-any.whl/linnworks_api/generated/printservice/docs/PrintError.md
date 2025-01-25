# PrintError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_type** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**error** | **str** |  | [optional] 
**tags** | [**List[PrintErrorTags]**](PrintErrorTags.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.printservice.models.print_error import PrintError

# TODO update the JSON string below
json = "{}"
# create an instance of PrintError from a JSON string
print_error_instance = PrintError.from_json(json)
# print the JSON string representation of the object
print(PrintError.to_json())

# convert the object into a dict
print_error_dict = print_error_instance.to_dict()
# create an instance of PrintError from a dict
print_error_from_dict = PrintError.from_dict(print_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


