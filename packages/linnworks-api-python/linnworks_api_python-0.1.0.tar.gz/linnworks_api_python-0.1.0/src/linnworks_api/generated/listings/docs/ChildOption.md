# ChildOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**option_id** | **int** |  | [optional] 
**value_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**label** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.child_option import ChildOption

# TODO update the JSON string below
json = "{}"
# create an instance of ChildOption from a JSON string
child_option_instance = ChildOption.from_json(json)
# print the JSON string representation of the object
print(ChildOption.to_json())

# convert the object into a dict
child_option_dict = child_option_instance.to_dict()
# create an instance of ChildOption from a dict
child_option_from_dict = ChildOption.from_dict(child_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


