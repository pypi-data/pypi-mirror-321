# ActionablePostSaleSearchFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actionable** | **bool** |  | [optional] [readonly] 
**type** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.actionable_post_sale_search_filters import ActionablePostSaleSearchFilters

# TODO update the JSON string below
json = "{}"
# create an instance of ActionablePostSaleSearchFilters from a JSON string
actionable_post_sale_search_filters_instance = ActionablePostSaleSearchFilters.from_json(json)
# print the JSON string representation of the object
print(ActionablePostSaleSearchFilters.to_json())

# convert the object into a dict
actionable_post_sale_search_filters_dict = actionable_post_sale_search_filters_instance.to_dict()
# create an instance of ActionablePostSaleSearchFilters from a dict
actionable_post_sale_search_filters_from_dict = ActionablePostSaleSearchFilters.from_dict(actionable_post_sale_search_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


