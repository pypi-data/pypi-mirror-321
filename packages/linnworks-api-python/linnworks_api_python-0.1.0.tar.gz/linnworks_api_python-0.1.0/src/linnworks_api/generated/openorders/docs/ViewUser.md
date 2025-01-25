# ViewUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**is_owner** | **bool** |  | [optional] 
**user_id** | **int** |  | [optional] 
**email_address** | **str** |  | [optional] 
**user_type** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.openorders.models.view_user import ViewUser

# TODO update the JSON string below
json = "{}"
# create an instance of ViewUser from a JSON string
view_user_instance = ViewUser.from_json(json)
# print the JSON string representation of the object
print(ViewUser.to_json())

# convert the object into a dict
view_user_dict = view_user_instance.to_dict()
# create an instance of ViewUser from a dict
view_user_from_dict = ViewUser.from_dict(view_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


