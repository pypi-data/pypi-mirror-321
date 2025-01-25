# TempFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.temp_file import TempFile

# TODO update the JSON string below
json = "{}"
# create an instance of TempFile from a JSON string
temp_file_instance = TempFile.from_json(json)
# print the JSON string representation of the object
print(TempFile.to_json())

# convert the object into a dict
temp_file_dict = temp_file_instance.to_dict()
# create an instance of TempFile from a dict
temp_file_from_dict = TempFile.from_dict(temp_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


