# AuthGetApplicationProfileBySecretKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** | Your application Id | [optional] 
**application_secret** | **str** | Your application secret key | [optional] 
**user_id** | **str** | User Id (Id field of the session) | [optional] 

## Example

```python
from linnworks_api.generated.auth.models.auth_get_application_profile_by_secret_key_request import AuthGetApplicationProfileBySecretKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthGetApplicationProfileBySecretKeyRequest from a JSON string
auth_get_application_profile_by_secret_key_request_instance = AuthGetApplicationProfileBySecretKeyRequest.from_json(json)
# print the JSON string representation of the object
print(AuthGetApplicationProfileBySecretKeyRequest.to_json())

# convert the object into a dict
auth_get_application_profile_by_secret_key_request_dict = auth_get_application_profile_by_secret_key_request_instance.to_dict()
# create an instance of AuthGetApplicationProfileBySecretKeyRequest from a dict
auth_get_application_profile_by_secret_key_request_from_dict = AuthGetApplicationProfileBySecretKeyRequest.from_dict(auth_get_application_profile_by_secret_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


