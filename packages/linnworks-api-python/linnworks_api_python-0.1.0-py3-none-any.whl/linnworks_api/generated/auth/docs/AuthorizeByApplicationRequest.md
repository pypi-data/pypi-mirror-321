# AuthorizeByApplicationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** |  | [optional] 
**application_secret** | **str** |  | [optional] 
**token** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.auth.models.authorize_by_application_request import AuthorizeByApplicationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizeByApplicationRequest from a JSON string
authorize_by_application_request_instance = AuthorizeByApplicationRequest.from_json(json)
# print the JSON string representation of the object
print(AuthorizeByApplicationRequest.to_json())

# convert the object into a dict
authorize_by_application_request_dict = authorize_by_application_request_instance.to_dict()
# create an instance of AuthorizeByApplicationRequest from a dict
authorize_by_application_request_from_dict = AuthorizeByApplicationRequest.from_dict(authorize_by_application_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


