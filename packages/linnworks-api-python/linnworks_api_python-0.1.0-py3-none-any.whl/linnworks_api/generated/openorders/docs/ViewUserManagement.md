# ViewUserManagement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view_id** | **int** |  | [optional] [readonly] 
**view_users** | [**List[ViewUser]**](ViewUser.md) |  | [optional] 
**view_groups** | [**List[ViewGroup]**](ViewGroup.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.openorders.models.view_user_management import ViewUserManagement

# TODO update the JSON string below
json = "{}"
# create an instance of ViewUserManagement from a JSON string
view_user_management_instance = ViewUserManagement.from_json(json)
# print the JSON string representation of the object
print(ViewUserManagement.to_json())

# convert the object into a dict
view_user_management_dict = view_user_management_instance.to_dict()
# create an instance of ViewUserManagement from a dict
view_user_management_from_dict = ViewUserManagement.from_dict(view_user_management_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


