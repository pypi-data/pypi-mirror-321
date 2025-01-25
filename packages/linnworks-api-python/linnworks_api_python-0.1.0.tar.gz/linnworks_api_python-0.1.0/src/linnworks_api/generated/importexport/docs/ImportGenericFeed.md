# ImportGenericFeed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feed_type** | **str** |  | [optional] [readonly] 
**encoding** | **str** |  | [optional] 
**delimiter** | **str** |  | [optional] 
**comment** | **str** |  | [optional] 
**has_headers** | **bool** |  | [optional] 
**escape** | **str** |  | [optional] 
**quote** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.importexport.models.import_generic_feed import ImportGenericFeed

# TODO update the JSON string below
json = "{}"
# create an instance of ImportGenericFeed from a JSON string
import_generic_feed_instance = ImportGenericFeed.from_json(json)
# print the JSON string representation of the object
print(ImportGenericFeed.to_json())

# convert the object into a dict
import_generic_feed_dict = import_generic_feed_instance.to_dict()
# create an instance of ImportGenericFeed from a dict
import_generic_feed_from_dict = ImportGenericFeed.from_dict(import_generic_feed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


