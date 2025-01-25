# ViewGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.openorders.models.view_group import ViewGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ViewGroup from a JSON string
view_group_instance = ViewGroup.from_json(json)
# print the JSON string representation of the object
print(ViewGroup.to_json())

# convert the object into a dict
view_group_dict = view_group_instance.to_dict()
# create an instance of ViewGroup from a dict
view_group_from_dict = ViewGroup.from_dict(view_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


