# ImportColumn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_data** | [**List[AddData]**](AddData.md) |  | [optional] 
**file_column** | **str** |  | [optional] 
**column** | **str** |  | [optional] 
**expression** | **str** |  | [optional] 
**default_value** | **str** |  | [optional] 
**visible** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.importexport.models.import_column import ImportColumn

# TODO update the JSON string below
json = "{}"
# create an instance of ImportColumn from a JSON string
import_column_instance = ImportColumn.from_json(json)
# print the JSON string representation of the object
print(ImportColumn.to_json())

# convert the object into a dict
import_column_dict = import_column_instance.to_dict()
# create an instance of ImportColumn from a dict
import_column_from_dict = ImportColumn.from_dict(import_column_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


