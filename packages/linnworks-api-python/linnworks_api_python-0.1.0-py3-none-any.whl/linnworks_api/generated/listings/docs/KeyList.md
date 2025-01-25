# KeyList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**values** | **List[str]** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.key_list import KeyList

# TODO update the JSON string below
json = "{}"
# create an instance of KeyList from a JSON string
key_list_instance = KeyList.from_json(json)
# print the JSON string representation of the object
print(KeyList.to_json())

# convert the object into a dict
key_list_dict = key_list_instance.to_dict()
# create an instance of KeyList from a dict
key_list_from_dict = KeyList.from_dict(key_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


