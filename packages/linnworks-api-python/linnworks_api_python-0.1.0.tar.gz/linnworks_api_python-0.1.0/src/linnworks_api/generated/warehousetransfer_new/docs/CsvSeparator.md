# CsvSeparator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**CsvSeparatorType**](CsvSeparatorType.md) |  | [optional] 
**value** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.csv_separator import CsvSeparator

# TODO update the JSON string below
json = "{}"
# create an instance of CsvSeparator from a JSON string
csv_separator_instance = CsvSeparator.from_json(json)
# print the JSON string representation of the object
print(CsvSeparator.to_json())

# convert the object into a dict
csv_separator_dict = csv_separator_instance.to_dict()
# create an instance of CsvSeparator from a dict
csv_separator_from_dict = CsvSeparator.from_dict(csv_separator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


