# UpdateScrapCategoriesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | [**List[ScrapCategory]**](ScrapCategory.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.update_scrap_categories_request import UpdateScrapCategoriesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateScrapCategoriesRequest from a JSON string
update_scrap_categories_request_instance = UpdateScrapCategoriesRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateScrapCategoriesRequest.to_json())

# convert the object into a dict
update_scrap_categories_request_dict = update_scrap_categories_request_instance.to_dict()
# create an instance of UpdateScrapCategoriesRequest from a dict
update_scrap_categories_request_from_dict = UpdateScrapCategoriesRequest.from_dict(update_scrap_categories_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


