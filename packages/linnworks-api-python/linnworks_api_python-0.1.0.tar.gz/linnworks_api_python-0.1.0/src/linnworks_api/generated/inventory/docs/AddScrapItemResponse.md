# AddScrapItemResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scrap_item** | [**ScrapItem**](ScrapItem.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.add_scrap_item_response import AddScrapItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddScrapItemResponse from a JSON string
add_scrap_item_response_instance = AddScrapItemResponse.from_json(json)
# print the JSON string representation of the object
print(AddScrapItemResponse.to_json())

# convert the object into a dict
add_scrap_item_response_dict = add_scrap_item_response_instance.to_dict()
# create an instance of AddScrapItemResponse from a dict
add_scrap_item_response_from_dict = AddScrapItemResponse.from_dict(add_scrap_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


