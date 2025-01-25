# DeleteScrapCategoriesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_ids** | **List[int]** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.delete_scrap_categories_request import DeleteScrapCategoriesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteScrapCategoriesRequest from a JSON string
delete_scrap_categories_request_instance = DeleteScrapCategoriesRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteScrapCategoriesRequest.to_json())

# convert the object into a dict
delete_scrap_categories_request_dict = delete_scrap_categories_request_instance.to_dict()
# create an instance of DeleteScrapCategoriesRequest from a dict
delete_scrap_categories_request_from_dict = DeleteScrapCategoriesRequest.from_dict(delete_scrap_categories_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


