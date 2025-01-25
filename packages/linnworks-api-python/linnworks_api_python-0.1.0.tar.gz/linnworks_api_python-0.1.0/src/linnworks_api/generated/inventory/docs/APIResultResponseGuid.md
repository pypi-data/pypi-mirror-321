# APIResultResponseGuid


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] 
**result_status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.api_result_response_guid import APIResultResponseGuid

# TODO update the JSON string below
json = "{}"
# create an instance of APIResultResponseGuid from a JSON string
api_result_response_guid_instance = APIResultResponseGuid.from_json(json)
# print the JSON string representation of the object
print(APIResultResponseGuid.to_json())

# convert the object into a dict
api_result_response_guid_dict = api_result_response_guid_instance.to_dict()
# create an instance of APIResultResponseGuid from a dict
api_result_response_guid_from_dict = APIResultResponseGuid.from_dict(api_result_response_guid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


