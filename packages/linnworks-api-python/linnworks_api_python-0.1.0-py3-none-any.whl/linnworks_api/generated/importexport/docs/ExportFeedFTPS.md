# ExportFeedFTPS


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**user_name** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**use_implicit_tls** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.importexport.models.export_feed_ftps import ExportFeedFTPS

# TODO update the JSON string below
json = "{}"
# create an instance of ExportFeedFTPS from a JSON string
export_feed_ftps_instance = ExportFeedFTPS.from_json(json)
# print the JSON string representation of the object
print(ExportFeedFTPS.to_json())

# convert the object into a dict
export_feed_ftps_dict = export_feed_ftps_instance.to_dict()
# create an instance of ExportFeedFTPS from a dict
export_feed_ftps_from_dict = ExportFeedFTPS.from_dict(export_feed_ftps_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


