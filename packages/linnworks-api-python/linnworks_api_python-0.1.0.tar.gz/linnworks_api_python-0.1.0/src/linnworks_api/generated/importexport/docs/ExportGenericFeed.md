# ExportGenericFeed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feed_type** | **str** |  | [optional] [readonly] 
**file_name** | **str** |  | [optional] 
**file_path** | **str** |  | [optional] 
**temp_file_name** | **str** |  | [optional] 
**if_file_exist** | **str** |  | [optional] 
**discriminator** | **str** |  | 

## Example

```python
from linnworks_api.generated.importexport.models.export_generic_feed import ExportGenericFeed

# TODO update the JSON string below
json = "{}"
# create an instance of ExportGenericFeed from a JSON string
export_generic_feed_instance = ExportGenericFeed.from_json(json)
# print the JSON string representation of the object
print(ExportGenericFeed.to_json())

# convert the object into a dict
export_generic_feed_dict = export_generic_feed_instance.to_dict()
# create an instance of ExportGenericFeed from a dict
export_generic_feed_from_dict = ExportGenericFeed.from_dict(export_generic_feed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


