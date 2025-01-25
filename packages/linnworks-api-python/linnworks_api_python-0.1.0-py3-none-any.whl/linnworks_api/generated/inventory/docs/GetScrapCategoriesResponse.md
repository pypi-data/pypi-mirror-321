# GetScrapCategoriesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scrap_categories** | [**List[ScrapCategory]**](ScrapCategory.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.get_scrap_categories_response import GetScrapCategoriesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetScrapCategoriesResponse from a JSON string
get_scrap_categories_response_instance = GetScrapCategoriesResponse.from_json(json)
# print the JSON string representation of the object
print(GetScrapCategoriesResponse.to_json())

# convert the object into a dict
get_scrap_categories_response_dict = get_scrap_categories_response_instance.to_dict()
# create an instance of GetScrapCategoriesResponse from a dict
get_scrap_categories_response_from_dict = GetScrapCategoriesResponse.from_dict(get_scrap_categories_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


