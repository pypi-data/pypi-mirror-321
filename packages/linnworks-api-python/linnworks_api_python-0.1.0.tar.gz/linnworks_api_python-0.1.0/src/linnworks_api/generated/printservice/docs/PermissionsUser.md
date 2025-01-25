# PermissionsUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | [optional] 
**fk_user_id** | **str** |  | [optional] 
**super_admin** | **bool** |  | [optional] 
**email_address** | **str** |  | [optional] 
**user_type** | **str** |  | [optional] 
**totp_authentication_enabled** | **bool** |  | [optional] 
**password_problems** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.printservice.models.permissions_user import PermissionsUser

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionsUser from a JSON string
permissions_user_instance = PermissionsUser.from_json(json)
# print the JSON string representation of the object
print(PermissionsUser.to_json())

# convert the object into a dict
permissions_user_dict = permissions_user_instance.to_dict()
# create an instance of PermissionsUser from a dict
permissions_user_from_dict = PermissionsUser.from_dict(permissions_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


