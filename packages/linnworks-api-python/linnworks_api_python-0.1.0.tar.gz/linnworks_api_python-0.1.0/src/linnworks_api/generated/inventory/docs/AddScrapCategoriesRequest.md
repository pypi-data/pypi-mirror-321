# AddScrapCategoriesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_names** | **List[str]** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.add_scrap_categories_request import AddScrapCategoriesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddScrapCategoriesRequest from a JSON string
add_scrap_categories_request_instance = AddScrapCategoriesRequest.from_json(json)
# print the JSON string representation of the object
print(AddScrapCategoriesRequest.to_json())

# convert the object into a dict
add_scrap_categories_request_dict = add_scrap_categories_request_instance.to_dict()
# create an instance of AddScrapCategoriesRequest from a dict
add_scrap_categories_request_from_dict = AddScrapCategoriesRequest.from_dict(add_scrap_categories_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


