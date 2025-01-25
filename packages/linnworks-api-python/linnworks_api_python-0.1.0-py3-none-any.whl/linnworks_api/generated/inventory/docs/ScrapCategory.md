# ScrapCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_id** | **int** |  | [optional] 
**category_name** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.scrap_category import ScrapCategory

# TODO update the JSON string below
json = "{}"
# create an instance of ScrapCategory from a JSON string
scrap_category_instance = ScrapCategory.from_json(json)
# print the JSON string representation of the object
print(ScrapCategory.to_json())

# convert the object into a dict
scrap_category_dict = scrap_category_instance.to_dict()
# create an instance of ScrapCategory from a dict
scrap_category_from_dict = ScrapCategory.from_dict(scrap_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


