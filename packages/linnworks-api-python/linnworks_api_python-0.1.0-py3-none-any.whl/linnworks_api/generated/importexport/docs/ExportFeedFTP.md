# ExportFeedFTP


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**user_name** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**ssl** | **bool** |  | [optional] 
**passive_mode** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.importexport.models.export_feed_ftp import ExportFeedFTP

# TODO update the JSON string below
json = "{}"
# create an instance of ExportFeedFTP from a JSON string
export_feed_ftp_instance = ExportFeedFTP.from_json(json)
# print the JSON string representation of the object
print(ExportFeedFTP.to_json())

# convert the object into a dict
export_feed_ftp_dict = export_feed_ftp_instance.to_dict()
# create an instance of ExportFeedFTP from a dict
export_feed_ftp_from_dict = ExportFeedFTP.from_dict(export_feed_ftp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


