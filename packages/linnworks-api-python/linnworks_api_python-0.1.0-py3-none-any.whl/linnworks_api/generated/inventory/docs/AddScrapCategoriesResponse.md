# AddScrapCategoriesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scrap_categories** | [**List[ScrapCategory]**](ScrapCategory.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.add_scrap_categories_response import AddScrapCategoriesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddScrapCategoriesResponse from a JSON string
add_scrap_categories_response_instance = AddScrapCategoriesResponse.from_json(json)
# print the JSON string representation of the object
print(AddScrapCategoriesResponse.to_json())

# convert the object into a dict
add_scrap_categories_response_dict = add_scrap_categories_response_instance.to_dict()
# create an instance of AddScrapCategoriesResponse from a dict
add_scrap_categories_response_from_dict = AddScrapCategoriesResponse.from_dict(add_scrap_categories_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


