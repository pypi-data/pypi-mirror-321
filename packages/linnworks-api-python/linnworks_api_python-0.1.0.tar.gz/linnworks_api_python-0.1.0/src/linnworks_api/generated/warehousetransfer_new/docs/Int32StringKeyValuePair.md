# Int32StringKeyValuePair


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **int** |  | [optional] [readonly] 
**value** | **str** |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.int32_string_key_value_pair import Int32StringKeyValuePair

# TODO update the JSON string below
json = "{}"
# create an instance of Int32StringKeyValuePair from a JSON string
int32_string_key_value_pair_instance = Int32StringKeyValuePair.from_json(json)
# print the JSON string representation of the object
print(Int32StringKeyValuePair.to_json())

# convert the object into a dict
int32_string_key_value_pair_dict = int32_string_key_value_pair_instance.to_dict()
# create an instance of Int32StringKeyValuePair from a dict
int32_string_key_value_pair_from_dict = Int32StringKeyValuePair.from_dict(int32_string_key_value_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


