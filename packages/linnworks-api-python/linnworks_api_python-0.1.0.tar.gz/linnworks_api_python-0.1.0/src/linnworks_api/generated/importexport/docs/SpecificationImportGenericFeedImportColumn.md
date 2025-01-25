# SpecificationImportGenericFeedImportColumn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feed** | [**ImportGenericFeed**](ImportGenericFeed.md) |  | [optional] 
**column_mappings** | [**List[ImportColumn]**](ImportColumn.md) |  | [optional] 
**execution_options** | [**List[ExecutionOption]**](ExecutionOption.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.importexport.models.specification_import_generic_feed_import_column import SpecificationImportGenericFeedImportColumn

# TODO update the JSON string below
json = "{}"
# create an instance of SpecificationImportGenericFeedImportColumn from a JSON string
specification_import_generic_feed_import_column_instance = SpecificationImportGenericFeedImportColumn.from_json(json)
# print the JSON string representation of the object
print(SpecificationImportGenericFeedImportColumn.to_json())

# convert the object into a dict
specification_import_generic_feed_import_column_dict = specification_import_generic_feed_import_column_instance.to_dict()
# create an instance of SpecificationImportGenericFeedImportColumn from a dict
specification_import_generic_feed_import_column_from_dict = SpecificationImportGenericFeedImportColumn.from_dict(specification_import_generic_feed_import_column_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


