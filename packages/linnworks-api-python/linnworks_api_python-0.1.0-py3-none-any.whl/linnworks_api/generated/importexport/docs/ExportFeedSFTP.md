# ExportFeedSFTP


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**user_name** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**compression** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.importexport.models.export_feed_sftp import ExportFeedSFTP

# TODO update the JSON string below
json = "{}"
# create an instance of ExportFeedSFTP from a JSON string
export_feed_sftp_instance = ExportFeedSFTP.from_json(json)
# print the JSON string representation of the object
print(ExportFeedSFTP.to_json())

# convert the object into a dict
export_feed_sftp_dict = export_feed_sftp_instance.to_dict()
# create an instance of ExportFeedSFTP from a dict
export_feed_sftp_from_dict = ExportFeedSFTP.from_dict(export_feed_sftp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


