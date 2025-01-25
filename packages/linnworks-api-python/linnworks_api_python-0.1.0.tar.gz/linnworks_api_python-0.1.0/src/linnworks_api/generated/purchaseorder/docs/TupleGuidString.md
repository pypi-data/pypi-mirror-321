# TupleGuidString


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item1** | **str** |  | [optional] [readonly] 
**item2** | **str** |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.tuple_guid_string import TupleGuidString

# TODO update the JSON string below
json = "{}"
# create an instance of TupleGuidString from a JSON string
tuple_guid_string_instance = TupleGuidString.from_json(json)
# print the JSON string representation of the object
print(TupleGuidString.to_json())

# convert the object into a dict
tuple_guid_string_dict = tuple_guid_string_instance.to_dict()
# create an instance of TupleGuidString from a dict
tuple_guid_string_from_dict = TupleGuidString.from_dict(tuple_guid_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


