# PrintErrorTags


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.printservice.models.print_error_tags import PrintErrorTags

# TODO update the JSON string below
json = "{}"
# create an instance of PrintErrorTags from a JSON string
print_error_tags_instance = PrintErrorTags.from_json(json)
# print the JSON string representation of the object
print(PrintErrorTags.to_json())

# convert the object into a dict
print_error_tags_dict = print_error_tags_instance.to_dict()
# create an instance of PrintErrorTags from a dict
print_error_tags_from_dict = PrintErrorTags.from_dict(print_error_tags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


