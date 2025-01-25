# DropboxAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**token** | **str** |  | [optional] 
**uid** | **str** |  | [optional] 
**account_id** | **str** |  | [optional] 
**api_version** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.importexport.models.dropbox_account import DropboxAccount

# TODO update the JSON string below
json = "{}"
# create an instance of DropboxAccount from a JSON string
dropbox_account_instance = DropboxAccount.from_json(json)
# print the JSON string representation of the object
print(DropboxAccount.to_json())

# convert the object into a dict
dropbox_account_dict = dropbox_account_instance.to_dict()
# create an instance of DropboxAccount from a dict
dropbox_account_from_dict = DropboxAccount.from_dict(dropbox_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


