# BaseSession


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**entity_id** | **str** |  | [optional] 
**database_name** | **str** |  | [optional] 
**database_server** | **str** |  | [optional] 
**private_database_server** | **str** |  | [optional] 
**database_user** | **str** |  | [optional] 
**database_password** | **str** |  | [optional] 
**app_name** | **str** |  | [optional] 
**sid_registration** | **str** |  | [optional] [readonly] 
**user_name** | **str** |  | [optional] 
**md5_hash** | **str** |  | [optional] 
**locality** | **str** |  | [optional] 
**super_admin** | **bool** |  | [optional] 
**ttl** | **int** |  | [optional] 
**token** | **str** |  | [optional] 
**access_token** | **str** |  | [optional] 
**group_name** | **str** |  | [optional] 
**device** | **str** |  | [optional] 
**device_type** | **str** |  | [optional] 
**user_type** | **str** |  | [optional] 
**status** | [**StatusDetails**](StatusDetails.md) |  | [optional] 
**user_id** | **str** |  | [optional] 
**properties** | **Dict[str, str]** |  | [optional] 
**email** | **str** |  | [optional] 
**server** | **str** |  | [optional] 
**push_server** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.auth.models.base_session import BaseSession

# TODO update the JSON string below
json = "{}"
# create an instance of BaseSession from a JSON string
base_session_instance = BaseSession.from_json(json)
# print the JSON string representation of the object
print(BaseSession.to_json())

# convert the object into a dict
base_session_dict = base_session_instance.to_dict()
# create an instance of BaseSession from a dict
base_session_from_dict = BaseSession.from_dict(base_session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


