# StatusDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 
**parameters** | **Dict[str, str]** |  | [optional] 

## Example

```python
from linnworks_api.generated.auth.models.status_details import StatusDetails

# TODO update the JSON string below
json = "{}"
# create an instance of StatusDetails from a JSON string
status_details_instance = StatusDetails.from_json(json)
# print the JSON string representation of the object
print(StatusDetails.to_json())

# convert the object into a dict
status_details_dict = status_details_instance.to_dict()
# create an instance of StatusDetails from a dict
status_details_from_dict = StatusDetails.from_dict(status_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


