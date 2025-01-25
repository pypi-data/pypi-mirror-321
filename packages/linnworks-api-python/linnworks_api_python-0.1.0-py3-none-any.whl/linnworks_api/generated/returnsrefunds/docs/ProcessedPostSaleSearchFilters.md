# ProcessedPostSaleSearchFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actionable** | **bool** |  | [optional] [readonly] 
**type** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.processed_post_sale_search_filters import ProcessedPostSaleSearchFilters

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessedPostSaleSearchFilters from a JSON string
processed_post_sale_search_filters_instance = ProcessedPostSaleSearchFilters.from_json(json)
# print the JSON string representation of the object
print(ProcessedPostSaleSearchFilters.to_json())

# convert the object into a dict
processed_post_sale_search_filters_dict = processed_post_sale_search_filters_instance.to_dict()
# create an instance of ProcessedPostSaleSearchFilters from a dict
processed_post_sale_search_filters_from_dict = ProcessedPostSaleSearchFilters.from_dict(processed_post_sale_search_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


